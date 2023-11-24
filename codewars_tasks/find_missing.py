list = [1, 1, 1, 2, 1, 1, 1]

def find_missing(sequence):
    difference = None
    list_of_difference = []

    for index in range(0, len(sequence)):
        last_index = len(sequence) - 1
        if index != len(sequence) - 1 :
            raz = sequence[index + 1] - sequence[index]
            list_of_difference.append(raz)

    print(list_of_difference)
    difference = min(list_of_difference)
    find_index = list_of_difference.index(max(list_of_difference))
    print(difference, find_index)
    return sequence[find_index] + difference

    

print(find_missing(list))