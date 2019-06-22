#!usr/bin/python

import urllib

def banner():
	print """
 _____       _            _____                                 
|  __ \     | |          / ____|                                
| |__) |___ | |__  ___  | (___   ___ __ _ _ __  _ __   ___ _ __ 
|  _  // _ \| '_ \/ __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| | \ \ (_) | |_) \__ \  ____) | (_| (_| | | | | | | |  __/ |   
|_|  \_\___/|_.__/|___/ |_____/ \___\__,_|_| |_|_| |_|\___|_|  \n"""
	print "       [X] http://www.explosionsquadcyber.id [X]"
	print "           [X] Coded By Nelo.F4 ~ D3N15 [X] "
	print "           [X] Tools Robots.txt Scanner [X] "

def scan():
	target = raw_input("Enter Your Target : ")
	if not target.startswith("http://"):
		target = "http://"+target
	scanrobot = target+"/robots.txt"
	robots = urllib.urlopen(scanrobot)
	if robots.getcode() == 200:
		html = "<head>"
		baca = robots.read()
		if html in baca:
			print "[X] Argh Robots.txt Not Found!"
		else:
			print "[!] Detected!: ",baca
	else:
		print "[X] Argh Not Found!"
def main():
	banner()
	scan()

main()