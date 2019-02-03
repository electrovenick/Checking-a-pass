special = '`!@#$%^&*+.-\=0|_/?'
l = s = True
p = 0
print("Enter a password")
password = (input())
if(len(password) < 5 or len(password) > 10):
    print("Error! Length [5; 10]")
    l = False
if((' ') in (password)):
    print("Error! Symbol ' ' in unacceptable")
    s = False
for i in password:
    if i in special:
        p = p + 1
if (p == 0):
    print("Enter a special symbol")
if(l == True and s == True and p > 0):
    print("True password")