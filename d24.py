#Write a function called grade_scantron. grade_scantron should
#take as input two lists: answers and key. Each list contain
#strings. Each string will be only one letter, a character
#from A to E. grade_scantron should return how many questions
#the student got "right", where a student gets a question
#right if their answer for a problem matches the answer key.
#
#In other words, if value of the first item in answers matches
#the value of the first item in key, the student gets a point.
#If it does not, the student does not get a point.
#
def grade_scantron(answers, key):
    score = 0
    index = 0
    if len(answers) == len(key):
        for i in answers:
            if answers[index] == key[index]:
                score += 1
            index += 1
        return score
    else:
        score = -1
        return score


#If your function works correctly, this will originally
#print: 7
test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))
