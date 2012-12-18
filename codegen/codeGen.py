#!/usr/bin/python
import os
import sys, getopt
import re
from parseTemplate import *
from printHeader import printHeader
from shutil import copyfile
from stateeng import *
'''
main loop.
'''
def main(argv):
	inputfile,outputfile=handleinputs(argv)
	printHeader("memincludes",outputfile)
	instrLib=readInstrLib("instructionLib.txt")
	rnode=parseTemplate(inputfile,outputfile,instrLib)
	fw = open(outputfile,'a') #open it here so recursive function doesn't open it
	#a bunch of times
	engine = StateEngine(rnode)
	executeTemplate(rnode,fw,instrLib,engine)
	fw.close()

'''
Handles input/output file checking/help.
'''
def handleinputs(argv):
	inputfile=''
	outputfile=''

	try:
		opts,args=getopt.getopt(argv,"i:o:")
	except getopt.GetoptError:
		print "Do codeGen.py -i [templatefile] -o [assemblyfile]"
		sys.exit(2)
	if (len(opts)!=2):
		print "Please do codeGen.py -h for more information"
		sys.exit(2)
	for opt, arg in opts:
		if (opt=="-h"):
			print "USAGE: python codeGen.py -i [templatefile] -o [assemblyfile]"
		if (opt=="-o"):
			outputfile=arg
		if (opt=="-i"):
			inputfile=arg
	return inputfile,outputfile



if __name__ == '__main__':
	main(sys.argv[1:])
