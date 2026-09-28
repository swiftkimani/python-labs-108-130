# Lab 120 - String Sequence and Numeric Weight of Insulin
# AWS re/Start - Python Programming

a_chain = "GIVEQCCTSICSLYQLENYCN"
b_chain = "FVNQHLCGSHLVEALYLVCGERGFFYTPKT"
insulin = a_chain + b_chain

# Average mass each amino acid contributes to a chain, in daltons
weights = {
    "A": 71.0788,  "R": 156.1875, "N": 114.1038, "D": 115.0886,
    "C": 103.1388, "E": 129.1155, "Q": 128.1307, "G": 57.0519,
    "H": 137.1411, "I": 113.1594, "L": 113.1594, "K": 128.1741,
    "M": 131.1926, "F": 147.1766, "P": 97.1167,  "S": 87.0782,
    "T": 101.1051, "W": 186.2132, "Y": 163.1760, "V": 99.1326
}

water = 18.0153      # one water molecule stays on each chain
hydrogen = 1.00794   # each disulfide bond removes two hydrogens

# ----- STRING OPERATIONS -----
print("STRING OPERATIONS")
print("Sequence:", insulin)
print("Length:", len(insulin))
print("First residue:", insulin[0])
print("Last residue:", insulin[-1])
print("First 10:", insulin[:10])
print("Last 10:", insulin[-10:])
print("Reversed:", insulin[::-1])

print("\nCounting specific residues")
print("Cysteine (C):", insulin.count("C"))
print("Leucine (L):", insulin.count("L"))
print("Glutamic acid (E):", insulin.count("E"))

print("\nSearching")
print("Position of 'CC':", insulin.find("CC"))
print("Does it contain 'W'?", "W" in insulin)

# Print the sequence in blocks of 10, the way databases show it
print("\nSequence in blocks of 10")
for start in range(0, len(insulin), 10):
    block = insulin[start:start + 10]
    print(f"{start + 1:3}  {block}")

# ----- NUMERIC WEIGHT -----
print("\nMOLECULAR WEIGHT")

# Step 1 - add up the weight of every residue
total = 0
for residue in insulin:
    total = total + weights[residue]
print(f"1. Sum of {len(insulin)} residue weights: {total:.4f} Da")

# Step 2 - add one water molecule for each chain
total = total + (water * 2)
print(f"2. Plus 2 water molecules:           {total:.4f} Da")

# Step 3 - subtract two hydrogens for each disulfide bond
total = total - (2 * hydrogen * 3)
print(f"3. Minus 6 hydrogens (3 S-S bonds):  {total:.4f} Da")

print(f"\nMolecular weight of insulin = {total:.2f} Da")
print("Published value             = 5807.57 Da")
print(f"Difference                  = {total - 5807.57:.4f} Da")

# Weight of each chain on its own
print("\nWeight of each chain")
for name, chain in [("A chain", a_chain), ("B chain", b_chain)]:
    chain_total = 0
    for residue in chain:
        chain_total = chain_total + weights[residue]
    chain_total = chain_total + water
    print(f"{name}: {len(chain)} residues, {chain_total:.2f} Da")

# Average weight per residue - should be around 110 for a normal protein
average = total / len(insulin)
print(f"\nAverage weight per residue: {average:.2f} Da")
