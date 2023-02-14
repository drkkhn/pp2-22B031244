s = "this is wonderful moment of time to be alive"

list1 = s.split(" ")
even_list = [x for x in list1 if len(x) % 2 == 0]
odd_list = [x for x in list1 if len(x) % 2 == 1]
print(even_list)
print(odd_list)
