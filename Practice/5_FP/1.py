lst = [3,4.0,'a',5,5.0,'b',['a','c']]

listlst = list(filter(lambda x: isinstance(x,list),lst))

print(listlst) # result is [['a','c']]