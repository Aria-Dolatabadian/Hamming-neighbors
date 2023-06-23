import csv

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

# Export the results as a CSV file
csv_filename = "hamming_neighbors.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Original Sequence", "Hamming Neighbor"])
    for neighbor in result:
        writer.writerow([sequence, neighbor])

print(f"Results exported to {csv_filename}")
