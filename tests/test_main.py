import unittest
import sys

from autograding.grade import calculate_grade
class TestMainTest(unittest.TestCase):
    def test_calculate_grade(self):
        grades = [85, 92, 78, 60, 45]
        valid_grades = ['B', 'A', 'C', 'D', 'F']
        for score, v_grade in zip(grades, valid_grades):
            grade = calculate_grade(score)
            self.assertEqual(grade, v_grade)

    def test_uppercase(self):
        string = "HELLO"
        self.assertTrue(string.isupper())

if __name__ == '__main__':
    unittest.main()