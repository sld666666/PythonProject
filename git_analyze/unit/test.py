import time
import platform
import sys
import subprocess
import os
import re
import signal



test_path = "/Users/luodongshen/Documents/program/document"

cmd = "git shortlog -s -n"
out = open("stdout.txt","wb")
p = subprocess.Popen(cmd, shell = True, cwd=test_path, stdout=subprocess.PIPE)
p.wait()
output = p.stdout.read()
print("done:"+ str(output))

