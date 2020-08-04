def my_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def my_avg(*numbers):
    return my_sum(*numbers) / len(numbers)

num_list = [1,2,3,4,5,6,7,8,9]

print(f"sum: {my_sum(1,2,3,4,5,6,7,8,9)}")
print(f"avg: {my_avg(1,2,3,4,5,6,7,8,9)}")

# The asterisk in *args changes tuple or list to a sequence of scalars
#print(f"sum list: {my_sum(*tuple(num_list))}")
print(f"sum list: {my_sum(*num_list)}")
