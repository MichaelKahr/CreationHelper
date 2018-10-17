from github import Github
import getpass
import os
import subprocess
"""
username = input("Please enter your username: ")
try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    pass
"""
name = input("Enter the name of the repo that you want to create: ")
g = Github("")
user = g.get_user()
username = "MichaelKahr"
repo = user.create_repo(name,auto_init=True)
yn = input("Do you want to add an collaborator?: ")

if yn =="y":
    num = int(input("How many would you like to add:"))
    for x in range(num):
        collab = input("Please enter the Name of the collaborator: ")
        repo.add_to_collaborators(collaborator=collab, permission='admin')
    print("Everybody added!")
else:
    print("Ok, no one added!")


os.system("cd /Users/mikeykahr/Desktop/Privat/SCHULE/POS/3.Klasse/Exercises && git clone https://github.com/"+username+"/"+name+".git")
cmd = "hyper /Users/mikeykahr/Desktop/Privat/SCHULE/POS/3.Klasse/Exercises/"+name+"/"
subprocess.Popen(cmd, shell=True)