import random
import re

class StateEngine(object):
	#TODO: keep state
	def __init__ (self,rnode):
		self.variables={} #keys: var names, values, their values
		self.constraints={} #keys: operation: constraint
		self.rnode = rnode #root node of template program
	'''
	Constrains a particular line of code with "?" to something more solid.
	More sophisticated: could take in current state info.
	'''
	def constrainLine(self,clauses):
		#right now only ? on variables, maybe constrain addresses later.
		#glio0-7
		#clauses is a list with fields to be printed in file
		#they can have unresolved ?s
		for i in range(len(clauses)):
			question = re.findall('%.*\?',clauses[i])
			if (question==[]):
				continue
			else:
				for j in range(len(question)):
					reg = re.findall('%[glio]\?',question[j])
					if (reg!=[]):
						reg = reg[0]
						rname = reg[0:2]
						r = random.randint(0,7)
						varname = rname+str(r)
						if (varname not in self.variables):
							#todo: keep track of stuff assigned
							#to registers so not to assign as to 0 only.
							self.variables[varname]=0
							clauses[i]=varname
						else:
							successfulAssign=0
							for k in range(8):
								varname = rname+str(k)
								if (varname not in self.variables):
									self.variables[varname]=0
									clauses[i]=varname
									successfulAssign=1
									break
							if (successfulAssign==0):
								#can't find any free slots
								#just assign a random one.
								r = random.randint(0,7)
								varname = rname+str(r)
								self.variables[varname]=0
								clauses[i]=varname
					elif (question[j]=="%?"):
						glioletters = 'glio'
						r = random.randint(0,7)
						glio = random.randint(0,3)
						glio = glioletters[glio]
						varname = "%"+glio + str(r)
						if (varname not in self.variables):
							self.variables[varname]=0
							clauses[i]=varname
						else:
							successfulAssign=0
							for regnum in range(8):
								for regname in range(4):
									varname="%"+glioletters[regname] + str(regnum)
									if (varname not in self.variables):
										self.variables[varname]=0
										clauses[i]=varname
										successfulAssign=1
										break
							if (successfulAssign==0):
								glioletters = 'glio'
								r = random.randint(0,7)
								glio=random.randint(0,3)
								glio=glioletters[glio]
								varname="%"+glio + str(r)
								self.variables[varname]=0
								clauses[i]=varname
		return clauses

