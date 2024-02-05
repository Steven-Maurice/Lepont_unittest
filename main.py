from autograding.grade import calculate_grade

if __name__ == '__main__':
    score = 72
    grade = calculate_grade(score)
    print(f'\n A score of {score} is a grade of {grade} \n')
