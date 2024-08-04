def f_dict(str_dict):
    list_dict = list(str_dict.items())
    return list_dict
def f_set(str_set):
    list_set = list(str_set)
    return list_set
def calculate_structure_sum(structure):
    l = len(structure)
    sm_structure = 0
    for i in range(l):
        if isinstance(structure[i], int):
            sm_structure = sm_structure + structure[i]
        elif isinstance(structure[i], str):
            sm_structure = sm_structure + len(structure[i])
        elif isinstance(structure[i], dict):
            sm_structure = sm_structure + calculate_structure_sum(f_dict(structure[i]))
        elif isinstance(structure[i], set):
            sm_structure = sm_structure + calculate_structure_sum(f_set(structure[i]))
        else:
            sm_structure = sm_structure + calculate_structure_sum((structure[i]))

    return sm_structure



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)



