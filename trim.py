def trim(s):
    if s=='':
        return s
    elif s[0]==' ':
        return trim(s[1:])
    elif s[-1]==' ':
        return trim(s[:-1])
    return s
print(trim('    hello   '))