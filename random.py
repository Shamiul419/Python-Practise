import re
messageValue = 'sas s fg gsafd dsa dgr gbob dad i gona love for ever plz call me 123-456-7890 '
findValue = re.compile(r'\d\d\d\-\d\d\d\-\d\d\d\d')
print(findValue.search(messageValue).group())
#or
#mo = findValue.search(messageValue)
#print(mo.group())