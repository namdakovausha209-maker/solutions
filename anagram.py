def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_split = list(s2)
    for c in s1:
        if c not in s2_split:
            return False
        else:
            s2_split.remove(c)
    return True




if __name__ == "__main__":
    print(is_anagram("hello", "world"))

    