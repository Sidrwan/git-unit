def get_summ(one, two, delimiter='&'):
    return one + delimiter + two

result = get_summ('learn', 'python', '//')
print(result[0])