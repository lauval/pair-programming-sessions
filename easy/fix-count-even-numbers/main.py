def count_even_nummbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 1:
            count += 1
        return count
