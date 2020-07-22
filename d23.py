def sort_artists(list):
    names = []
    sales = []
    for tuples in list:
        name = tuples[0]
        names.append(name)
        sale = tuples[1]
        sales.append(sale)
    names.sort()
    sales.sort()
    sales.reverse()
    result = (names, sales)
    return result

# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))
