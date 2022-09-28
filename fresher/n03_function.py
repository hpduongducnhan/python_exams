from .rules import *
from typing import Callable, List


def question_01(test_funcs: List[Callable]):
    result = None
    try:
        def add(a, b):
            return a+5, b+5

        result = add(3, 2)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_02(test_funcs: List[Callable]):
    result = None
    try:
        def outer_fun(a, b):
            def inner_fun(c, d):
                return c + d
            return inner_fun(a, b)
            return a
        result = outer_fun(5, 10)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)



def question_03(test_funcs: List[Callable]):
    result = None
    try:
        def display(**kwargs):
            return [i for i in kwargs]

        result = display(emp="Kelly", salary=9000)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_04(test_funcs: List[Callable]):
    result = None
    try:
        def outer_fun(a, b):
            def inner_fun(c, d):
                return c + d
            return inner_fun(a, b)

        result = outer_fun(5, 10)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)



def question_05(test_funcs: List[Callable]):
    result = None
    try:
        def fun1(num):
            return num + 25

        result = fun1(5)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_06(test_funcs: List[Callable]):
    result = None
    try:
        def display(*args):
            return [i for i in args]

        result = display(name="Kelly", age=18)
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)




