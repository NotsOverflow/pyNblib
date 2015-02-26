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

import nblib

def hello():
	test_bytestr = [
		"\xDE\xAD\xBE\xEF",
		"\x00\x01\x02\x03",
		"abcdef",
		"0123456789",
		"#sdvbsbv"
	]
	test_ishex = [
		"abcdef",
		"ABcd0125",
		"14251",
		"\x00",
		"\x00\xA2",
		"abA8@"
	]

	test_remodel = [ 
		(
			"000011112222333344445555666677770000000000000000FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCC",
			[("\n"+"-"*21+"\n",64),("\n",16),(" - ",8),(" ",4)]
		)
	]

	nbl = nblib.Instance()
	for test in test_bytestr:
		print "testing -> %s" % test
		print "result  -> %s\n" % nbl.b2h(test)
	for test in test_ishex:
		print "testing -> %s" % test
		print "result  -> %s \n" % nbl.iah(test)
	for test in test_remodel:
		print "testing  : \n%s" % test[0]
		print "result : \n%s\n" % nbl.rb(test[0],test[1])
	tmp = "".join(test_bytestr) + "".join(test_ishex) + test_remodel[0][0]
	print "testing :\n%s" % tmp
	print "result :"
	nbl.pcfb(tmp,4)


if __name__ == "__main__":

	hello()
