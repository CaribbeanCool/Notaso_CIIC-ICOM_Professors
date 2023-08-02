import os

# function that wipes console for better readability


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")

# function to determine the letter grade of a specific professor


# def determineLetterGrade(percent):

#     textnum = percent[0:5]
#     num = float(textnum)

#     if num >= 90 and num <= 100:
#         return 'A'
#     elif num >= 80 and num <= 89:
#         return 'B'
#     elif num >= 70 and num <= 79:
#         return 'C'
#     elif num >= 60 and num <= 69:
#         return 'D'
#     else:
#         return 'F'
