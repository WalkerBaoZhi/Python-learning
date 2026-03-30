s=input()
p=input()

temp=s[0:len(p)]
if p!=temp:
    print ("该字符串不以",p,"开头。",sep='')
else:
    print ("该字符串以",p,"开头。",sep='')