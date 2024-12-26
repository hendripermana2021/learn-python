import re

txt = "The rainasd asdasfasd as dasd in Spain"
x = re.search("^The.*Spain$", txt)

if x :
    print("Yes, the string starts with 'The' and ends with 'Spain'")
else :
    print("No, the string does not start with 'The' or ends with 'Spain'")
