def reverse_it(str):
    str_list = list(str)
    str_list.reverse()
    return "".join(str_list)

print(reverse_it("hello"))
