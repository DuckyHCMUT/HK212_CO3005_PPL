def flatten(lst):
    return [i for sublist in lst for i in sublist]

print(flatten([[1,2,3],[4,5],[6,7]]))