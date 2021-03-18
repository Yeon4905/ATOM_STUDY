# how to use arguments(which is same as parameters) and keyword arguments
# you can use *(asterisk) when you do not know how many args and kwargs would be used in function

def myfunction(*args, **kwargs):
    return args, kwargs

if __name__ == '__main__':
    mylist = [1,2,3]
    argument1 = 3.14
    argument2 = True

    y = [myfunction(x, argument1, mykeyword = argument2) for x in mylist]
    
