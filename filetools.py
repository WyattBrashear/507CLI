import os

def write_to_file(filename):
  """Writes the user-entered text to the specified file.

  Args:
      filename (str): The name of the file to write to.

  Returns:
      None
  """

  text = input("Enter file contents: ")

  # Open the file in write mode ('w')
  with open(filename, 'w') as file:
    # Write the text to the file using the write() method
    file.write(text)
    print(f"Successfully wrote to file: {filename}")  # Informative message

def read_from_file(filename):
  """Reads the contents of the specified file and prints them.

  Args:
      filename (str): The name of the file to read from.

  Returns:
      None
  """

  # Open the file in read mode ('r')
  with open(filename, 'r') as file:
    # Read the entire file content as a string
    contents = file.read()
    print(f"Contents of {filename}:")
    print(contents)

def write_to_filed(filename, contents):
  """Writes the user-entered text to the specified file.

  Args:
      filename (str): The name of the file to write to.

  Returns:
      None
  """

  text = contents

  # Open the file in write mode ('w')
  with open(filename, 'w') as file:
    # Write the text to the file using the write() method
    file.write(text)
    print(f"Successfully wrote to file: {filename}")  # Informative message