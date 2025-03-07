def reversee(a):
    if len(a)<=0:
        return ''
    b = a.split()  
    c = ["".join(i[::-1]) for i in b]  
    
    return " ".join(c)  

a = "Hello           World         Python"
print(reversee(a))  






# def reversee(a):
#     if len(a)<=0:
#         return ''
#     c = []
#     b = a.split(' ')
#     for i in range(len(b)):
#         c.append(b[i][::-1])
#     return " ".join(c)
# a = "Hello          World        Python"
# print(reversee(a))