# File Handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''


# Open a File on the Server
f = open("test.txt")
print(f.read())

f = open("test.txt")
print(f.read(5))  #read some part of file


f = open("test.txt", "r")
print(f.readline())

f = open("test.txt", "r")
for x in f:
  print(x)


# Close the file when you are finished 

f = open("test.txt", "r")
print(f.readline())
f.close()

# File Write
f = open("test.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Delete a File
import os
os.remove("test.txt")



# Check if file exists, then delete it:

import os
if os.path.exists("test.txt"):
  os.remove("test.txt")
else:
  print("The file does not exist")


