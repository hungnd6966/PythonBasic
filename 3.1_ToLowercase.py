#Write a Python class which has two methods set_String and print_String.
#set_String accept a string from the user and print_String print the string in upper case.

class ToLowerCase:
  def __init__(self, input_string="hello world"):
    self.input_string = input_String

  def set_String(self, inputString):  #this is setter
    self.input_string = inputString

  def print_String(self):
    return self.input_string.lower()
#  return self.input_string.upper()


if __name__ == "__main__":
  input_String = input("Please key in your string: ") #variable and function use snake_to_case
  toLowerCaseString = ToLowerCase() #instance use camelCase
  toLowerCaseString.set_String(input_String)
  print(toLowerCaseString.print_String())
