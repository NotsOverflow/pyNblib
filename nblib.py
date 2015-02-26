#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 

'''---------------------------------------------------------------------------|
                                                              _____           |
      Autor: Notsgnik                                       /||   /           |
      Email: Labruillere gmail.com                         / ||  /            |
      website: notsgnik.github.io                         /  || /             |
      License: GPL v3                                    /___||/              |
      																		  |
---------------------------------------------------------------------------!'''

msgs = {
	"0" : " [!] Program Error",
	"1" : " [*] Warning Error",
	"2" : " [!] Wrong Data Type"
}
debug_lvl = 0
def debug_msg(msg_nb, lvl = 1):
	"""
		Hello, i'm a debug message function for the curent module.
		You can add debug message to 'msgs' dictionary.
		if the index is not found in 'msgs',
		I will concider that you did that in purpuse
		and you gave me a custom error message that i have to display
	"""
	wtf = "dude wtf!"
	try:
		if type(msg_nb) is not str \
		or type(lvl) is not int \
		or type(debug_lvl) is not int:
			raise Exception(wtf)
	except:
		raise Exception(wtf)
	try:
		error =  msgs[msg_nb]
	except :
		error =  msg_nb

	if debug_lvl < 0 or lvl < 0:
		raise Exception(error)
	elif debug_lvl >= lvl:
		print error

