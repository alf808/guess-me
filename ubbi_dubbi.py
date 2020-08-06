def ubbi_dubbi(word):
    char_lst = []
    for char in word:
        if char in 'aeiou':
            nc = f"ub{char}"
            char_lst.append(nc)
        else:
            char_lst.append(char)
    return "".join(char_lst)

print(ubbi_dubbi("octopus"))
            
            
