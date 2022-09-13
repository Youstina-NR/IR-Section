#Tuples
#A tuple is a collection which is unchangeable
#Tuples can be thought of as read-only lists
t1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (t1)           # Prints complete tuple
print (t1[0])        # Prints first element of the tuple
print (t1[-1])       # Prints last element of the tuple
print (t1[1:3])      # Prints elements starting from 2nd till 3rd 
print (t1[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (t1 + tinytuple) # Prints concatenated tuple
#tuple[0] = 222         #error

for x in t1:
  print(x)
  
print(len(t1))

for x in (1,2,3) :
    print (x)
for x in (1,2,3) :
    print (x, end = ' ')
print()

tup1 = ()
#To write a tuple containing a single value you have to include a comma, even though there is only one value −
tup1 = (50,)
print(tup1)
print(type(tup1))

t = (50)
print(type(t)) #int


tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

del tup1
#print(tup1) #error

#tuple() Constructor
thistuple = tuple((1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
print(thistuple)
x = thistuple.count(5)
print(x)
x = thistuple.index(8)
print(x)
x=min(thistuple)
print(x)
print(max(thistuple))
print(sum(thistuple))

print('-'*50)
########################################################
#Sets
#A set is a collection which is unordered and unindexed
thisset = { "banana", "apple", "cherry"}
print(thisset)
for x in thisset:
  print(x)

print("banana" in thisset)

#print(thisset[0])  #error

thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "grapes","banana"])
print(thisset)

print(len(thisset))

thisset.remove("banana")
#If the item to remove does not exist, remove() will raise an error.
print(thisset)

thisset.discard("banana")
#If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

#The clear() method empties the set:
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
del thisset
#print(thisset)  #error

#set() Constructor
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

print('-'*50)
########################################################
#Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict)
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


dict = {"b":1.2,"a":3.5,"c":4}

for x in dict:
  print(x)

for x in dict:
  print(dict[x])

for x in dict:
  print(x,' : ',dict[x])

for x, y in dict.items():
  print(x," : " ,y)


print('-'*50)
########################################################
#Files I/O
##############################################################
#access_mode:
#r    Opens a file for reading only.
#     The file pointer is placed at the beginning of the file.
#     This is the default mode.
#rb   Opens a file for reading only in binary format.
#     The file pointer is placed at the beginning of the file.
#r+   Opens a file for both reading and writing.
#     The file pointer placed at the beginning of the file.
#rb+  Opens a file for both reading and writing in binary format.
#     The file pointer placed at the beginning of the file.
#w    Opens a file for writing only.
#     Overwrites the file if the file exists.
#     If the file does not exist, creates a new file for writing.
#wb   Opens a file for writing only in binary format.
#     Overwrites the file if the file exists.
#     If the file does not exist, creates a new file for writing.
#w+   Opens a file for both writing and reading.
#     Overwrites the existing file if the file exists.
#     If the file does not exist, creates a new file for reading and writing.
#wb+  Opens a file for both writing and reading in binary format.
#     Overwrites the existing file if the file exists.
#     If the file does not exist, creates a new file for reading and writing.
#a    Opens a file for appending.
#     The file pointer is at the end of the file if the file exists.
#     That is, the file is in the append mode.
#     If the file does not exist, it creates a new file for writing.
#ab   Opens a file for appending in binary format.
#     The file pointer is at the end of the file if the file exists.
#     That is, the file is in the append mode.
#     If the file does not exist, it creates a new file for writing.
#a+   Opens a file for both appending and reading.
#     The file pointer is at the end of the file if the file exists.
#     The file opens in the append mode.
#     If the file does not exist, it creates a new file for reading and writing.
#ab+  Opens a file for both appending and reading in binary format.
#     The file pointer is at the end of the file if the file exists.
#     The file opens in the append mode.
#     If the file does not exist, it creates a new file for reading and writing.
#########################################################################
#write
f = open("file1.txt", "w")
print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)
f.write("Python is a great language.\nYeah its great!!\n")
f.close()

#read
f = open("file1.txt", "r+")
str = f.read(10)
print ("Read String is : ", str)
line = f.readline()
print ("Read Line: %s" % (line))
s =  f.readlines()
print(s)
f.close()
#########################################################################
#File Positions
#The tell() method tells you the current position within the file;
#in other words, the next read or write will occur at that many bytes
#from the beginning of the file.
#
#The seek(offset[, from]) method changes the current file position.
#The offset argument indicates the number of bytes to be moved.
#The from argument specifies the reference position from where
#the bytes are to be moved.
#The position is computed from adding offset to a reference point;
#the reference point is selected by the from_what argument.
# 0 (default)measures from the beginning of the file,
# 1 uses the current file position,
# 2 uses the end of the file as the reference point.
#


# Open a file
f = open("file1.txt", "r+")
str = f.read(10)
print ("Read String is : ", str)

# Check current position
position = f.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = f.seek(0, 0)
str = f.read(10)
print ("Again read String is : ", str)

# position = f.seek(-10,2)  # error 
# position = f.seek(3,1)    #error
# use rb mode 

str = f.readlines() #This reads the remaining lines from the file object and returns them as a list.

# Close opened file
f.close()
######################################################################
# Renaming and Deleting Files

import os

# Rename a file from test1.txt to test2.txt
os.rename( "file1.txt", "test.txt" )
# Delete file test2.txt
os.remove("test.txt")

#create a directory test in the current directory 
os.mkdir("test")
# remove a directory
os.rmdir('test')
#display the current working directory
print(os.getcwd())
#change the current directory
os.chdir("E:/Sections/")
print(os.getcwd())
#Moving up one directory
os.chdir("..")
# or
# os.chdir(os.path.pardir)
print(os.getcwd())

print(os.listdir(r'E:\Sections'))

#######################################################################


