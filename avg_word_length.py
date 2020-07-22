def word_count(my_string):
    word_count = 1
    for i in range(1, len(my_string)):
        if my_string[i] == " ":
            if not my_string[i - 1] == " ":
                word_count += 1
    return word_count

def letter_count(my_string):
    punct = [",", " ", ".", "!", "?"]
    let_count = 0
    for i in range(0, len(my_string)):
        if my_string[i] in punct:
            let_count += 0
        else:
            let_count += 1
    return let_count

def average_word_length(my_string):
    if isinstance(my_string, str):
        wd_count = word_count(my_string)
        let_count = letter_count(my_string)
        avg = (let_count/wd_count)
        return avg
    else:
        return "Not a string"


print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
