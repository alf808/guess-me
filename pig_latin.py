def pig_latin(word):
    if word[0] in 'aeiou':
        return f"{word}way"

    return f"{word[1:]}{word[0]}ay"


def pl_sentence(str):
    str_list = []
    for word in str.split():
        str_list.append(pig_latin(word))
    return " ".join(str_list)


print(pig_latin("python"))
print(pig_latin("alf"))
print(pl_sentence("the quick brown fox jumps over"))
