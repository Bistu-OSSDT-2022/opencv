x = "hi"
print(x.upper())
X = "HI"
print(X.lower())
y = "hello"
print(y.replace("llo","art"))
z = " hello,world     "
print(z.strip())
p = "hello,world"
print(p.split(",w"))
age = 18
txt = "She is {}."
print(txt.format(age))#输出 She is 18.
a = 1
b = 2
c = 3
num = "{1}+{2}={0}"
print(num.format(c,b,a))#输出 2+1=3
sen = "I love {dish} most."
print(sen.format(dish = "tofu"))
txt = "we are \"family\""
print(txt)
print(bool(0))
print(bool(""))

x = 10
print(x,float)#输出 False
print(1+2)#加 输出3
print(4-2)#减 输出2
print(2*3)#乘 输出6
print(8/8)#除 输出2
print(5%3)#取余 输出2
print(3**2)#3的2次方 输出9
print(7//2)#整除 输出3
print(1==2)#相等 输出False
print(1!=2)#不相等 输出True
print(1>2)#大于 输出False
print(1<2)#小于 输出True

print(1<2 and 2<3)
print(1<2 or 2>3)
print(not(3>5))

x = y = "hhh"
print(x is y)#输出 True
print(x is not y)#输出 False

a = "hhh"
b = "hhh"
print(a is b)#输出 False

a = 4
print(~a)

list = ["a","b","c"]
#插入项目数量大于指定范围
list[1:2] = ["A","B"]
print(list)#输出 True
#插入项目数量小于指定范围
list = ["a","b","c"]
list[0:2] = ["A"]
print(list)#输出 False


list = ['a','b','c']
list.append('d')
print(list)


list1 = ['a','b','c']
list2 = ['e','f']
list1.extend(list2)
print(list1)

list = ['a', 'b', 'c', 'e', 'f']
list.remove('e')
print(list)#输出


list = ['a', 'b', 'c', 'f']
list.pop(1)
print(list)#输出
list.pop()
del list
print(list)
x = [1,2,3]
x.clear()
print(x)

list = ['a', 'b', 'c', 'e', 'f']
for x in list:
	print(x)

list = ['a', 'b', 'c', 'e', 'f']
count = range(len(list))
print(count)#输出 range(0,5)
for i in count:
	print(list[i])

list = ['a', 'b', 'c', 'd', 'e']
i = 0
while i < len(list):
	print(list[i])
	i += 1

list = ["cow","cat","bird","dog"]
newList = []
for x in list:
	if 'c' in x:
		newList.append(x)
print(newList)#输出

list = ["cow","cat","bird","dog"]
newList = [x for x in list if 'c' in x]
print(newList)#输出 ['cow', 'cat']

list = ['e','a','c','b','d','f']
list.sort()
print(list)#

list = [3,2,4,1,5]
list.sort()
print(list)

list = ['E','a','c','B','d','f']
list.sort()
print(list)#输出

list = ['e','a','c','b','d','f']
list.sort(reverse = True)
print(list)#['a', 'b', 'c', 'd', 'e', 'f']

list1 = [1,2,3]
list2 = [4,5]
for x in list2:
	list1.append(x)
print(list1)#输出 [1,2,3,4,5]


list1 = [1,2,3]
list2 = [4,5]
list1.extend(list2)
print(list1)#输出 [1,2,3,4,5]


'''x = ('a','b','c')
y = list(x)
y[1] = 'b'
x = tuple(y)
print(x)#输出 (1,4,3)
'''

x = ('a','b','c')
(x1,x2,x3) = x
print(x1)#输出 'a'
print(x2)#输出 'b'
print(x3)#输出 'c'
(x1,*x2) = x
print(x1)#输出
print(x2)#输出

(*x1,x2) = x
print(x1)#输出
print(x2)#输出

x = (1,2,3,4,5,6)
(x1,*x2,x3) = x
print(x1)#输出 1
print(x2)#输出 [2,3,4,5]
print(x3)#输出 6

x = ('a','b','c')
y = x*3
print(y)#输出


set1 = {1,2,3,4}
set2 = [6,-1]
set1.update(set2)
print(set1)#输出 {1,2,3,4,5}

set1 = {1,2,3,4,5}
set1.remove(5)
print(set1)#

set1 = {1,2,3,4,5}
set1.discard(6)
print(set1)

set1 = {1,2,3,4,5}
set1.pop()
print(set1)#输出 {1, 2, 3, 4}

set1 = {1,2,3,4,5}

print(set1.pop())#输出 1（返回删除的项）
print(set1)#输出 {2, 3, 4, 5}（pycharm运行结果）

set1 = {1,2,3}
set2 = {4,5}
set3 = set1.union(set2)
print(set1)#输出 {1,2,3,4,5}

set1 = {1,2,3}
set2 = {4,5}
set1.update(set2)
print(set1)#输出 {1,2,3,4,5}

dict = {
    "apple":4,
    "banana":6,
    "orange":3
}
print(dict)#输出

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":5
}
print(dict)#输出 {'apple': 4, 'banana': 6, 'orange': 3}
dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict)#输出 {'apple': 'red', 'banana': 6, 'orange': 3}
#新的"apple"键对应的值5会替换原来的"apple"键对应的4

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict["apple"])#输出 red
dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict.get("apple"))#输出 red

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict.keys())#输出 red

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict.values())#输出 dict_keys(['apple', 'banana', 'orange'])

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
print(dict.items())#输出 dict_values(['red', 6, 3])

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
if "apple" in dict:#in之后是字典名 而不是key列表（字典名.keys()）
    print("yes")