class Instance():
	"""
		Hello, I'm an Instance of Not binary lib.
		I have plany of tools disagned to deal with binary strings
		like converting edian or adding tow hex string value etc...
	"""
	def __init__(self, options = {}):
		"""
			Hello, I'm a initialisation function
			i make sure that stuff needed by the object get loaded or are available
		"""
		#short method name vertion

		self.h2b 	= self.hexStringToByteString
		self.b2h 	= self.byteStringToHexString
		self.iah 	= self.isAsciiHex
		self.lbs 	= self.leByteSwap
		self.lhs 	= self.leHexStringSwap
		self.grh 	= self.getRandomHexString
		self.grb 	= self.getRandomByteString
		self.h2i 	= self.hexStringToInt
		self.b2i 	= self.byteStringToInt
		self.i2h 	= self.intToHexString
		self.i2b 	= self.intToByteString
		self.bc  	= self.byteStringCleaner
		self.sl  	= self.stringsList
		self.cnl 	= self.cleanedStringList
		self.crl 	= self.clearedStringList
		self.ps  	= self.printStrings
		self.sc  	= self.splitChuncks
		self.rb  	= self.remodelByteString
		self.pfb 	= self.printFormatedByteString
		self.pcfb 	= self.printCleanedFormatedByteString

	#original methods


	def hexStringToByteString(self,hstring):
		"""
			Hello, I'm basicly str.encode('hex')
			I turn '010203' into '☺☻♥'
		"""
		try:
			return hstring.decode("hex")
		except:
			debug_msg("2",-1)

	def byteStringToHexString(self,bstring):
		"""
			Hello, I'm basicly str.decode('hex')
			I turn '☺☻♥' into '010203'
		"""
		try:
			return bstring.encode("hex")
		except:
			debug_msg("2",-1)

	def isAsciiHex(self,hstring):
		"""
			Hello, I test if the given string is only made with hexdigits
			Notice that i don't care about case
		"""
		if type(hstring) is not str:
			debug_msg("2",-1)
		for char in hstring:
			c = ord(char)
			if not ((c > 47 and c < 58 ) \
			or ( c > 64 and c < 71 ) \
			or (c > 96 and c < 103 )):
				return False
		return True

	def leByteSwap(self,bstring):
		"""
			Hello, I do littleEdian swap on byte strings
			I turn '☺☻♥' into '♥☻☺'
		"""
		return bstring[::-1]

	def leHexStringSwap(self,hstring):
		"""
			Hello, I do littleEdian swap on hexdigits strings
			i turn '010203' into '030201'
		"""
		return self.byteStringToHexString(self.hexStringToByteString(hstring)[::-1])

	def getRandomHexString(self,size):
		"""
			Hello, I return a random hexdigits String of lenght 'size' in bytes
		"""
		try:
			return "".join([random.choice("0123456789abcdef") for n in xrange(int(size)<<1)])
		except:
			debug_msg("2",-1)

	def getRandomByteString(self,size):
		"""
			Hello, I return a random byte String of lenght 'size' in bytes
		"""
		return self.hexStringToByteString(self.getRandomHexString(size))

	def hexStringToInt(self,hstring):
		"""
			Hello, I return an int value from a hexdigits string
			I turn '010203' into 66051
		"""
		try:
			return int(hstring,16)
		except:
			debug_msg("2",-1)

	def byteStringToInt(self,bstring):
		"""
			Hello, I return an int value from a byte string
			I turn '☺☻♥' into 66051
		"""
		return self.hexStringToInt(self.byteStringToHexString(bstring))

	def intToHexString(self,number,size=-1):
		"""
			Hello, I return a byte string out of an int
			I turn 66051 into '010203' and may had some pading depending on size (in bytes)
		"""
		try:
			number =  "%x" % number
			if (number % 2) == 1:
				number = "0" + number
			nsize = len(number)/2
			delta = size - nsize
			if delta > 0:
				for i in range(delta):
					number = "00" + number
			return number
		except:
			debug_msg("2",-1)

	def intToByteString(self,number,size=-1):
		"""
			Hello, I return a byte string out of an int
			I turn 66051 into '☺☻♥' and may had some pading depending on size (in bytes)
		"""
		return self.hexStringToByteString(self.intToHexString(number,size))

	def byteStringCleaner(self,bstring,creplace=" "):
		"""
			Hello, I return a bytestring where non printable chars become spaces
			I turn '☺☻♥' into '   '
		"""
		result = ""
		for char in bstring:
			o = ord(char)
			if o > 31 and o < 127:
				result += char
			else:
				result += creplace
		return result

	def stringsList(self,bstring):
		"""
			Hello, I return a list of zero terminated byte strings
		"""
		if type(bstring) is not str:
			debug_msg("2",-1)
		result = []
		tmp = ""
		for char in bstring: 
			if char != "\x00":
				tmp += char
			else:
				tmp += char
				result.append(tmp)
				tmp = ""
		if tmp != "":
			result.append(tmp)

	def cleanedStringList(self,bstring):
		"""
			Hello, I return a list of cleaned zero terminated byte strings
		"""
		result = []
		for elem in self.stringsList(bstring):
			result.append(self.byteStringCleaner(elem))
		return result

	def clearedStringList(self,bstring):
		"""
			Hello, I return a cleared list of cleaned zero terminated byte strings
		"""
		result = []
		tmp = ""
		for elem in self.stringsList(bstring):
			tmp = self.byteStringCleaner(elem,"")
			if tmp != "":
				result.append()
		return result

	def printStrings(self,bstring):
		"""
			Hello, I print all zero terminated string that have printable chars
			non printable chars are replaced by spaces and non printable strings
			are removed.
		"""
		for found_string in self.clearedStringList(bstring):
			print found_string

	def splitChuncks(self,bstring,length=2):
		"""
			Hello, I return a list of chunks of 'length' from a byte string
			I turn "abcdef" into ["ab,"cd","ef"]
			using 'length' = 2
		"""
		try:
			return [bstring[i:i+length] for i in range(0, len(bstring), length)]
		except:
			debug_msg("2",-1)

	def remodelByteString(self,bstring,separators=[]):
		"""
			Hello, I remodel a byte string depending on 'separators' tuple list
			i turn "0000000000000000FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCC"
			into "0000 0000 - 0000 0000
			      FFFF FFFF - FFFF FFFF
			      AAAA AAAA - AAAA AAAA
			      BBBB BBBB - BBBB BBBB
			      ---------------------
			      CCCC CCCC - CCCC CCCC"
			using [("\n"+"-"*21+"\n",64),("\n",16),(" - ",8),(" ",4)]
		"""
		if separators == []:
			return bstring
		elem = separators[0]
		tab = []
		if len(separators) > 1:
			tab = separators[1:]
		result = ""
		chunks = self.splitChuncks(bstring,elem[1])
		lchunks = len(chunks)
		lchunksc = lchunks -1
		for i in range(lchunks):
			tmp = chunks[i]
			tmp = self.remodelByteString(tmp,tab)
			if i != lchunksc:
				tmp += elem[0]
			result += tmp
		return result

	def printFormatedByteString(self,bstring,multipicator=1):
		"""
			Hello, I remodel a byte string depending on 'separators' tuple list
			i turn "0000000000000000FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCC"
			into "0000 0000 - 0000 0000
			      FFFF FFFF - FFFF FFFF
			      AAAA AAAA - AAAA AAAA
			      BBBB BBBB - BBBB BBBB

			      CCCC CCCC - CCCC CCCC"
			depending on the 'multiplicator'
		"""
		format = [
			("\n\n",32*multipicator),
			("\n",8*multipicator),
			(" - ",4*multipicator),
			(" ",2*multipicator)
		]
		print self.remodelByteString(bstring,format)

	def printCleanedFormatedByteString(self,bstring,multipicator=1):
		"""
			Hello, I do printFormatedByteString but cleaned first
		"""
		self.printFormatedByteString(self.byteStringCleaner(bstring,"."),multipicator)
			
			
