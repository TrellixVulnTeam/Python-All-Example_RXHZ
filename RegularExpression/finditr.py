import re 
itr=re.finditer("[a-z]","a7b9c5kz")
for m in itr:
    print(m.start(),"...",m.end(),"...",m.group())
    