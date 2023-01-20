s1, s2 = input().split(' ')

print(s1[:len(s1)-2] + s2[len(s2)-2:] + ' ' + s2[:len(s2)-2] + s1[len(s1)-2:])
