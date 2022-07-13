def bigger_is_greater(word):
    i, j = len(word) - 1, len(word) - 1

    while i > 0 and word[i - 1] >= word[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    while word[i - 1] >= word[j]:
        j -= 1

    word[i - 1], word[j] = word[j], word[i - 1]
    word[i:] = word[len(word) - 1 : i - 1 : -1]

    return "".join(word)


t = int(input("Number of words: "))
w = [list(input().strip()) for _ in range(t)]
print("\n", *map(bigger_is_greater, w), sep="\n")
