from main import *

run_cases = [
    (["ant", "planet", "sky", "cloud"], 5, 2, 10, 3, 4),
    (["red", "green", "blue", "gold"], 4, 3, 8, 2, 4),
]

submit_cases = run_cases + [
    ([], 3, 0, 7, 5, 2),
    (["hi", "to", "be"], 2, 3, 0, 4, 0),
    (["moon", "star", "galaxy", "sun", "comet"], 5, 2, 13, 4, 4),
]


def test(words, min_length, expected_long_count, target, jump_size, expected_jumps):
    print("---------------------------------")
    print(f"Words:      {words}")
    print(f"Min length: {min_length}")
    long_count = count_long_words(words, min_length)
    print(f"Expected long word count: {expected_long_count}")
    print(f"Actual long word count:   {long_count}")
    print("")
    print(f"Target:    {target}")
    print(f"Jump size: {jump_size}")
    jumps = count_jumps_to_target(target, jump_size)
    print(f"Expected jumps: {expected_jumps}")
    print(f"Actual jumps:   {jumps}")
    if long_count == expected_long_count and jumps == expected_jumps:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
