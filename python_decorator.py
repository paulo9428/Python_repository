# @ 심볼 활용하기 
 
def decorator_function(original_function):
    def wrapper_function():
        print("{} 함수가 호출되기 전입니다.".format(original_function.__name__))
        return original_function()
    return wrapper_function
 
@decorator_function
def display_1():
    print("display_1 함수가 실행됐습니다.")
 
@decorator_function
def display_2():
    print("display_2 함수가 실행됐습니다.")
 
# display_1 = decorator_function(display_1) 
# display_2 = decorator_function(display_2) 
 
display_1() # 변수에 함수형 리턴값 할당 없이 바로 함수 호출이 가능하다. 
display_2() # 변수에 함수형 리턴값 할당 없이 바로 함수 호출이 가능하다. 

#-----------------------------------------------------------------------------------------

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("{} 함수가 호출되기 전입니다.".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
 
@decorator_function
def display_1():
    print("display_1 함수가 실행됐습니다.")
 
@decorator_function
def display_info(name, age): # 위 예제와 다르게 인자가 전달된다. 
    print("display_info( {}, {} ) 함수가 실행됐습니다.".format(name, age))
 
# display_1 = decorator_function(display_1) 
# display_2 = decorator_function(display_2) 
 
display_1()
display_info('김아무개', 37)


# ------------------------------------------------------------------

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function : ', func.__name__)
        print('Positional arguments : ', args)
        print('Keyword arugments :' , kwargs)
        result = func(*args, **kwargs)
        print('Result : ', result)
        return result
    return new_function
 
def add_inits(a, b):
    return a + b
 
 
def div_inits(a,b):
    return a / b
 
add = document_it(add_inits)
div = document_it(div_inits)
 
print("")
print(add(5,3))
print("")
print(div(5,3))