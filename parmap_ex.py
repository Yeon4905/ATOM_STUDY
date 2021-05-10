# how to use parmap module

import parmap
from tqdm import tqdm
def myfunction(*args, **kwargs):
    return args, kwargs

if __name__ == '__main__':
    mylist = [1,2,3]
    argument1 = 3.14
    argument2 = True
    argument3 = False
    mylists = [(1,2), (3,4), (5,6)]

    """ without using parmap, you can use your function for parallelization"""
    y = [myfunction(x, argument1, mykeyword = argument2) for x in mylist]


    """ without using mykeyword (kwargs)"""
    y = parmap.map(myfunction, mylist, argument1, pm_pbar = True)
    """you get the result like this:
            [((1, 3.14), {}), ((2, 3.14), {}), ((3, 3.14), {})]"""


#     """ using all of parameters(arguments)"""
#     # you can use kwargs using other variable name
#     y = parmap.map(myfunction, mylist, argument1, mykeyword = argument2)
#     """ you get the result like this:
#             [((1, 3.14), {'mykeyword': True}),
#              ((2, 3.14), {'mykeyword': True}),
#              ((3, 3.14), {'mykeyword': True})] """


#     """ multiple arguments """
#     z = [myfunction(x,y, argument1, argument2, mykey = argument3) for (x,y) in mylists]
#     """result: [((1, 2, 3.14, True), {'mykey': False}),
#                 ((3, 4, 3.14, True), {'mykey': False}),
#                 ((5, 6, 3.14, True), {'mykey': False})]"""

#     z1 = parmap.starmap(myfunction, mylists, argument1, argument2, mykey = argument3, pm_pbar = True, pm_processes= 3)
#     """result: [((1, 2, 3.14, True), {'mykey': False}),
#                 ((3, 4, 3.14, True), {'mykey': False}),
#                 ((5, 6, 3.14, True), {'mykey': False})] """

#     listx = [1,2,3,4,5,6]
#     listy = [2,3,4,5,6,7]
#     param1 = 3.14
#     param2 = 42
#     listz = []
#     for (x,y) in zip(listx, listy):
#         listz.append(myfunction(x, y, param1, param2))
#     print(listz)
#     # In parallel:
#     listz = parmap.starmap(myfunction, zip(listx, listy), param1, param2)
#     print(listz)
#     """ result: [((1, 2, 3.14, 42), {}), ((2, 3, 3.14, 42), {}),
#                 ((3, 4, 3.14, 42), {}), ((4, 5, 3.14, 42), {}),
#                 ((5, 6, 3.14, 42), {}), ((6, 7, 3.14, 42), {})]"""


# """ multiple parallel tasks running in parallel
#     Does not have pm_pbar"""
# def task1(item):
#     return 2*item

# def task2(item):
#     return 2*item + 1

# if __name__ == "__main__":
#     items1 = range(500000)
#     items2 = range(500)

#     with parmap.map_async(task1, items1, pm_processes = 5) as result1:
#         with parmap.map_async(task2, items2, pm_processes = 3) as result2:
#             data_task1 = None
#             data_task2 = None
#             task1_working = True
#             task2_working = True
#             while task1_working or task2_working:
#                 result1.wait(0.1)
#                 if task1_working and result1.ready():
#                     print("Task1 has finished!")
#                     data_task1 = result1.get()
#                     task1_working = False
#                 result2.wait(0.1)
#                 if task2_working and result2.ready():
#                     print("Task2 has finished!")
#                     data_task2 = result2.get()
#                     task2_working = False

import multiprocessing
from itertools import repeat

def a(x,d):
    d[x] = True
    
    