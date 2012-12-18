import re
import string
import shlex
import sys
from mynode import *
import random
import copy

def executeTemplate(rnode,fw,instrLib,eng):
	#given current node, check what it is supposed to do.
	if (rnode.isProgram()):
		#program root, execute children.
		for i in range(len(rnode.children)):
			cnode = rnode.children[i]
			executeTemplate(cnode,fw,instrLib,eng)
	else:
		tmpData = rnode.data
		directive = re.findall('\s*(.*):',tmpData)
		directive = directive[0]
		#print directive
		if (rnode.isLeaf()):
			#primitive, just slap down instruction
			line = re.findall('instr:\s*(.*)$',rnode.data)
			if (line!=[]):
				line=line[0]
				instr = re.findall('(.*?)\s',line)
				if (instr!=[]):
					instr = instr[0]
				else: #nop and one-word instr case
					instr = line
				srcdest = re.findall('.*?\s+(.*?)\s*=\s*(.*)$',line)
				#srcdest [] or tuple of lhs and rhs
				if (srcdest!=[]):
					srcdest=srcdest[0]	
				parseLine(instr,srcdest,instrLib[instr],eng,fw,line)
			elif(directive[0:5] == "macro"):
				mac = re.findall('\s*.*:\s*(.*)$',tmpData)
				if (mac==[]):
					mac = ""
				else:
					mac = mac[0]
				fw.write("\t"+mac+"\n")
			#fw.write()
			return
		elif (directive == "one of"):
			r = random.randint(0,len(rnode.children)-1)
			cnode = rnode.children[r]
			executeTemplate(cnode,fw,instrLib,eng)
		elif (directive[0:6] == "repeat"):
			numrepeats = re.findall('\((.*)\)',directive)
			numrepeats = numrepeats[0]
			numrepeats = int(numrepeats)
			for iter in range(numrepeats):
				for codebit in range(len(rnode.children)):
					cnode = rnode.children[codebit]
					executeTemplate(cnode,fw,instrLib,eng)
		elif (directive[0:6] == "thread"):
			numrepeats = re.findall('\((.*)\)', directive)
			labelname = re.findall('"(.*)"',directive)
			if (labelname==[]):
				print "SYNTAX error: labels need labelnames e.g. thread \"blah\" (optional repetitions):"
			labelname = labelname[0]
			if (numrepeats==[]):
				numrepeats=1
			else:
				numrepeats=numrepeats[0]
				numrepeats=int(numrepeats)
			for iter in range(numrepeats):
				fw.write("\n"+labelname + "_" + str(iter) + ":\n")
				for codebit in range(len(rnode.children)):
					cnode = rnode.children[codebit]
					executeTemplate(cnode,fw,instrLib,eng)
		elif (directive[0:5] == "label"):
			labelname = re.findall('"(.*)"',directive)
			if (labelname==[]):
				print "SYNTAX ERROR: labels need a name. e.g. label \"name\":"
			labelname = labelname[0]
			fw.write("\n"+labelname+":\n")
			for codebit in range(len(rnode.children)):
				cnode = rnode.children[codebit]
				executeTemplate(cnode,fw,instrLib,eng)
		else:
			print "SYNTAX ERROR: " + parent + "at line number: " + str(rnode.parent.lineNum+1)
			sys.exit(2)
	
	return
'''
Parses a particular line of code using instruction library
'''
def parseLine(instr,srcdest,instrTemplateOrig,eng,fw,line):
	privtag = 0 #0 is NONH #1 is CHANGE_PRIV #2 is CHANGE_HPRIV
	#TODO: things with addr and a regsrc at the same time e.g. casa
	#TODO: bury constraints within comments in header 
	#registers--src/dest or src?/dest?
	#addresses--[stuff]
	#literals--not registers can refer to anything manually typed down.
	instrTemplate=copy.deepcopy(instrTemplateOrig)
	for i in range(len(instrTemplate)):
		elements = instrTemplate[i]
		for j in range(len(elements)):
			if ("addr" in elements[j]):
				#addresses are either [blah]disp
				if (instr[0:2]=="st"):
					addr = re.findall('\[.*\].*',srcdest[0])
				else:
					addr = re.findall('\[.*\].*',srcdest[1])
				if (addr!=[]):
					addr = addr[0]
					elements[j] = addr
				else:
					break
			elif ("regsrc" in elements[j]):
				if (len(srcdest)==1):
					break
				elif (len(srcdest)==2):
					src=re.findall('%\w*\??',srcdest[1])
				if (src==[]):
					break
				else:
					if (elements[j]=="regsrc1"):
						elements[j]=src[0]
					elif (elements[j]=="regsrc2"):
						if (len(src)==1):
							break
						else:
							elements[j]=src[1]
			elif (elements[j]=="regdest"):
				if (len(srcdest)==1):
					break
				elif (len(srcdest)==2):
					dest=re.findall('%\w*\??',srcdest[0])
				if (dest==[] or len(dest)!=1):
					break
				else:
					elements[j]=dest[0]
			elif (elements[j]=="value"):
				#values can never be the destination unless it is a constraint.
				#but a constraint is not an instruction.
				if (len(srcdest)==1):
					break
				elif (len(srcdest)==2):
					val = re.findall('0x\w+',srcdest[1]) #try hex
				if (val==[]):
					val = re.findall('random([0-9]+)',line) #try random case
					prefix = re.findall('([0-9]+)random[0-9]+',line) #prefix
					if (val!=[]):
						lst = [random.choice(string.hexdigits) for n in xrange(int(val[0]))]
						str = "".join(lst)
						if (prefix==[]):
							str = "0x"+str
						else:
							str = "0x"+prefix[0]+str
						str = str.lower()
						val = str
						elements[j]=val
					else:
						val = re.findall('[0-9]+',srcdest[1]) #try decimal, put farthest to the right.
						if (val!=[]):
							val = val[-1]
							elements[j]=val
						else:
							break
				else:
					elements[j]=val[0]
			elif (elements[j]=="label"):
				if (len(srcdest)==1):
					break
				elif (len(srcdest)==2):
					lab = re.findall('[a-z0-9_]+',srcdest[1])
				elements[j]=lab[0]
			elif (elements[j]=="macro"):
				mac = re.findall('[A-Z_]+',line)
				elements[j]=mac[0]
			elif (elements[j]=="%cleanwin"):
				elements[j]=="%cleanwin"
			else:
				#this is something literal to write down.
				#print "\t"+elements[j]
				fw.write("\t"+elements[j]+"\n")
				return
		if (j==len(elements)-1):
			#found an appropriate usage of current instr.
			break
		elif (i==len(instrTemplate)-1):
			#broke out of inner loop
			#also last usage of current instruction is explored
			print "Syntax error for current instruction: " + instr
		#otherwise continue to search for another usage.
	elcopy = copy.deepcopy(elements)
	completedFields=eng.constrainLine(elcopy)
	#print "\t" + instr + " " + ",".join(completedFields)
	fw.write("\t" + instr + "\t" + ",".join(completedFields)+"\n")

