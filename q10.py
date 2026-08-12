def calculator(*args, operation="add", **options):
    op = {
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "max": lambda x, y: x if x > y else y,
        "min": lambda x, y: x if x < y else y
    }
    func = op[operation]
    res = args[0]
    for i in args[1:]:
        if options.get("show_steps"):
            print(res, i, operation, ":", func(res, i))
        res = func(res, i)
    return res
print(calculator(10, 20, 30, operation="add", show_steps=True))
print(calculator(2, 3, 4, operation="mul", show_steps=True))
print(calculator(10, 50, 30, 80, operation="max"))
print(ca





lculator(86, 27,16,74, operation="min"))