s=input()
a=eval(input())
l=[]
for i in a:
    if i.startswith(s):
       l.append(i)
    
    
print(l)
