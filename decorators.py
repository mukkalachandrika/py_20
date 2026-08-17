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
value=say_hi
print(value)

def greet(name):
    print("my name is",name)
def m1():
    print("hi!")
m1()
greet("Kulfi")

def m1(func):
    print("hi!")
    func("Kulfi")
m1(greet)


def intro():
    print("this is py-20")


def decorator1(func):
    def wrapper1():
        print("hi")
        func()
    return wrapper1
modify = decorator1(intro)
modify()


def about():
    print("my name is chandrika")
    print("i am from guntur")



def intro():
    print("this is py-20")


def decorator1(func):
    def wrapper1():
        print("hi")
        func()
    return wrapper1
intro = decorator1(intro)
intro()

def system_decorator(func):
    def wrapper():
        print("System starting...")
        func()
        print("System started successfully")
    return wrapper
def start_system():
    print("Loading system")
start_system()


def message_decorator(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Goodbye!")
    return wrapper
def show_message():
    print("Have a nice day!")
show_message()


def payment_decorator(func):
    def wrapper():
        print("Payment initiated")
        func()
        print("Payment successful")
    return wrapper
def make_payment():
    print("Processing payment")
make_payment()


def start_system():
    print("Starting System")
def dec1(func):
    def wrapper1():
        func()
        print("System started")
    return wrapper1
start_system = dec1(start_system)
start_system()

def show_message():
    print("Showing the message")
def dec2(func):
    def wrapper2():
        print("Welcome!")
        func()
        print("Done displaying the message")
    return wrapper2
show_message = dec2(show_message)
show_message()


def make_payment():
    print("Processing payment")
def dec3(func):
    def wrapper3():
        print("Payment initiated")
        func()
        print("Payment successful")
    return wrapper3
make_payment = dec3(make_payment)
make_payment()


def add(a,b):
    print(a+b)
def dec1(func):
    def wrapper1(*args,**kwargs):
        print("before calling")
        func(*args,**kwargs)
        print("after calling")
    return wrapper1
x=dec1(add)
x(10,20)

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("before calling")
        func(*args, **kwargs)
        print("after calling")
    return wrapper


def add(a, b):
    print(a + b)

add = decorator1(add)
add(10, 20)


@decorator1
def add(a, b):
    print(a + b)

add(20, 30)


#qes1
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@decorator
def get_message():
    return "hello user"
print(get_message())

#ques2
def decorator2(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result*2
    return wrapper
@decorator2
def get_number():
    return 10
print(get_number())

#ques3
def decorator3(func):
    def wrapper(*args,**kwargs):
        print("Order process started")
        func(*args,**kwargs)
        print("order process completed")
    return wrapper
@decorator3
def order_item(item):
    print("order placed",item)
order_item("chicken 65")


#ques4
def decorator4(func):
    def wrapper(*args,**kwargs):
        print("authenticating user")
        func(*args,**kwargs)
        print("login successful")
    return wrapper
@decorator4
def login_user(username):
    print(username)
login_user("chandrika")

#ques5
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Sending message...")
        result = func(*args, **kwargs)
        print("Message sent")
        return result
    return wrapper
@decorator
def send_message(msg):
    print(msg)
send_message("Hello!")

#ques 6
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculating sum...")
        result = func(*args, **kwargs)
        print("Calculation done")
        return result
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(10, 20))


#ques7
def decorator7(func):
    def wrapper(*args, **kwargs):
        print("Applying discount...")
        result = func(*args, **kwargs)
        print("Discount applied")
        return result
    return wrapper
@decorator7
def apply_discount(price):
    discount=100
    return price - discount
print(apply_discount(1000))



def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Sending message...")
        return func(*args, **kwargs)
    return wrapper
def decorator2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Message sent")
        return result
    return wrapper
@decorator2
@decorator1
def send_message(msg):
    print(msg)
print(send_message.__name__)
send_message("Hello!")


def method1():
    print("hello")
print(method1.__name__)

import functools


def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Sending message...")
        return func(*args, **kwargs)
    return wrapper
def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Message sent")
        return result
    return wrapper
@decorator2
@decorator1
def send_message(msg):
    print(msg)
print(send_message.__name__)
send_message("Hello!")

def dec1(func):
    def wrapper1(*args, **kwargs):
        print("hi")
        func(*args, **kwargs)
    return wrapper1


def dec2(func):
    def wrapper2(*args, **kwargs):
        func(*args, **kwargs)
        print("bye")
    return wrapper2


@dec2
@dec1
def my_name(name):
    print("my name is", name)


my_name("kate")

#14-08-2026
def verify_user(func):
    def wrapper1(*args,**kwargs):
        print("user verified")
        func(*args,**kwargs)
    return wrapper1
def log_transaction(func):
    def wrapper2(*args,**kwargs):
        func(*args, **kwargs)
        print("Transaction logged")
    return wrapper2
@log_transaction
@verify_user
def check_balance():
    print("balance displayed")
check_balance()


def login_required(func):
    def wrapper(*args, **kwargs):
        print("Login verified")
        return func(*args, **kwargs)
    return wrapper
def log_activity(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Exam activity logged")
        return result
    return wrapper
@login_required
@log_activity
def start_exam(student):
    print("Exam started for", student)
start_exam("Chandrika")



def login_check(func):
    def wrapper(*args, **kwargs):
        print("Login verified")
        return func(*args, **kwargs)
    return wrapper
def order_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Order recorded")
        return result
    return wrapper
@login_check
@order_log
def place_order():
    print("Order placed successfully")
place_order()



