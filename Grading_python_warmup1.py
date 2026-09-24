

def sleep_in_test():
    """Run the 4 checks for sleep_in only."""
    cases = [
        ((False, False), True, 'CodingBat example'),
        ((True, False), False, 'CodingBat example'),
        ((False, True), True, 'CodingBat example'),
        ((True, True), True, 'CS110 extra'),
    ]
    passed = 0
    print("\nsleep_in —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "sleep_in(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = sleep_in(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for sleep_in: {passed}/{len(cases)} passed")
    return passed, len(cases)


def monkey_trouble_test():
    """Run the 4 checks for monkey_trouble only."""
    cases = [
        ((True, True), True, 'CodingBat example'),
        ((False, False), True, 'CodingBat example'),
        ((True, False), False, 'CodingBat example'),
        ((False, True), False, 'CS110 extra'),
    ]
    passed = 0
    print("\nmonkey_trouble —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "monkey_trouble(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = monkey_trouble(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for monkey_trouble: {passed}/{len(cases)} passed")
    return passed, len(cases)


def sum_double_test():
    """Run the 6 checks for sum_double only."""
    cases = [
        ((1, 2), 3, 'CodingBat example'),
        ((3, 2), 5, 'CodingBat example'),
        ((2, 2), 8, 'CodingBat example'),
        ((0, 0), 0, 'CS110 extra'),
        ((-2, -2), -8, 'CS110 extra'),
        ((5, -1), 4, 'CS110 extra'),
    ]
    passed = 0
    print("\nsum_double —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "sum_double(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = sum_double(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for sum_double: {passed}/{len(cases)} passed")
    return passed, len(cases)


def diff21_test():
    """Run the 6 checks for diff21 only."""
    cases = [
        ((19,), 2, 'CodingBat example'),
        ((10,), 11, 'CodingBat example'),
        ((21,), 0, 'CodingBat example'),
        ((22,), 2, 'CS110 extra'),
        ((25,), 8, 'CS110 extra'),
        ((-4,), 25, 'CS110 extra'),
    ]
    passed = 0
    print("\ndiff21 —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "diff21(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = diff21(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for diff21: {passed}/{len(cases)} passed")
    return passed, len(cases)


def parrot_trouble_test():
    """Run the 7 checks for parrot_trouble only."""
    cases = [
        ((True, 6), True, 'CodingBat example'),
        ((True, 7), False, 'CodingBat example'),
        ((False, 6), False, 'CodingBat example'),
        ((True, 20), False, 'CS110 extra'),
        ((True, 21), True, 'CS110 extra'),
        ((False, 23), False, 'CS110 extra'),
        ((True, 0), True, 'CS110 extra'),
    ]
    passed = 0
    print("\nparrot_trouble —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "parrot_trouble(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = parrot_trouble(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for parrot_trouble: {passed}/{len(cases)} passed")
    return passed, len(cases)


def makes10_test():
    """Run the 7 checks for makes10 only."""
    cases = [
        ((9, 10), True, 'CodingBat example'),
        ((9, 9), False, 'CodingBat example'),
        ((1, 9), True, 'CodingBat example'),
        ((10, 2), True, 'CS110 extra'),
        ((5, 5), True, 'CS110 extra'),
        ((0, 0), False, 'CS110 extra'),
        ((-3, 13), True, 'CS110 extra'),
    ]
    passed = 0
    print("\nmakes10 —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "makes10(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = makes10(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for makes10: {passed}/{len(cases)} passed")
    return passed, len(cases)


def near_hundred_test():
    """Run the 9 checks for near_hundred only."""
    cases = [
        ((93,), True, 'CodingBat example'),
        ((90,), True, 'CodingBat example'),
        ((89,), False, 'CodingBat example'),
        ((110,), True, 'CS110 extra'),
        ((111,), False, 'CS110 extra'),
        ((190,), True, 'CS110 extra'),
        ((200,), True, 'CS110 extra'),
        ((210,), True, 'CS110 extra'),
        ((211,), False, 'CS110 extra'),
    ]
    passed = 0
    print("\nnear_hundred —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "near_hundred(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = near_hundred(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for near_hundred: {passed}/{len(cases)} passed")
    return passed, len(cases)


def pos_neg_test():
    """Run the 8 checks for pos_neg only."""
    cases = [
        ((1, -1, False), True, 'CodingBat example'),
        ((-1, 1, False), True, 'CodingBat example'),
        ((-4, -5, True), True, 'CodingBat example'),
        ((-4, -5, False), False, 'CS110 extra'),
        ((-4, 5, True), False, 'CS110 extra'),
        ((0, 5, False), False, 'CS110 extra'),
        ((5, -5, True), False, 'CS110 extra'),
        ((-5, -5, True), True, 'CS110 extra'),
    ]
    passed = 0
    print("\npos_neg —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "pos_neg(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = pos_neg(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for pos_neg: {passed}/{len(cases)} passed")
    return passed, len(cases)


def not_string_test():
    """Run the 8 checks for not_string only."""
    cases = [
        (('candy',), 'not candy', 'CodingBat example'),
        (('x',), 'not x', 'CodingBat example'),
        (('not bad',), 'not bad', 'CodingBat example'),
        (('nothing',), 'nothing', 'CS110 extra'),
        (('',), 'not ', 'CS110 extra'),
        (('no',), 'not no', 'CS110 extra'),
        (('Not bad',), 'not Not bad', 'CS110 extra'),
        (('not',), 'not', 'CS110 extra'),
    ]
    passed = 0
    print("\nnot_string —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "not_string(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = not_string(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for not_string: {passed}/{len(cases)} passed")
    return passed, len(cases)


def missing_char_test():
    """Run the 7 checks for missing_char only."""
    cases = [
        (('kitten', 1), 'ktten', 'CodingBat example'),
        (('kitten', 0), 'itten', 'CodingBat example'),
        (('kitten', 4), 'kittn', 'CodingBat example'),
        (('a', 0), '', 'CS110 extra'),
        (('abc', 2), 'ab', 'CS110 extra'),
        (('abc', 1), 'ac', 'CS110 extra'),
        (('xyz', 0), 'yz', 'CS110 extra'),
    ]
    passed = 0
    print("\nmissing_char —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "missing_char(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = missing_char(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for missing_char: {passed}/{len(cases)} passed")
    return passed, len(cases)


def front_back_test():
    """Run the 7 checks for front_back only."""
    cases = [
        (('code',), 'eodc', 'CodingBat example'),
        (('a',), 'a', 'CodingBat example'),
        (('ab',), 'ba', 'CodingBat example'),
        (('',), '', 'CS110 extra'),
        (('hi',), 'ih', 'CS110 extra'),
        (('hello',), 'oellh', 'CS110 extra'),
        (('aba',), 'aba', 'CS110 extra'),
    ]
    passed = 0
    print("\nfront_back —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "front_back(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = front_back(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for front_back: {passed}/{len(cases)} passed")
    return passed, len(cases)


def front3_test():
    """Run the 7 checks for front3 only."""
    cases = [
        (('Java',), 'JavJavJav', 'CodingBat example'),
        (('Chocolate',), 'ChoChoCho', 'CodingBat example'),
        (('abc',), 'abcabcabc', 'CodingBat example'),
        (('',), '', 'CS110 extra'),
        (('a',), 'aaa', 'CS110 extra'),
        (('hi',), 'hihihi', 'CS110 extra'),
        (('abcd',), 'abcabcabc', 'CS110 extra'),
    ]
    passed = 0
    print("\nfront3 —", len(cases), "tests")
    for number, (args, expected, source) in enumerate(cases, start=1):
        call_text = "front3(" + ", ".join(repr(arg) for arg in args) + ")"
        try:
            actual = front3(*args)  # Call THIS problem's function.
            correct = (type(actual) is type(expected) and actual == expected)
            if correct:
                passed += 1
                print(f"  PASS {number:02d} [{source}] {call_text} -> {actual!r}")
            else:
                print(f"  FAIL {number:02d} [{source}] {call_text}: expected {expected!r}; got {actual!r}")
        except Exception as exc:
            print(f"  ERROR {number:02d} [{source}] {call_text}: {type(exc).__name__}: {exc}")
    print(f"  Result for front3: {passed}/{len(cases)} passed")
    return passed, len(cases)