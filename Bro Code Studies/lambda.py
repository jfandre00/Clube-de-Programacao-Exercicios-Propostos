# Lamba function = A small anonymous function for a single line of code (throw away function)

double = lambda x: x * 2
add = lambda x, y: x + y

print(double(5))
print(add(5, 2))


max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y

print(max_value(5, 2))
print(min_value(5, 2))

full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))

is_even = lambda num: num % 2 == 0
print(is_even(5))
print(is_even(6))

age_check = lambda age: True if age >= 18 else False
print(age_check(20))
print(age_check(15))