'''
parses instruction file, uses keywords:
repeat(n)
oneof
instr

above clarifiers all have colons.  repeat and oneof works like python, uses tabulation
to determine when a particular frame ends
'''
def parseTemplate(fread,fwrite,instrLib):
	fr = open(fread)
	tabNumPrev=0
	lineNum=0
	tabVector=[]
	errflg=0
	while(True):
		a = fr.readline()
		firstNonSpace = re.findall('\s*(.)',a)
		iswhitespace = re.findall('\w',a)
		if (a==''):
			break
		elif (firstNonSpace!=[] and firstNonSpace[0]=="!"): #skip lines that are pure comments
			tabVector.append(-1) #-1 implies a commented line, don't do anything with them.
			#preserve line numbers with index of tabVector
			continue
		elif (iswhitespace==[]): #this line is pure whitespace
			tabVector.append(-1)
			continue
		else:
			tabs=re.findall('(\t*)[^\t]',a)
			tabNum=re.findall('\t',tabs[0])
			tabNum = len(tabNum)
			tabVector.append(tabNum)
			if ((tabNum-tabNumPrev)>1):
				print "Syntax error: extra tabulation at line " + str(lineNum+1) + ": " + a
				errflg=1
			tabNumPrev = tabNum
		lineNum=lineNum+1
	if (errflg==1):
		sys.exit(2)
	#now build a tree
	fr.close()
	pnode = Node() #parent node
	rnode = Node() #root node
	rnode = pnode #allows me to do pnode = Node() a bunch of times for each generation.
	deepest = max(tabVector)
	cnodelist = []
	pnodelist = [pnode]
	pIdx = [-1]
	k=0 #pnode progress
	'''
	Cidx arrays that describe next layer of tree.  Tree wants to know which code
	is embedded and which isn't (determined by number of tabs)
	So more tabs => deeper in tree.
	The C/Pidx arrays will have integers that describe which lines in the code
	contain the current layer of depth described by i in range(deepest+1)
	'''
	for i in range(deepest+1):
		k=0
		L = len(pIdx)
		cIdx = [j for j, x in enumerate(tabVector) if x==i]
		fr=open(fread)
		for i, line in enumerate(fr):
			if i in cIdx:
				while(True):
					#last element: every child must have parent
					#thus, this child's parent must trivially be
					#the last index
					if (L==(k+1)): 
						cnode = Node()
						cnode.data = line
						cnode.parent = pnodelist[k]
						cnode.lineNum = i
						pnodelist[k].children.append(cnode)
						cnodelist.append(cnode)
						break #found parent.
					elif (i < pIdx[k+1]):
						cnode = Node() #child node
						cnode.data = line #data is line instruction
						cnode.parent = pnodelist[k] #parent program root of tree.
						cnode.lineNum = i
						pnodelist[k].children.append(cnode) #one pnode
						cnodelist.append(cnode) #for entire layer
						break #found parent
					elif (i > pIdx[k+1]):
						k=k+1 #no need to break b/c arrays built
						#guarantee non-inf loop
					else:
						print "unreachable! bug in code?"
						sys.exit(2)
		pnodelist=cnodelist #for next iteration
		cnodelist=[]
		fr.close()
		pIdx = cIdx
	#for j in range(len(rnode.children)):
	#	for k in range(len(rnode.children[j].children)):
	#		for l in range(len(rnode.children[j].children[k].children)):
	#			for m in range (len(rnode.children[j].children[k].children[l].children)):
	#				print rnode.children[j].children[k].children[l].children[m].data
	return rnode	

def readInstrLib(fread):
	fr = open(fread)
	instrLib = {} #in format: keys=instructions, values=[[one,way,to,use],[alternative,usage]]
	instrSyntaxArray = []
	#read instruction library file:
	while(True):
		a=fr.readline()
		if(a==''):
			break
		else:
			instrName=re.findall('(.*):',a)
			instrSyntaxArray = re.findall(':\s*(.*)$',a)
			my_splitter = shlex.shlex(instrSyntaxArray[0],posix=True)
			my_splitter.whitespace += ','
			my_splitter.whitespace_split = True
			if (instrLib.get(instrName[0])==None): #first usage of instr.
				instrLib[instrName[0]] = [list(my_splitter)]
			else: #instr is already had.
				instrLib[instrName[0]].append(list(my_splitter))
	return instrLib
