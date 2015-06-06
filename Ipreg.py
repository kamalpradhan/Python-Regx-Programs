import re;
t = int(input());
for x in range(0,t):
    element = input();
    m = re.match("^[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}", element);
    if m:
       print("true");
    else:
       print("false");
    

