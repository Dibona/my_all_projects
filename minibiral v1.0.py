import os
file_name = input("Folder name: ")
f = int(input("folder number: "))
for i in range(f):
	os.system(f"mkdir {file_name}{i}")
z = input("delete folder ?/: ")

if z == "yes":
	for i in range(f):
		os.system(f"rmdir {file_name}{i}")
else:
	print("Thanks for using my program")

print("mew")	
	
