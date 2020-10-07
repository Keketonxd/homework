lis = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([lis[el] for el in range(1, len(lis)) if lis[el - 1] < lis[el]])
# слишком замысловато или норм?
