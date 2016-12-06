#! /usr/bin/python3
# Initer - A script to initialise new projects

import sys, os, subprocess, time, requests, github
from github import Github

# TODO: Accept Project name and create new folder

projectName = sys.argv[1]
githubUserName = sys.argv[2]
token = str(sys.argv[3])

if not os.path.exists(projectName):
    os.makedirs(projectName)
else:
	print('That directory name already exists')
	sys.exit()

# TODO: Change directory into new folder

os.chdir(projectName)

# TODO: Create new file within folder

projectFile = open( '{}.py'.format(projectName), 'w+')
projectFile.write("#! /usr/bin/python3 \n")
projectFile.write("# {} - \n".format(projectName))
projectFile.close()

# TODO: Create README.md

readme = open('README.md', 'w+')
readme.write('Project name: {} \n'.format(projectName))
readme.close()

# TODO: Run git init
print(os.getcwd())
subprocess.Popen(['git', 'init'], stdout=subprocess.PIPE)
time.sleep(1)
subprocess.Popen(['git', 'add', '.'], stdout=subprocess.PIPE)
subprocess.Popen(['git', 'commit', '-m','"Initial commit"'], stdout=subprocess.PIPE)
data = '{"name":"' + projectName + '"}'
print(data, token, githubUserName)
createRepo = requests.post('https://api.github.com/user/repos', data=data, auth=(githubUserName, token))
createRepo.raise_for_status()

# git remote add origin git@github.com:GaryLomberg/Dsdas.git
# git push -u origin master

