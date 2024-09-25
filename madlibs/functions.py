import random

def get_madlib():
    num = random.randint(1,5)
    path = "madlibs\\madlib" + str(num) + ".txt"

    file = open(path)
    madlib = file.readline()
    file.close()

    return madlib

def get_subjects(madlib: str):
    # subjects to replace in the madlib
    subjects = {}

    while "(" in madlib:
        start_index = madlib.find("(")
        end_index = madlib.find(")")
        subject = madlib[start_index:end_index+1]

        # Add subject to dictionary
        if subject in subjects:
            subjects[subject] += 1
        else:
            subjects[subject] = 1

        # Remove first instance of subject from madlib string
        madlib = madlib.replace(subject, "*", 1)

    return subjects

def replace_subjects(madlib: str, subjects: dict):
    for subject, count in subjects.items():
        for i in range(count):
            value = input(f"Enter {subject[1:-1].lower()}: ")
            madlib = madlib.replace(subject, value, 1)

    return madlib