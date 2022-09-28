from .rules import *
from typing import Callable, List

# done
def question_01(test_funcs: List[Callable]):
    result = None
    try:
        samples = ("Hello", "World")
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

# done
def question_02(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    result_c = None
    try:
        samples = (10, 20, 30, 40, 50, 60, 70, 80)
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

# done
def question_03(test_funcs: List[Callable]):
    result = None
    try:
        samples = (1120, 'a')
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

# done
def question_04(test_funcs: List[Callable]):
    result = None
    try:
        sampleList = (100, 200, 300, 400, 500)
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


# done
def question_05(test_funcs: List[Callable]):
    result = None
    try:
        sample  =  (100,)

        result = sample * 2
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)

# done
def question_06(test_funcs: List[Callable]):
    result = None
    try:
        sample = (5, 10, 15, 25)
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

# done
def question_07(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        sample = ("Orange", [10, 20, 30], (5, 15, 25))
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

# done
def question_08(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    result_c = None
    try:
        aTuple = "Yellow", 20, "Red"
        result_a, result_b, result_c = aTuple
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


# done
def question_09(test_funcs: List[Callable]):
    result = None
    try:
        aTuple = (100, 200, 300, 400, 500)
        aTuple.pop(2)
        result = aTuple

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your_answer'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)

