"""
        Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
    """

def score_checker():
    grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'E': 50, 'F': 0}

    while True:
        try:
            score = int(input("Enter your score: "))
            if 0<=score<=100:
                break
            else:
                print("Enter a number between 0-100")
        except ValueError:
            print("Invalid input. ")

    for grade, min_score in grades.items():
        if score >= min_score:
            print(f"Your grade will be: {grade}")
            break

def main():
    score_checker()

main()


