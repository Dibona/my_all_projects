import os
from datetime import datetime
time = str(datetime.now())
x = input("commit name")


if x == "":
    x = time
command = f"git commit -m \"{x}\""
print(command)

os.system("git add .")
os.system(command)
os.system("git push -u origin master")

