def itcast1(fun):
    def inner(*args, **kwargs):
        print("itcast1 start")

        result = fun(*args, **kwargs)
        print(result)
        print("itcast1 end")

        return result

    return inner


@itcast1
def say_hello():
    return "hello"

print("===============================")
say_hello()  # inner()
print("===============================")

@itcast1
def add(num1, num2):
    print(num1 + num2)

print("===============================")


add(100, 200)  # inner(100, 200)


# 函数中如果没有使用return返回值，默认情况函数也是有返回值的，默认返回None


@itcast1
def minus(num1, num2):
    return num1 - num2


ret = minus(200, 50)  # ret =  inner(200, 50)

print(ret)
