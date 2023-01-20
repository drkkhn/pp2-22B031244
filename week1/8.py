s1, s2 = input().split(' ')

set1 = { x for x in s1 }
set2 = { x for x in s2 }

print(len(set1.intersection(set2)))
