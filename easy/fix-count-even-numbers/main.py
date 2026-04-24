numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # python counts 0 as even
def count_even_nummbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count
print(count_even_nummbers(numbers))

