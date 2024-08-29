import os
from cmdhandler import runcmd

print("Welcome to the 507 CLI Running on", os.name, "if you have any questions please type help")
print()
while True:
  cmd = input()
  runcmd(cmd)