'''
НАЧАЛО:
Применение классов с менеджерами контекста
'''


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def a_print(self, text):
        print('  ' * self.level + str(text))


with Indenter() as indent:
    indent.a_print("Привет")
    with indent:
        indent.a_print("Я здесь")
        with indent:
            indent.a_print("А теперь тут")
    indent.a_print("Вернулся на первый уровень")
'''
КОНЕЦ:
Применение классов с менеджерами контекста
'''

'''
НАЧАЛО:
Использование вложенных функций,
Использование вызываемых классов,
Использование лямбда-функций
'''
'''
КОММЕНТАРИЙ:
* Функции являются объектами: их можно присваивать переменным,
  передавать в другие функции и возвращать из других функций.
* Функции могут быть определены внутри других функций — 
  и дочерняя функция может захватывать локальное состояние
  родительской функции (лексические замыкания).
'''


def get_speak_func(text, volume=0.):
    def yell():
        print(text.upper() + "!")
    if volume > 0.5:
        return yell
    else:
        print("Hi, I'm get_speak_func")


get_speak_func("Hello", 0.6)()


def adder(n):
    def add(x):
        return x + n
    return add


plus_3 = adder(3)
plus_5 = adder(5)

print(plus_3(4))
print(plus_5(4))


class Adder:
    def __init__(self,n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_7 = Adder(7)
print(plus_7(4))

add = lambda x, y: x + y
print(add(3, 5))
print(sorted(range(-5, 6), key=lambda x: x*x*x))
print(sorted(range(-5, 6), key=lambda x: x*x))

'''
КОНЕЦ:
Использование вложенных функций,
Использование вызываемых классов,
Использование лямбда-функций
'''

'''
НАЧАЛО:
Использование декораторов
'''
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


def uppercase2(func):
    return func().upper


@uppercase
def greet():
    return "Greetings!"


@uppercase2
def hello():
    return "Hello!"


greet2 = uppercase(greet)

print(greet())
print(greet2())
print(hello())


def strong(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper


def em(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


@strong
@em
@uppercase
def text():
    return "Some text"


print(text())


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return (f'ТРАССИРОВКА вызвана функцией {func.__name__}'
                f' с аргументами {args}, {kwargs}\n'
                f'Полученный результат: {result}')
    return wrapper


@trace
def multiply(x, y):
    return x * y


print(multiply(3, 5))

'''
КОНЕЦ:
Использование декораторов
'''

'''

'''
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


#asyncio.run(main())

async def main_concur():
    task1 = asyncio.create_task(say_after(4, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"Started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")


#asyncio.run(main_concur())


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial ({number}), currently i={i}")
        await asyncio.sleep(number)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main_factorial():
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 7),
    )
    print(L)


#asyncio.run(main_factorial())


def blocking_io():
    print(f"Start blocking_io at {time.strftime('%X')}")
    time.sleep(2)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main_block():
    print(f"Started main_blocking at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io()),
        asyncio.sleep(1),
    )
    print(f"Finished main_blocking at {time.strftime('%X')}")


asyncio.run(main())
