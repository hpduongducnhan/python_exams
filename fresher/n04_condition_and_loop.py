from .rules import *
from typing import Callable, List


def question_01(test_funcs: List[Callable]):
    result = None
    try:
        x = 0
        a = 5
        b = 5
        if a > 0:
            if b < 0: 
                x = x + 5 
            elif a > 5:
                x = x + 4
            else:
                x = x + 3
        else:
            x = x + 2
        result = x
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
        x = 0
        for i in range(5):
            for j in range(-1, -5, -1):
                x += 1
        result = x
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
    result = ''
    try:
        for l in 'Jhon':
            if l == 'o':
                pass
            result += l
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
        var = 10
        for i in range(10):
            for j in range(2, 10, 1):
                if var % 2 == 0:
                    continue
                    var += 1
            var+=1
        else:
            var+=1

        result = var
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
        x = 0
        while (x < 100):
            x+=2

        result = x
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
    result = []
    try:
        for num in range(10, 14):
            for i in range(2, num):
                if num%i == 1:
                    result.append(num)
                    break

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_07(test_funcs: List[Callable]):
    result = None
    try:
        a, b = 12, 5
        if a + b:
            result = True
        else:
            result = False

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_08(test_funcs: List[Callable]):
    result = []
    try:
        numbers = [10, 20, 30]
        items = ["Chair", "Table", "Desk"]

        for x in numbers:
            for y in items:
                result.append((x, y,))

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)



def question_09(test_funcs: List[Callable]):
    result = []
    try:
        x = 0
        a = 0
        b = -5
        if a > 0:
            if b < 0: 
                x = x + 5 
            elif a > 5:
                x = x + 4
            else:
                x = x + 3
        else:
            x = x + 2
        result = x

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)