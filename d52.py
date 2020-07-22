#Write a function called calculate_score. calculate_score
#should take two parameters: a dictionary of student answers
#and a dictionary of correct answers. Both dictionaries should
#have integers as their keys, and one-character strings as
#their values.
#
#calculate_score should count how many questions the student
#got right. Or, in more precise terms, calculate_score should
#count how many keys for which the associated value is the
#same in the student's dictionary and in the answer key
#dictionary.
#
#As before, it is possible that there will be more answers in
#one than the other. This means that these answers don't
#belong to the same test! If that happens, return -1.
def calculate_score(student_answers, correct_answers):
    score = 0
    if len(student_answers) == len(correct_answers):
        for (question, answer) in student_answers.items():
            if answer == correct_answers[question]:
                score += 1
        return score
    else:
        return -1

#If your function works correctly, this will originally
#print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))
