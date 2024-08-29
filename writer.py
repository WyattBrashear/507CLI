import filetools
def writer():
  print("Welcome to writer")
  print("Would you like to create a new file or open an existing file?")
  print("1. Create")
  print("2. Open")
  cmd = input()
  filename = input("Enter File Name: ")
  if cmd == "1":
      # Example usage
    filetools.write_to_file(filename)
  if cmd == "2":
    filetools.read_from_file(filename)