def hamming_neighbors(sequence):
    neighbors = []
    bases = ['A', 'C', 'G', 'T']

    for i in range(len(sequence)):
        for base in bases:
            if sequence[i] != base:
                neighbor = sequence[:i] + base + sequence[i + 1:]
                neighbors.append(neighbor)

    return neighbors


# Example usage
sequence = "AAACGCAATAGCAGATACC"
result = hamming_neighbors(sequence)
print(result)