dict = {
		"apple": 4,
		"banana": 6,
		"orange": 3,
		"apple": "red"
	}
dict["apple"] = "green"
print(dict)  # 输出

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict2 = {"peach":5}
print(dict1.update({"orange":5}))#输出

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict2 = {"peach":5}
dict1.update(dict2)
print(dict1)#输出

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict2 = {"peach":5,"orange":5}
dict1.update(dict2)
print(dict1)#输出 {'apple': 'red', 'banana': 6, 'orange': 3, 'peach': 5}

dict = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict["peach"] = 5
print(dict)#

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict1.update({"peach":5})
print(dict1)#输出


dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict1.pop("apple")
print(dict1)#输出 {'banana': 6, 'orange': 3, 'peach': 5}

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict1.popitem()
print(dict1)#输出 {'banana': 6, 'orange': 3, 'peach': 5}

dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
for x,y in dict1.items():
    print(x,y)
'''
输出
red
6
3
'''
dict1 = {
    "apple":4,
    "banana":6,
    "orange":3,
    "apple":"red"
}
dict2 = dict1.copy()
print(dict2)#输出

if 1==2:
	print("1等于2")
elif 1<2:
	print("1小于2")
#输出 1小于2

if 1<2:
	print("yes")
#输出 yes

if 1==2:
	print("1等于2")
elif 1>2:
    print("1大于2")
else:
	print("1小于2")#输出 1小于2


x = 1
while x<4:
    print(x)
    x += 1
'''
输出
1
2
3
'''

x = 0
while x < 4:
    print(x)
    x += 1
    if x == 3:
    	break
'''
输出
0
1
2
3
'''

x = 0
while x < 4:
    x += 1
    if x == 3:
    	continue
    print(x)


'''    
输出
0
1
2
4
'''

x = 1
while x<4:
    print(x)
    x += 1
else:
    print("Finally finished.")
'''
输出
1
2
3
Finally finished.
'''
for x in range(5):
    print(x)
'''
输出
0
1
2
3
4
注意 最后输出的不是5
'''
for x in range(1,5):
	print(x)
'''
输出
1
2
3
4
最后输出的是结束数字-1
'''
for x in range(1,10,2):#2为每次增加的数
	print(x)
'''
输出
1
3
5
7
9
'''
try:
	print(A)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")#输出 The 'try except' is finished

try:
    x = 10
    print(x)
except:
	print("Something went wrong")#处理错误，返回一个语句
else:
    print("Nothing went wrong")
