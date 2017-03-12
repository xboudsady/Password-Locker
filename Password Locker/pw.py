#! /usr/bin/env python3
# pw.py - An insecure password locker program
# To use the program, use 'python3 pw.py email' for email

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
			 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
			 'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]	# first command line arg is the account

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account name ' + account)