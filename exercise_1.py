n = int(input("number of lines: "))
words = [input().strip() for i in range(n)]
dictionary = {}

for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1

print(len(dictionary))
print(*list(dictionary.values()))
