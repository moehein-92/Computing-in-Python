def search_for_string(lst, goal):
    indices = []

    for i in range(0, len(lst)):
        if lst[i] == goal:
            indices.append(i)
    return indices

sample_list = ["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"]
print(search_for_string(sample_list, "turnip"))
