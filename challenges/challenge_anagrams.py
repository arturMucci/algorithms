def sortNaMao(word):
    if 0 == len(word) <= 1:
        return word
    else:
        pilot = word[0]
        arrayLesser = [x for x in word[1:] if x < pilot]
        arrayEqual = [x for x in word if x == pilot]
        arrayGreater = [x for x in word[1:] if x > pilot]
        return sortNaMao(arrayLesser) + arrayEqual + sortNaMao(arrayGreater)


def is_anagram(first_string, second_string):
    first = "".join(sortNaMao(first_string.lower()))
    second = "".join(sortNaMao(second_string.lower()))
    if not first or not second:
        return (first, second, False)
    check = first == second
    return (first, second, check)
