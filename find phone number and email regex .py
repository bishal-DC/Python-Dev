#To do import modules

##This code can find telephone number and email address from a giant document 
##Please refer this website for this documents https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf

import pyperclip
import re

#Phone number identification regex
#863-583-8107
#863-583-8107,#(863) 583-8107,583-8107, ext.12345 ,x12345

phonenumberregex=re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? # first part is optional checking something like 546 or (546)
(\s|-) # checking second separator or white space 
\d\d\d[-] # checking second set of three digits and second separator
\d\d\d\d # Last set of 4 digit
(ext(\.)\s | x(\d{2,5}))? # extension which is optional
)# this set of parenthesis to group this whole search result
''',re.VERBOSE)

#sshepherd61@sbcglobal.net

emailregex=re.compile(r'''
[a-zA-Z0-9.+*_?#%]+#name part 
[@]# @b part
[a-zA-Z0-9.+_]+#domain name 
''',re.VERBOSE)

#phonenumbertstregex=re.compile(r'\d\d\d')

#text='sshepherd61@sbcglobal.net'
text=pyperclip.paste()

phonenumber=phonenumberregex.findall(text)

phonenumberlist=[]

for extact in phonenumber:
    phonenumberlist.append(extact[0])

#phonenumbertest=phonenumbertstregex.findall(text)

#print(phonenumbertest)

#print(phonenumberlist)

emailnumber=emailregex.findall(text)

#print(emailnumber)
results='\n'.join(phonenumberlist) +'\n' + '\n'.join(emailnumber)

pyperclip.copy(results)




