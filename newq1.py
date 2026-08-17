

def simple_interest(principal,rate=5,time=1):
    sim=(principal * rate * time)/100
    return sim
print(simple_interest(1000))
print(simple_interest(1000,8))
print(simple_interest(1000,8,3))



add1=lambda x,y : x+y
print(add1(10,20))

def add(x,y):
    return x+y
print(add(10,20))

sq=lambda x:x**2
print(sq(6))
print(sq(8))

cube=lambda x:x**3
print(cube(4))

gre=lambda x,y:x if x>y else y
print(gre(9,6))

even=lambda x:x%2==0
print(even(7))

l=[3,7,8,27,32,12,19,4]
l.sort(key=lambda x: x)#x:x/2 can also be used
print(l)

l=[3,7,8,27,32,12,19,4]#based on remainder this get sorted
l.sort(key=lambda x: -x)
print(l)

simple_interest = lambda p, r, t: (p * r * t) / 100
print(simple_interest(10000, 5, 2))

celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(25))


electricity_bill = lambda units: units * 5 if units <= 100 else units * 8
print(electricity_bill(80))
print(electricity_bill(150))

login = lambda username, password: "Login Success" if username == "admin" and password == "1234" else "Invalid"
print(login("admin", "1234"))
print(login("user","1234"))

#q1
l=[1,2,3,4]
p=list(map(lambda x:x**2,l))
def square(x):
    return x**2
print(p)
x=list(map(square,l))

l1=[1,2,3,4]
l2=[5,6,7,8]
p=list(map(lambda x,y:x+y,l1,l2))
print(p)


