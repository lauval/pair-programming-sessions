# exercise to convey the difference between for loops and while loops

def count_long_words(words, min_length):
    """
    function to count words in a list exceeding the minimum length

    input:
    words - [list] a list of strings.
    min_length - [int] the minimum character length to check each word against.

    output:
    num_words - [int] the number of words meeting/exceeding the character length limit.
    """

    # initalise counter variable at 0
    count = 0

    # loop over all words in the list
    for word in words:
        # determine length of each word using built-in `len()` function
        length = len(word)
        # check if word length exceeds minimum character length value
        if length >= min_length:
            # increment counter by 1
            count += 1
    # return number of words exceeding character limit
    return count


def count_jumps_to_target(target, jump_size):
    """
    function to count the number of jumps required to reach a target.

    input:
    target - [int] 
    jump_size - [int]
    """

    # initilise empty counter variable
    count = 0
    # keep track of the current position, starting from zero
    position = 0

    # loop until the position is equal to or past the target
    while position < target:
        # udpate the position by jumping one jump size unit
        position += jump_size
        # increment the counter by 1
        count += 1
    # return the number of jumps taken to reach or exceed the target
    return count
