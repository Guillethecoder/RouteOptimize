array = ['a', 'b', 'c', 'd', 'e']
def CargoPartition(array):
    n = len(array)
    final_list_solution = []

    for partition_index in range(2 ** (n-1)):

        # current partition, e.g., [['a', 'b'], ['c', 'd', 'e']]
        partition = []

        # used to accumulate the subsets, e.g., ['a', 'b']
        subset = []

        for position in range(n):

            subset.append(array[position])

            # check whether to "break off" a new subset
            if 1 << position & partition_index or position == n-1:
                partition.append(subset)
                subset = []

        final_list_solution.append(partition)
    return final_list_solution

print(CargoPartition(array))
