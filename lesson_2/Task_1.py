def is_cyclic_shift_efficient(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


print(is_cyclic_shift_efficient("abcde", "cdeab"))  # True
print(is_cyclic_shift_efficient("abc", "cdeab"))  # False
print(is_cyclic_shift_efficient("asdf", "qwerty"))  # True