l1=[1,2,3,4]
p=list(map(lambda x:x//2,l1))
print(p)

def iseven(x):
    if x%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5]
l1=list(filter(iseven,l))
print(l1)



p = [100, 250, 500, 750]
updated_prices = list(map(lambda p: p + p * 0.10, p))
print(updated_prices)

usernames=['alice','bob','swetha','bindu']
updated_names=list(map(lambda x: x.capitalize(),usernames))
print(updated_names)

p = [200, 450, 600, 1200, 350]
expensive_products = list(filter(lambda p: p > 500, list(map(lambda x:x+x*0.10,p))))
print(expensive_products)

usernames=['alice','bob','swetha','bindu']
length=list(map(lambda x: len(x),usernames))
print(length)

l=[1,2,3,4,5]
mulby=list(map(lambda x:x*5,l))
print(mulby)


numbers = [25, 45, 60, 75, 30, 90, 50]
result = list(filter(lambda x: x > 50, numbers))
print(result)

numbers = [4, 7, 8, 10, 12, 15, 16, 21]
result = list(filter(lambda x: x % 4 == 0, numbers))
print(result)

num=[24,7,9,8,46,30,178]
result=list(filter(lambda x:x%4==0,list(map(lambda x:x**2,l1))))
print(result)

num=[2,3,4,5,6,7,8]
mulby=list(map(lambda x:x*3,list(filter(lambda x:x%2==0,num))))
print(mulby)

num=[34,2,4,5,6,8,1,4]
sq=list(map(lambda x:x**2,list(filter(lambda x:x>20,num))))
print(sq)

words = ['apple', 'cat', 'banana', 'dog', 'orange']
gre=list(map(lambda x: x.upper(), list(filter(lambda x: len(x) > 4, words))))
print(gre)

n=[2,25,35,55,65,16,105]
print(list(map(lambda x:x+10,list(filter(lambda x:x%5==0,n)))))

marks=[38,48,86,68,91]
print(list(map(lambda x:x+5,list(filter(lambda x:x>40,marks)))))

from functools import reduce
l=[2,4,6,68,34]
print(reduce(lambda x,y:x+y,l))

from functools import reduce
words = ["Python", " ", "is", " ", "easy"]
result = reduce(lambda x, y: x + y, words)
print(result)

from functools import reduce
digits = [1, 2, 3, 4]
num = reduce(lambda x, y: x * 10 + y, digits)
print(num)

from functools import reduce
nums = [50, 10, 5, 2]
diff = reduce(lambda x, y: x - y, nums)
print(diff)

from functools import reduce
marks = [85, 90, 78, 92, 80]
total = reduce(lambda x, y: x + y, marks)
average = total / len(marks)
print("To+tal =", total)
print("Average =", average)

students=[{'name':'alice','score':85},{'name':'bob','score':79},{'name':'chandrika','score':97}]
l=sorted(students,key=lambda x:x['score'])
print(l)

students=['chandu','raji','sunitha','vibhav']
l=sorted(students,key=lambda x:len(x))
print(l)

from functools import reduce
num=[1,2,3,4,5]
prod=reduce(lambda x,y:x*y,num)
print(prod)

names=[('chandu',24),('sunitha',21),('chandrika',22)]

num=[3,7,8,4,12]
l=list(map(lambda x:x**2,filter(lambda x:x%2==1,num)))
print(l)


from functools import reduce
prices=[607,298,563,290,940]
final_bill=list(map(lambda x:x+0.10,filter(lambda x:x>500,prices)))
print(reduce(lambda x,y:x+y,final_bill))

from functools import reduce
num=[-5, 8, -10, 15, -20]
l=list(map(lambda x:abs(x),filter(lambda x:x<0,num)))
con=reduce(lambda x,y:x+y,l)
print(con)

num=[34,54,67,15,8,6]
l=list(map(lambda x:x*3,filter(lambda x:x>50,num)))
maxi=reduce(lambda x,y:x if x>y else y,l)
print(maxi)

words=["cat","dog","snake","fish"]
l=list(map(lambda x:x.upper(),filter(lambda x:len(x)>3,words)))
con=reduce(lambda x,y:x+" "+y,l)
print(con)
++hjvb
salaries=[25000,30000,89000,73000]
inc=list(map(lambda x:x*1.15,filter(lambda x:x>30000,salaries)))
exp=reduce(lambda x,y:x+y,inc)
print(exp)

num=[2,6,74,83,99,17,35]
odd=list(map(lambda x:x**2,filter(lambda x:x%2!=0,num)))
sum=reduce(lambda x,y:x+y,odd)
print(sum)

prices=[266,374,835,347,843,335,221]
dis=list(map(lambda x:x*0.9,filter(lambda x:x>500,prices)))
tot=reduce(lambda x,y:x+y,dis)
print(tot)

amt=[2478,3330,5000,640000]
bank=list(map(lambda x:x+10,filter(lambda x:x>0,amt)))
sum=reduce(lambda x,y:x+y,bank)
print(sum)


def my_map(func, lst):
    res=[]
    for i in lst:
        x=func(i)
        result.append(x)
        print(x)
def square(x):
    return x**2
l=[2,4,6,8]
print(my_map(square,l))

def calculator(*args, operation="add", **options):

    if operation == "add":
        result = 0
        for i in args:
            if options.get("show_steps"):
                print(result, "+", i, "=", result + i)
            result += i

    elif operation == "multiply":
        result = 1
        for i in args:
            if options.get("show_steps"):
                print(result, "*", i, "=", result * i)
            result *= i

    elif operation == "max":
        result = args[0]
        for i in args:
            if i > result:
                result = i

    elif operation == "min":
        result = args[0]
        for i in args:
            if i < result:
                result = i

    return result


print(calculator(10, 20, 30, operation="add", show_steps=True))
print(calculator(2, 3, 4, operation="multiply", show_steps=True))
print(calculator(10, 50, 30, 80, operation="max"))
print(calculator(10, 50, 30, 80, operation="min"))












def apply_operation(a, b, op):
    return op(a, b)

print(apply_operation(10, 5, lambda x, y: x + y))
print(apply_operation(10, 5, lambda x, y: x - y))
print(apply_operation(10, 5, lambda x, y: x * y))



def recursive_sum(*args):
    if len(args) == 0:
        return 0
    return args[0] + recursive_sum(*args[1:])
print(recursive_sum(10, 20, 30, 40))


numbers = list(range(1, 21))
result = list(map(lambda x: x*x,filter(lambda x: x % 3 == 0, numbers)))
print(result)


from functools import reduce
def weighted_average(**scores):
    total = reduce(lambda x, y: x + y, scores.values())
    return total / len(scores)
print(weighted_average(Maths=90, English=80, Science=70))


students = [
    {"name":"Ram","score":75},
    {"name":"Ravi","score":45},
    {"name":"Anu","score":90}
]
passed = filter(lambda x: x["score"] >= 60, students)
graded = map(lambda x: {**x, "grade":"Pass"}, passed)
result = sorted(graded, key=lambda x: x["score"], reverse=True)
print(result)


def outer():
    def inner():
        print("hi")
    inner()
    return inner
func=outer()
func()

def greet():
    print("hi")
    x=20
    print(x)
    return x
say_hi=greet()
value=say_hi()
print(value)
