'''输出
10
Nothing went wrong
'''
'''
x = -1
if x < 0:
	raise Exception("Sorry, the number is out of range.")
#输出 Exception:Sorry, the number is out of range.
'''
def names(name):
    print("The name is "+name+".")
names("Jiang")#输出 Jiang
names("Lotus")#输出 Lotus


def my_function(name1, name2):
    print(name1 + " and " + name2 + " are good friends.")


my_function("Jiang", "Lotus")
# 输出
def my_function(*name):
	print(name[2]+" is sweetest.")
my_function("Lorry","Cherry","Jerry")
#输出

def my_function(name1,name2):
	print(name1+" and "+name2+" are good friends.")
my_function(name2 = "Jiang",name1 = "Lotus")
#输出 Jiang and Lotus are good friends.

def my_function(**item):
	print("The "+item["name"]+" is "+item["price"]+" yuan.")
my_function(name = "milk",price = "5")
#输出
def my_hometown(h = "Chinese"):
	print("I come from "+h)
my_hometown()
my_hometown("Norway")
def my_function(x):
    return x**2
print(my_function(3))
#输出 9

def my_function():
    pass


def my_function(x):
    if x > 0:
        y = x - my_function(x-1)
        return y
    else:
        return 0
print(x)
print(my_function(3))

x = lambda a,b,c:a * b * c
print(x(1,2,3))#输出 6

def cells(n):
    return lambda a : a * n
hh = cells(2)
print(hh)
print(hh(2))

x = lambda a,b,c : a * b * c
print(x(1,2,3))#输出 6

def my_function(a):
    return lambda b : a * b
myNumber = my_function(3)#参数a变成3
print(myNumber(4))#参数b变成4 输出 12

class MyClass:
    x = 5
myclass = MyClass()
print(myclass.x)#输出 5

class Student:
	def __init__(self, name, sex, year):
		self.name = name
		self.sex = sex
		self.year = year
s = Student("Mike","male",20)#初始化时 传入参数
print(s.name)#输出 Mike
print(s.sex)#输出 male
print(s.year)#输出 20

class Student:
#init前后是两个_
	def __init__(self, name, sex, year):
		self.name = name
		self.sex = sex
		self.year = year
	def hello(self):
            print("Hello, I am "+self.name+".")
s = Student("Mike","male",20)
s.hello()#输出 Hello, I am Mike.

class Student:
#init前后是两个_
    def __init__(self, name, sex, year):
	    self.name = name
	    self.sex = sex
	    self.year = year
    def hello(h):
    	 print("Hello, I am "+h.name+".")
s = Student("Mike","male",20)
del s.sex
s.hello()#输出 Hello, I am Mike.
print(s)
print(s)

class Person:
  def __init__(self,name):
  	self.name = name
  def printName(self):
  	print("The name is "+self.name+".")
class Student(Person):
  pass
s = Student("Mike")
s.printName()#输出 The name is Mike.

class Student(Person):
  def __init__(self,name, sex):
    super().__init__(name)
    self.sex = sex#增加sex属性
s = Student("Mike","male")
s.printName()

class Student(Person):
  def __init__(self,name, sex):
    super().__init__(name)
    self.sex = sex#增加sex属性
  def deleteName(self):
    print("delete "+self.name)
s = Student("Mike","male")
s.printName()#输出 The name is Mike.
s.deleteName()#输出 delete Mike

class Number:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myNumber = Number()
myIter = iter(myNumber)
print(next(myIter))
print(next(myIter))
print(next(myIter))

class Number:
    def __iter__(self):
        self.a = 1#初始化
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1#a递增
            return x#返回当前a
        else:
            raise StopIteration
myNumber = Number()
myIter = iter(myNumber)#调用iter()方法，传入迭代器myNumber
for x in myIter:
    print(x)
'''
输出
1
2
3
'''
f = open("hello.txt","a")
f.write("just have a walk.")
f.close()
f = open("hello.txt","r")
print(f.read())
f.close()

f = open("hello.txt","w")
f.write("hello")
f.close()
f = open("hello.txt","r")
print(f.read())
f.close()


import os
os.remove("美式霸凌.txt")
