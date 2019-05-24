from unittest import TestCase
from Practice_Test.Practice_code import Practice_code_file

class Test_Practice_Code(TestCase):
    def test_answer(self):
        some_obj = Practice_code_file(10,20)
        result = some_obj.some_function()
        assert result == 30


    def test_answer_two(self):
        some_obj = Practice_code_file(50,20)
        result = some_obj.some_function()
        assert result == 70


    def test_answer_three(self):
        some_obj = Practice_code_file(100,20)
        result = some_obj.some_function()
        assert result == 120

    def test_answer_four(self):
        some_obj = Practice_code_file(-10,20)
        result = some_obj.some_function()
        assert result == 10