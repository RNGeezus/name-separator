#! python3

import re, pyperclip

# Create a regex for names
nameRegex = re.compile(r'''
# Debra Clark,,,

(\w+)
\s
(\w+),,,       # Finds a full name

''', re.VERBOSE)

#Get a text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedName = nameRegex.findall(text)

#allPhoneNumbers = []
#for phoneNumber in extractedPhone:
#    allPhoneNumbers.append(phoneNumber[0])
#

# TODO: Copy separated names to clipboard
# Text format: FirstName,LastName,\n
results = ''
for name in extractedName:
    results = results + name[0] + ',' + name[1] + ',' + '\n\n'
    
pyperclip.copy(results)
