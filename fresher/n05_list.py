from .rules import *
from typing import Callable, List


def question_01(test_funcs: List[Callable]):
    result = None
    try:
        samples = ["Hello", "Python"]
        result = "-".join(samples)
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
    result_a = None
    result_b = None
    result_c = None
    try:
        samples = [10, 20, 30, 40, 50, 60, 70, 80]
        result_a = samples[2:5]
        result_b = samples[:4]
        result_c = samples[3:]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = 'your_answer'
    your_answer_of_result_b = 'your_answer'
    your_answer_of_result_c = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b,
            result_c, your_answer_of_result_c,
        )


def question_03(test_funcs: List[Callable]):
    result = None
    try:
        samples = ['xyz', 'zara', 'PYnative']
        result = max(samples)

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
        sampleList = [10, 20, 30, 40, 50]
        result = sampleList[-4:-1]
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
    result_a = None
    result_b = None
    try:
        listOne  =  ['a', 'b', 'c', 'd']
        listTwo =  ['e', 'f', 'g']

        result_a = listOne.extend(listTwo)
        result_b = listOne + listTwo
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = 'your_answer'
    your_answer_of_result_b = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_06(test_funcs: List[Callable]):
    result = None
    try:
        sample = [5, 10, 15, 25]
        result = sample[::-2]

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
    result_a = None
    result_b = None
    try:
        sample = ["PYnative", [4, 8, 12, 16]]
        print(sample[0][1])    
        print(sample[1][3])

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = 'your_answer'
    your_answer_of_result_b = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_08(test_funcs: List[Callable]):
    result = None
    try:
        l = [None] * 10
        result = len(l)
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
    result_a = None
    result_b = None
    try:
        sampleList = [10, 20, 30, 40, 50]
        sampleList.pop()
        result_a = sampleList

        sampleList.pop(2)
        result_b = sampleList

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = 'your_answer'
    your_answer_of_result_b = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_10(test_funcs: List[Callable]):
    result = None
    try:
        result = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)



def question_11(test_funcs: List[Callable]):
    result = None
    try:
        result = [4, 8, 12, 16]
        result[1:4] = [20, 24, 28]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_12(test_funcs: List[Callable]):
    result = None
    try:
        aList = [1, 2, 3, 4, 5, 6, 7]
        result = [2 * x for x in aList]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)



def question_13(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        sampleList = [10, 20, 30, 40, 50]
        sampleList.append(60)
        result_a = sampleList

        sampleList.append(60)
        result_b = sampleList

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = 'your_answer'
    your_answer_of_result_b = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b
        )


def question_14(test_funcs: List[Callable]):
    result = None
    try:
        sampleList = [10, 20, 30, 40]
        del sampleList[0:6]
        result = sampleList
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)