import time
def delay_decorator(function):
    def wrapper_function():
        function()
        function()
    return wrapper_function



@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")
@delay_decorator
def say_bye():
    print("bye")
@delay_decorator
def say_greeting():
    print("How are you")



decorated_function = delay_decorator(say_greeting)
decorated_function()