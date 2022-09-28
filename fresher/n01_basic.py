from .rules import *
from typing import Callable, List


def question_01(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    
    try:
        salary = 8000
        def printSalary():
            salary = 12000
            result_a = salary
            return result_a
        
        result_a = printSalary()
        result_b = salary
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = 'your asnwer here'
    your_answer_of_result_b =  'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result_a, result_b, your_answer_of_result_a, your_answer_of_result_b)
  


def question_02(test_funcs: List[Callable]):
    result_of_loop = None
    result_of_else = None
    try:
        for i in range(1, 5):
            result_of_loop = i
        else:
            result_of_else = "this is else block statement" 
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_of_loop and result_of_else values
    your_answer_of_result_of_loop = 'your asnwer here'
    your_answer_of_result_of_else =  'your asnwer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_of_loop, 
            your_answer_of_result_of_loop, 
            result_of_else, 
            your_answer_of_result_of_else
        )
  
def question_03(test_funcs: List[Callable]):
    result = None
    try:
        result = 36 / 4 * (3 +  2) * 4 + 2
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
    result = ''
    try:
        for i in range(10, 15, 1):
            result = result + str(i) + ', '
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
        var1 = 1
        var2 = 2
        var3 = "3"

        result = var1 + var2 + var3
    except Exception:
        pass
        
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer)


def question_06(test_funcs: List[Callable]):
    result = None
    try:
        sample = "pynative"
        result = sample[1:3]
    except Exception:
        pass
        
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


def question_07(test_funcs: List[Callable]):
    result = None
    try:
        def calculate (num1, num2=4):
            return num1 * num2

        result = calculate(5, 6)
    except Exception:
        pass

    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)



def question_08(test_funcs: List[Callable]):
    result_equal_operation = None
    result_is_operation = None
    try:
        listOne = [20, 40, 60, 80]
        listTwo = [20, 40, 60, 80]

        result_equal_operation = (listOne == listTwo)
        result_is_operation = (listOne is listTwo)
    except Exception:
        pass

    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_equal_operation = 'your answer here'
    your_answer_of_result_is_operation = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_equal_operation, 
            your_answer_of_result_equal_operation,
            result_is_operation,
            your_answer_of_result_is_operation
        )


def question_09(test_funcs: List[Callable]):
    result_equal_operation = None
    result_is_operation = None

    try:
        listOne = [20, 40, 60, 80]
        listTwo = [20, 40, 60, 80]

        result_equal_operation = (listOne == listTwo)
        result_is_operation = (listOne is listTwo)
    except Exception:
        pass


    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_equal_operation = 'your answer here'
    your_answer_of_result_is_operation = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            result_equal_operation, 
            your_answer_of_result_equal_operation,
            result_is_operation,
            your_answer_of_result_is_operation
        )


def question_10(test_funcs: List[Callable]):
    p = None
    q = None
    r = None

    try:
        p, q, r = 10, 20 ,30
    except Exception:
        pass
        
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_p = 'your answer here'
    your_answer_of_q = 'your answer here'
    your_answer_of_r = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(
            p, your_answer_of_p,
            q, your_answer_of_q,
            r, your_answer_of_r
        )



def question_11(test_funcs: List[Callable]):
    result = None

    try:
        sample = "James Bond"
        result = sample[2::-1]
    except Exception:
        pass
        
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result = 'your answer here'
    your_answer_of_q = 'your answer here'
    your_answer_of_r = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)



def question_12(test_funcs: List[Callable]):
    result = None

    try:
        sampleList = ["Jon", "Kelly", "Jessa"]
        sampleList.append(2, "Scott")
        result = sampleList
    except Exception:
        pass
        
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result = 'your answer here'
    # End your answer--------------------------------

    # TEST block -  do not change
    for func in test_funcs:
        func(result, your_answer_of_result)


if __name__ == '__main__':
    pass
    # question_01()