def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@decorator
def get_message():
    return "hello user"
print(get_message())


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@decorator
def get_number():
    return 10

print(get_number())


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Order process started")
        func(*args, **kwargs)
        print("Order process completed")
    return wrapper
@decorator
def place_order(item):
    print("Order placed:", item)
place_order("Pizza")



def verify_user(func):
    def wrapper1(*args, **kwargs):
        print("User verified")
        func(*args, **kwargs)
    return wrapper1


def log_transaction(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Transaction logged")
    return wrapper


@log_transaction
@verify_user
def check_balance():
    print("Balance displayed")


check_balance()