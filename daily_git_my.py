import os
import datetime
import time

def gitcmd(cmd):
    os.system(cmd)


now = datetime.datetime.now()

default_msg = "{} 강의".format(now.strftime('%Y-%m-%d'))


input_msg = input("Default Message?? (Yes: Enter or input message) > ")
    
if input_msg !='':
    commit_msg = input_msg
else:
    commit_msg = default_msg

print("commit...", commit_msg)

gitcmd("git add --all")
gitcmd('git commit -am "{}"'.format(commit_msg))
gitcmd("git push -fu origin master")

print("깃에 올라갔습니다")

time.sleep(5)