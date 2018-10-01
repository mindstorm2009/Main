import reverse


def test_reverse_rec(name, a_string, expected):
    result = reverse.reverse_rec(a_string)
    if result == expected:
        print(name, "passed")
    else:
        print(name, "failed; expected", expected, "got", result)


def test_reverse_rec_empty():
    test_reverse_rec("empty", "", "")


def test_reverse_rec_one():
    test_reverse_rec("one", "a", "a")


def test_reverse_rec_three():
    test_reverse_rec("three", "abc", "cba")


def test_reverse_rec_palindrome():
    test_reverse_rec("palindrome", "PalindromemordnilaP", "PalindromemordnilaP")


def run_all_tests():
    test_reverse_rec_empty()
    test_reverse_rec_one()
    test_reverse_rec_three()
    test_reverse_rec_palindrome()


if __name__ == "__main__":
    run_all_tests()
