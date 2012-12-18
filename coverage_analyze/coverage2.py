#!/usr/bin/python
import sys,getopt
import re
from sets import Set

def main(argv):
	#python blah.py -i ../verilog/rs.v -o ../verilog/blahout.v
	inputfile,outputfile,outputfilestate = handleinputs(argv)
	trace = open(inputfile,'r')
	traceout = open(outputfile,'w')
	#traceout.write("blah\n\t")
        symbols =[]
	uniquename={}
	phase = 0
	bitjoined = Set([])
	clocks = 0
	lncnt = 0
	delay = ""
	while (True):
		line = trace.readline()
		lncnt = lncnt+1
		if ( (lncnt % 50000) == 0):
			print lncnt
		if (line==''):
			#also push the uniquename into set.
			bits=[]
			for symbol in s:
				bits.append(uniquename[symbol])
			bitjoined.add("".join(bits))
			numBits = 0 
			for bit in bits:
				numBits = numBits + len(bit)
			print "total number of bits = " + str(numBits)
			print "total number of symbols = " + str(len(uniquename))
			traceout.write(delay+","+str(len(bitjoined))+"\n")
			clocks = clocks+1
			break 
		if (phase == 0): #parse the preamble of the file to acquire all symbols.
	                pattern = re.findall('\$var \w+ [0-9]+ ([^\s]*)',line)
			if (pattern != []):
				symbols.append(pattern[0])
                if (line == "#0\n"): #transitioning from phase 0 -> 1 (or parsing preamble -> parsing stuff underneath #0)
        		for i in symbols:
				uniquename[i]=0
			phase=1
			delay="0"
			s = uniquename.keys()
			s.sort()
		elif (phase == 1): #start parsing the rest of the file.i
			if (line[0]=="#"):
				bits = []
				for symbol in s:
					bits.append(uniquename[symbol])
				bitjoined.add("".join(bits))
				traceout.write(delay+","+str(len(bitjoined))+"\n")
				delay=line[1:-1]
				clocks=clocks+1
				continue
			if (line[0]!="b" and line[0:5]!="$dump" and line[0:4]!="$end"): #one bit
				currentSymbol = line[1:-1]
				currentState = line[0]
				uniquename[currentSymbol]=currentState
			elif (line[0]=="b"):
				stateAndSymbol = re.findall('b([01zx]+) (.*)$',line)
				stateAndSymbol = stateAndSymbol[0]
				currentSymbol = stateAndSymbol[1]
				currentState = stateAndSymbol[0]
				uniquename[currentSymbol]=currentState
	print "Total number of states visited: " + str(len(bitjoined))
	print "Total number of transition: " + str(clocks)
def handleinputs(argv):
	inputfile=''
	outputfile=''
	outputfilestate=''
	try:
		opts,args=getopt.getopt(argv,"i:o:")
	except getopt.GetoptError:
		print "error!"
		sys.exit(2)
	for opt, arg in opts:
		if (opt=="-i"):
			inputfile=arg
		if (opt=="-o"):
			outputfile=arg
		if (opt=="-s"):
			outputfilestate=arg
	return inputfile,outputfile,outputfilestate

#def grapsymbols(trace):

if __name__ == '__main__':
	main(sys.argv[1:])
	
