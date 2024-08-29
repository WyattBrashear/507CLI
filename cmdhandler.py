import appdirectory

def runcmd(cmd):
  if cmd == "calc":
    appdirectory.execute(1)
  if cmd == "help":
    print("calc - Runs the calculator")
    print("help - Shows this menu")
    print("clear - Clears the screen")
    print("screentest - Runs the screentest")
  if cmd == "clear":
    for x in range(100):
      print("")
    
  if cmd == "diagnostics":
     appdirectory.execute(2)
  if cmd == "writer":
     appdirectory.execute(3)
  else:
    print()