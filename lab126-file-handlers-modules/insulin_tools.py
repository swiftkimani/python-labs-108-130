# Lab 126 - File Handlers and Modules
# AWS re/Start - Python Programming
# This is a module - it holds functions that other files can import.
# It does not run anything on its own.

weights = {
    "A": 71.0788,  "R": 156.1875, "N": 114.1038, "D": 115.0886,
    "C": 103.1388, "E": 129.1155, "Q": 128.1307, "G": 57.0519,
    "H": 137.1411, "I": 113.1594, "L": 113.1594, "K": 128.1741,
    "M": 131.1926, "F": 147.1766, "P": 97.1167,  "S": 87.0782,
    "T": 101.1051, "W": 186.2132, "Y": 163.1760, "V": 99.1326
}

WATER = 18.0153
HYDROGEN = 1.00794


def read_chains(filename):
    """Read the insulin chains from a file and return them as a list."""
    chains = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                chains.append(line)
    return chains


def count_residues(sequence):
    """Count how many times each amino acid appears."""
    counts = {}
    for residue in sequence:
        if residue in counts:
            counts[residue] = counts[residue] + 1
        else:
            counts[residue] = 1
    return counts


def molecular_weight(sequence, chains=1, bonds=0):
    """Calculate the molecular weight of a sequence in daltons."""
    total = 0
    for residue in sequence:
        total = total + weights[residue]
    total = total + (WATER * chains)
    total = total - (2 * HYDROGEN * bonds)
    return total


def find_residue(sequence, residue):
    """Return a list of the positions where a residue appears."""
    positions = []
    for position, letter in enumerate(sequence, 1):
        if letter == residue:
            positions.append(position)
    return positions


def save_report(filename, sequence, counts, weight):
    """Write the results out to a text file."""
    with open(filename, "w") as file:
        file.write("INSULIN ANALYSIS REPORT\n")
        file.write("=" * 30 + "\n\n")
        file.write("Sequence: " + sequence + "\n")
        file.write("Length: " + str(len(sequence)) + " residues\n")
        file.write("Molecular weight: " + str(round(weight, 2)) + " Da\n\n")
        file.write("Composition:\n")
        for residue in sorted(counts):
            file.write(residue + ": " + str(counts[residue]) + "\n")
