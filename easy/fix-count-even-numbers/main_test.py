from main import *

run_cases = [
    ([2, 5, 8, 11, 14], 3),
    ([4, 6, 7, 9], 2),
    ([10], 1),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, 3, 5, 7], 0),
    ([2, 4, 6, 8, 10], 5),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("")
    result = count_even_numbers(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
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
