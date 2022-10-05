pattern = input()
bil = int(input())
words = []

for i in range(bil):
    words.append(input())

if len(pattern) == 1 and pattern[0] == "*":
    for word in words:
        print(word)
else:
    patterns = pattern.split("*")
    if pattern[0] == "*":
        for word in words:
            if len(word) >= len(patterns[1]):
                word_temp = word[-len(patterns[1]):]
                if patterns[1] == word_temp:
                    print(word)
    elif pattern[-1] == "*":
        for word in words:
            if len(word) >= len(patterns[0]):
                word_temp = word[:len(patterns[0])]
                if patterns[0] == word_temp:
                    print(word)
    else: 
        for word in words:
            if len(word) >= len(patterns[0] + patterns[1]):
                word_temp = word[:len(patterns[0])]
                if patterns[0] == word_temp:
                    word_temp2 = word[-len(patterns[1]):]
                    if patterns[1] == word_temp2:
                        print(word)