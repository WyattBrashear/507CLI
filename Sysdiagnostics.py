import Grapher
import os
import sys
import time
import random
import filetools

def startdiagnostics():
  print("Starting 507 Diagnostics suite")
  time.sleep(3)
  print("Welcome to the 507 Diagnostics suite! Please select an option from the list below:")
  print("1. Screentest")
  print("2. Terminaltest")
  cmd = input()
  if cmd == "1":
    print("Starting screentest")
    Grapher.drawtest()
    print("Screen test complete.")
  if cmd == "2":
    for i in range(100000):
      print(random.random())
    print("Termiant test complete.")