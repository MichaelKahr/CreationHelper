from github import Github
import getpass
import os
import subprocess

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


os.system("cd exercisefolder && git clone https://github.com/"+username+"/"+name+".git")
cmd = "hyper exercisefolder"+name+"/"
subprocess.Popen(cmd, shell=True)
