array = [1,2,3,4,5,6,7,8,9]

x = [i**2 for i in array if i != 0]

# print(array[3:-1])

sum= lambda a,b,c:a+b+c

# print(sum(1,2,3))

score = [['san',89,78,91],['li',99,87],['wang',111,112,78],['luo',37,28,38]]

x = sorted([ [i[0], sum(i[1],i[2],i[3])/3] for i in score if len(i)==4],key=lambda x: x[1],reverse=True)

print(x)

