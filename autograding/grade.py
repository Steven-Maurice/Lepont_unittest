def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

if __name__ == "__main__":
    # Run the tests
    import unittest
    class TestGrade(unittest.TestCase):
        def test_grade_A(self):
            self.assertEqual(calculate_grade(95), 'A')
        def test_grade_B(self):
            self.assertEqual(calculate_grade(85), 'B')
        def test_grade_C(self):
            self.assertEqual(calculate_grade(75), 'C')
        def test_grade_D(self):
            self.assertEqual(calculate_grade(65), 'D')
        def test_grade_E(self):
            self.assertEqual(calculate_grade(55), 'E')
    unittest.main()