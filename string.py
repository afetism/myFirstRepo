#sual1
str="Hello programmers"
print(str.replace("p","P"))
#sual2
s = "qwertyuiqwopzercdscgnvxbhgmjlma"
new_string=""
for i in range(len(s)):
    b = s[i]
    a = s.count(b)
    if (a > 1):
        if b not in new_string:
            print(b)
            new_string += b
#sual3
string="  Hello World  "
print(string.strip())
#sual4
course = "Our course is best in the World, STEP IT ACADEMY Azerbaijan"
print(course.lower())
#sual5
website = "http://www.google.com"
if(website.startswith("www") and website.endswith("com")):
    print(True)
else:
    print(False)

