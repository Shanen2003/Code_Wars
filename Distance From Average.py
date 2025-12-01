def distances_from_average(test_list):
    mean = sum(test_list) / len(test_list)
    std = list(map(lambda x: round(mean - x, 2), test_list))
    return std

distances_from_average([5,6,7,90])
