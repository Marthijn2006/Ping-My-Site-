import os
from socket import *
import time
#	Welcome Screen:
print("Welcome user!" + " Get ip of a website")
#	Making option screen (Front - End)
print("""

:::::::::  ::::    ::::   ::::::::  
:+:    :+: +:+:+: :+:+:+ :+:    :+: 
+:+    +:+ +:+ +:+:+ +:+ +:+        
+#++:++#+  +#+  +:+  +#+ +#++:++#++ 
+#+        +#+       +#+        +#+ 
#+#        #+#       #+# #+#    #+# 
###        ###       ###  ########  
By : MAVIBE                                                                    
                                                                                                                                            
Make a choice: 

[0] Ping www.google.com
[1] Ping www.facebook.com
[2] Type youre own site
[3] HelpDesk
[4] Quit 

	""")
# 	Making the userinput 
userinput = int(input("Option : "))
#	Receiving the input
# 	Now making the if ... else() statement
if(userinput == 0):
	print("Pinging Google")
	hello = os.system("ping www.google.com")
	print(hello)

	


if(userinput == 1):
	print("Pinging Facebook")
	time.sleep(3)
	fb = os.system('ping facebook.com')
	print(fb)

if(userinput == 2):
	option = input("Typ your site here ! : ")
	time.sleep(3)
	var = os.system("ping " + option)
	print(var)

if(userinput == 3):
	print("""

 ██████   ██████   █████████   █████   █████ █████ ███████████  ██████████
░░██████ ██████   ███░░░░░███ ░░███   ░░███ ░░███ ░░███░░░░░███░░███░░░░░█
 ░███░█████░███  ░███    ░███  ░███    ░███  ░███  ░███    ░███ ░███  █ ░ 
 ░███░░███ ░███  ░███████████  ░███    ░███  ░███  ░██████████  ░██████   
 ░███ ░░░  ░███  ░███░░░░░███  ░░███   ███   ░███  ░███░░░░░███ ░███░░█   
 ░███      ░███  ░███    ░███   ░░░█████░    ░███  ░███    ░███ ░███ ░   █
 █████     █████ █████   █████    ░░███      █████ ███████████  ██████████
░░░░░     ░░░░░ ░░░░░   ░░░░░      ░░░      ░░░░░ ░░░░░░░░░░░  ░░░░░░░░░░ 
                                        
!! DISCLAIMER !!

ONLY USE THIS TOOL FOR EDUCATIONAL PURPOSES
DON'T HACK WITHOUT PERMISSION!

!! DISCLAIMER !!
This tool is created by : MAVIBE 

	Options :

[1] Ping Google

This options print automaticly the ip of google.com.
End the attack with:

[MacBook]:
Command + c or Control + c 
[Windows]
Control + c
[Linux]
Control + c


[2] Ping Facebook

This options print automaticly the ip of facebook.com.
End the attack with:

[MacBook]:
Command + c or Control + c 
[Windows]
Control + c
[Linux]
Control + c


[3] Ping youre site

This options print automaticly the ip of the prefered site.
End the attack with:

[MacBook]:
Command + c or Control + c 
[Windows]
Control + c
[Linux]
Control + c







		""")


if(userinput == 4):
	exit()




