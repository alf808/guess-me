def run_timing():
    time_list = []
    err = ""
    while True:
        user_input = input(f"Enter 10 km run time: ")
        if user_input:
            if user_input.isnumeric():
                try:
                    user_input = float(user_input)
                except ValueError as ve:
                    print("Please enter a number.")
                    err = ve
                else:
                    time_list.append(user_input)
        else:
            if time_list:
                return sum(time_list)/len(time_list)


print(run_timing())
