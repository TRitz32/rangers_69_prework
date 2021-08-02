def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name('USERNAME')

start, end = 0, 100
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")

def odd_numbers():
    for num in range(1, 100, 2):
        print(num)

print(odd_numbers())

def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max

a_list = [56, 28, 1, 989, 4569, 345]
print("Largest number is:", max_num_in_list(a_list))

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])
print(max_num_in_list([2, 6, 3, 98, 34]))

def max_num(a_list):
    print(max(a_list))
print(max_num([1, 7, 87, 45]))

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(1960))
print(is_leap_year(1977))

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(1967))

