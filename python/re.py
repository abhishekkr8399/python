import re
#txt="aaaaabbbbb"
#txt="Today's date is 103-09-2019"
txt="My landline number is 08255-269315"
#x=re.search("a*",txt)
#x=re.search("b*",txt)
#x=re.search("ac*?",txt)
#x=re.search("[0-9]{2}-[0-9]{2}-[0-9]{4}",txt)   this matches 103-09-2019 also
x=re.search("[0-9]{5}-[0-9]{6}$",txt)
if(x):
    print("Match found.")
else:
    print("No match found.")
