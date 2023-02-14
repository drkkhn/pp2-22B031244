arr = [ 100, 'Astana', True, 1, 'KBTU', 'Almaty', False]

dictionary = {
    'only_ints': [],
    'list_of_string': [],
    'float_nums': [],
    'array_of_bools': []
}
for x in arr:
    if type(x) == int:
        dictionary['only_ints'].append(x)
    if isinstance(x, str):
        dictionary['list_of_string'].append(x)
    if isinstance(x, float):
        dictionary['float_nums'].append(x)
    if isinstance(x, bool): 
        dictionary['array_of_bools'].append(x)

for x in dictionary.values():
    print(x)
