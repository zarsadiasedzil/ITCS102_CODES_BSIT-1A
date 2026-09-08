# getpass
#conditional statement/control structures/ selection statement

import getpass
username = "Wow"
password = "Mamamoblue"
u = input("enter username -->")
p = getpass.getpass("enter password -->")

if username == u and password == p:
	print("Access Granted")
else:
	print("Access Denied")