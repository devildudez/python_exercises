def str_count(strng, letter) -> int:
    sm = 0
    for i in strng:
        if i == letter:
            sm += 1
    return sm





print(str_count('hello world','l'))