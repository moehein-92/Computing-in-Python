
def check_plagiarism(file1, file2):
    d1 = {}
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    for line in f1:
        words = line.split()
        for i in range(0, len(words) - 5):
            if words[i] not in d1:
                d1[words[i]] = []
            d1[words[i]].append(words[i+1:i+5])
    ans = []
    for line in f2:
        words = line.split()
        for i in range(0, len(words) - 5):
            if words[i] in d1:
                if words[i+1:i+5] in d1[words[i]]:
                    j = i + 5
                    k = i + 1
                    while(words[k+1:j+1] in d1[words[k]]):
                        k+=1
                        j+=1
                        if (j == len(words)):
                            break
                    if(len(words[i:j]) > len(ans)):
                        ans = words[i:j]
    f1.close()
    f2.close()
    if len(ans) == 0:
        return False
    else:
        return " ".join(ans)

print(check_plagiarism("file_1.txt", "file_2.txt"))
#print(check_plagiarism("file_1.txt", "file_3.txt"))
#3print(check_plagiarism("file_2.txt", "file_3.txt"))
