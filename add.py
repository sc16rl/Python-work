### 一行代码实现1加到100
print(sum([i for i in range(101)]))

t = ['t','t','t']

cc = "||".join(t)
print(cc)

### 把1到100的整数里，能被2，3，5同时整除的数区取出来
array = [str(i) for i in range(1,101) if i%3 ==0 and i%2 ==0 and i%5 == 0]
print(";".join(array))

### Score
score=[['张三', 89, 78, 91], ['李四', 99, 87], ['王五', 49, 55, 78]]

x = sorted([[i[0],sum(i[1:])/3] for i in score if len(i) == 4], key=lambda i:i[1], reverse=True)

print(x)