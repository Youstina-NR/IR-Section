import re
# ^ defines the start of the line
# Parenthesis defines a capturing group
# \d+ represents one or more digits
# $ defines the end of the line
pattern = r'^(\d+)$' 
test_string = '100'
result = re.match(pattern,test_string)
print(result)
if result:
    print('Match success')
else:
    print('No match')



# ^      start of the string
# $      the end
# .      any character except a newline
# *      0 or more
# ?      0 or one
# .*?    anything after that
# \(     opening parenthesis
# (\d+)  one or more digits
# \)     closing parenthesis
# {m}    exactly m copies of the previous RE should be matched
#        re.match( r'(\w\d){2}', 'a1b2') 
# {m,n}  match from m to n repetitions of the preceding RE
print(re.match( r'a{4,}b', 'aaaaab')) 
# {m,n}?  attempting to match as few repetitions as possible.
print(re.match( r'a{3,}?', 'aaaaa')) 
print(re.match( r'a{3,5}', 'aaaaaaa')) 
print(re.match(r'(\d+)','aaa3421'))
print(re.search(r'(\d+)','aaa3421'))
# []     Used to indicate a set of characters.
#        [a-zA-Z0-9] 
#        [^5] will match any character except '5'
# '|'    or - A|B, where A and B can be arbitrary REs
# \d     [0-9] 
# \D     [^0-9]
# \w     [a-zA-Z0-9_]
# \W     [^a-zA-Z0-9_]
print(re.match( r'^[^591]+', '2344445678b'))


f = open("Lab6/sample.txt", "r")

pattern = r'\((\d+)\)'

# pass in the pattern and the file content to findall
s = str(f.read())
result = re.findall(pattern, s) 
print(result)
# ['4', '345', '14', '6']

print(re.findall( r'^\((\d+)\)', s) )
# []

print(re.findall( r'\((\d+)\)$', s) )
# []

print(re.findall( r'^.*?\((\d+)\)', s) )
# ['4']

text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly", text))
# ['carefully', 'quickly']