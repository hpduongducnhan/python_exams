from fresher.rules import *
from fresher.n06_tuple import *


def test_question_01():
    qname = 'question 01'
    def test_func(res_a, res_b, answer_a, answer_b):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
        assert res_b == answer_b, ASSERT_FAILED.format(qname)
    question_01([test_func])
    logger.info(f'{qname} passed')


def test_question_02():
    qname = 'question 02'
    def test_func(res_a, answer_a, res_b, answer_b):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
        assert res_b == answer_b, ASSERT_FAILED.format(qname)
    question_02([test_func])
    logger.info(f'{qname} passed')


def test_question_03():
    qname = 'question 03'
    def test_func(res_a, answer_a):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
    question_03([test_func])
    logger.info(f'{qname} passed')


def test_question_04():
    qname = 'question 04'
    def test_func(res_a, answer_a):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
    question_04([test_func])
    logger.info(f'{qname} passed')


def test_question_05():
    qname = 'question 05'
    def test_func(res_a, answer_a):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
    question_05([test_func])
    logger.info(f'{qname} passed')


def test_question_06():
    qname = 'question 06'
    def test_func(res_a, answer_a):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
    question_06([test_func])
    logger.info(f'{qname} passed')



def test_question_07():
    qname = 'question 07'
    def test_func(res_a, answer_a):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
    question_07([test_func])
    logger.info(f'{qname} passed')


def test_question_08():
    qname = 'question 08'
    def test_func(res_a, answer_a, res_b, answer_b):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
        assert res_b == answer_b, ASSERT_FAILED.format(qname)
    question_08([test_func])
    logger.info(f'{qname} passed')


def test_question_09():
    qname = 'question 09'
    def test_func(res_a, answer_a, res_b, answer_b):
        assert res_a == answer_a, ASSERT_FAILED.format(qname)
        assert res_b == answer_b, ASSERT_FAILED.format(qname)
    question_09([test_func])
    logger.info(f'{qname} passed')


if __name__ == '__main__':
    test_question_02()