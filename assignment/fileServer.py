"""
	According to https://www.binarytides.com/python-socket-server-code-example/

	Steps to creating a server:
	1. Create socket with socket.socket function
	2. Bind socket to address+port with socket.bind function
	3. Put the socket in listening mode with socket.listen function
	4. Accept connection with socket.accept function
"""

import sys

sys.path.append("../lib")

import re, socket, params

sys.path.append("../lib")

import sys, re, socket, params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket

# Binding to local host # and paramMap['listenPort']
bindAddr = ("127.0.0.1", listenPort)
try:
	listeningSock.bind(bindAddr)
except socket.error as msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + 'Message: ' + msg[1]
	sys.exit(1) # exit with failure code

listeningSock.listen(4) # allow only one outstanding request
print("listening on:", bindAddr)