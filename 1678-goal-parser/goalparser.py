def parse(s):
    s = s.replace("()", "o")
    s = s.replace("(al)", "al")
    return s

print(parse("(al)G(al)()()G"))