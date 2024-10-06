l1=["aaa","sasda","svvs","aada","as","s","f","adafa","try"]
l2=[]
count=0
for c in l1:
    if len(c)>=2:
       if c[0]==c[-1]:
          l2.append(c)
          count=count+1
print("New list is:",12)
print("Total Count is:",count)


