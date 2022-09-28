from .rules import *
from typing import Callable, List
import copy


def question_01(test_funcs: List[Callable]):
    result = None
    try:
        dict1 = {"key1":1, "key2":2}
        dict2 = {"key2":2, "key1":1}
        result = (dict1 == dict2)
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
        student = { 
            "name": "Emma", 
            "class": 9, 
            "marks": 75 
        }
        del student[0:2]
        result = student
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
        dict1 = {"name": "Mike", "salary": 8000}
        result = dict1.pop("age")

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
        sample = {
            1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
            2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}
        }
        result = sample[1]['age']
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
        sampleDict = { 
            "class":{ 
                "student":{ 
                    "name":"Mike",
                    "marks":{ 
                        "physics": 70,
                        "history": 80
                    }
                }
            }
        }
        result_a = "Mike"
        result_b = 70
    except Exception:
        pass
    # Fill your answers here-------------------------
    # write code to get value from sampleDict
    your_answer_of_result_a = sampleDict
    your_answer_of_result_b = sampleDict
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_a, your_answer_of_result_a,
            result_b, your_answer_of_result_b,
        )


def question_06(test_funcs: List[Callable]):
    result = None
    try:
        sample = {
            "name": "Emma",
            "class": 9,
            "marks": 75
        }
        result = sample.get('age')
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
        sampleDict = dict([
            ('first', 1),
            ('second', 2),
            ('third', 3)
        ])
        result = sampleDict

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
    result_a = None
    result_b = None
    try:
        dict1 = {'hello': 'world', 'hi': 'there'}
        dict2 = {'hello': 'world', 'hi': 'there'}

        result_a = (dict1 == dict2)
        result_b = (dict1 is dict2)
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



def question_09(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        dict1 = {'hello': 'world', 'hi': 'there'}
        dict2 = dict2

        result_a = (dict1 == dict2)
        result_b = (dict1 is dict2)
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
    result_a = None
    result_b = None
    try:
        dict1 = {'hello': 'world', 'hi': 'there'}
        dict2 = copy.copy(dict1)

        result_a = (dict1 == dict2)
        result_b = (dict1 is dict2)
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