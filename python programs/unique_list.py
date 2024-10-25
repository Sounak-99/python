def unique_list():
    x = [1, 2, 3, 3, 3, 3, 4, 5]
    print("Before unique list:- ", x)
    unique = list(set(x))
    print("After unique list:- ", unique)

unique_list()