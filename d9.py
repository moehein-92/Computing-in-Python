def string_type(string):
    space = 0
    if string == "":
        return "empty"
    elif len(string) == 1:
        return "character"
    elif not chr(32) in string:
        return "word"
    elif chr(32) in string:
        if string.count("\n") >= 1:
                return "page"
        elif string.count(".") <= 1:
            return "sentence"
        elif string.count(".") > 1:
            return "paragraph"


#print(".".count("There's way too many ostriches. Why are there so many ostriches."))
#empty
#character
#word
#sentence
#paragraph
#page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))
