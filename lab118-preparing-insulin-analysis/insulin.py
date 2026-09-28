# Lab 118 - Preparing to Analyze Insulin with Python
# AWS re/Start - Python Programming

# Human insulin has two chains joined by disulfide bonds
a_chain = "GIVEQCCTSICSLYQLENYCN"
b_chain = "FVNQHLCGSHLVEALYLVCGERGFFYTPKT"

print("A chain:", a_chain)
print("B chain:", b_chain)

print("\nA chain length:", len(a_chain))
print("B chain length:", len(b_chain))

# Both chains together
insulin = a_chain + b_chain
print("\nWhole molecule:", insulin)
print("Total residues:", len(insulin))

# The valid amino acid codes
valid_codes = "ACDEFGHIKLMNPQRSTVWY"

# Check every residue is a real amino acid code
print("\nChecking the sequence is valid")
invalid = []
for position, residue in enumerate(insulin, 1):
    if residue not in valid_codes:
        invalid.append((position, residue))

if len(invalid) == 0:
    print("All", len(insulin), "residues are valid amino acid codes")
else:
    print("Found invalid residues:", invalid)

# Count how many times each residue appears
print("\nAmino acid composition")
counts = {}
for residue in insulin:
    if residue in counts:
        counts[residue] = counts[residue] + 1
    else:
        counts[residue] = 1

for residue in sorted(counts):
    print(residue, ":", counts[residue])

print("\nDifferent amino acids used:", len(counts), "out of 20")

# Find the cysteines - these form the disulfide bonds
print("\nCysteine positions")
a_cysteines = []
for position, residue in enumerate(a_chain, 1):
    if residue == "C":
        a_cysteines.append(position)

b_cysteines = []
for position, residue in enumerate(b_chain, 1):
    if residue == "C":
        b_cysteines.append(position)

print("A chain:", a_cysteines)
print("B chain:", b_cysteines)
print("Total cysteines:", len(a_cysteines) + len(b_cysteines))
print("These form 3 disulfide bonds: A6-A11, A7-B7, A20-B19")
