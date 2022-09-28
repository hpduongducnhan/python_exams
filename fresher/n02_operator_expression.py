from .rules import *
from typing import Callable, List


def question_01(test_funcs: List[Callable]):
    result = None
    try:
        x = 100
        y = 50
        result = x and y
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)

def question_02(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        result_a = [10, 20]
        result_b = result_a
        result_b += [30, 40]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = 'your asnwer here'
    your_answer_of_result_b = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_03(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        x = 6
        y = 2
        result_a = x ** y
        result_b = x // y
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = 'your asnwer here'
    your_answer_of_result_b = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_04(test_funcs: List[Callable]):
    result = None
    try:
        result = 2 ** 3 ** 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_05(test_funcs: List[Callable]):
    result = None
    try:
        y = 10
        result = y += 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_06(test_funcs: List[Callable]):
    result = None
    try:
        y = 6
        result = 2%y
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_07(test_funcs: List[Callable]):
    result = None
    try:
        result = 36/4
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_08(test_funcs: List[Callable]):
    result = None
    try:
        result = 10 - 4 * 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_09(test_funcs: List[Callable]):
    result = None
    try:
        result = 2 * 2 ** 3 * 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)



def question_10(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        result_a = 10
        result_b = 50
        if result_a ** 2 > 100 and result_b < 100:
            x = result_a + 10 ** result_b
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = 'your asnwer here'
    your_answer_of_result_b = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_11(test_funcs: List[Callable]):
    result = None
    try:
        result = -18 // 4
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)



def question_12(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        # 4 is 100 in binary and 11 is 1011 in binary
        a = 4
        b = 11
        result_a = a | b
        result_b = a >> 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = 'your asnwer here'
    your_answer_of_result_b = 'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )