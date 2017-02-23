#!usr/bin/env python

import urllib, sys

print "Please enter your link and the filename:"

#user input
user_input = sys.stdin.read().strip().split()

#error checking
if len(user_input) < 2:
   print "Error, please seperate by space."
   sys.exit()

#sys split
url = user_input[0]
filename = user_input[1]
 
#image downlaoder
urllib.urlretrieve(url, "/home/cian/Downloads/" + filename)
