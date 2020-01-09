import re
pattern = re.compile(r'([a-zA-Z]).([a])')
string = 'search inside of this text please!'
print('search' in string)
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group())