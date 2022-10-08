#INFO 
# 1. GET the text off the clipboard.
# 2. Find all the phone number in the text.
# Paste them onto the clip board.
 # q. How this will work?
 # 1. use pyperclip module to copy and paste string.
 # 2. Create two regex, one for matching number and other for e-mail address
 # 3. Find all the matches not just one , of both regex.
 # 4. Neatly format the matched string into a single string to paste.
 # 5. Display some kind of message if no match are found. 

import re, pyperclip
comRegex = re.compile(r'''(
(\d{3}|\(d{3}\))?            # area code
(\s|-|\.)?                   # seperator
\d{3}                        # First 3 Digit    
(\s|-|\.)?                   # Seperator
\d{4}                        # last four digit
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''',re.VERBOSE|re.I | re.DOTALL)
# Regex for email address
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]        #username
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find match in clipboard 
text = str(pyperclip.paste())
matches = []
for groups in comRegex.findall(text):
    phoneNum = ''.join(groups[0])
    if groups[5] != ' ':
        phoneNum += ' x' + groups[5]  
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy result to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('coppied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email address found.')
