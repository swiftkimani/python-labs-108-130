# Lab 122 - Calculating the Net Charge of Insulin Using Python Lists and Loops
# AWS re/Start - Python Programming

a_chain = "GIVEQCCTSICSLYQLENYCN"
b_chain = "FVNQHLCGSHLVEALYLVCGERGFFYTPKT"
insulin = a_chain + b_chain

# Amino acids that carry a charge at pH 7
positive = ["K", "R", "H"]     # basic - lysine, arginine, histidine
negative = ["D", "E"]          # acidic - aspartic acid, glutamic acid

# ----- METHOD 1: COUNT THE CHARGED RESIDUES -----
print("METHOD 1 - counting charged residues")
print("-" * 40)

# Build a list holding the charge of every residue
charges = []
for residue in insulin:
    if residue in positive:
        charges.append(1)
    elif residue in negative:
        charges.append(-1)
    else:
        charges.append(0)

print("Charges list has", len(charges), "entries")

# Count them up
positive_count = 0
negative_count = 0
for charge in charges:
    if charge > 0:
        positive_count = positive_count + 1
    elif charge < 0:
        negative_count = negative_count + 1

print("Positive residues:", positive_count)
print("Negative residues:", negative_count)

net = sum(charges)
print("Net charge =", net)

# Show which residues these were
print("\nCharged residues found")
for residue in positive + negative:
    count = insulin.count(residue)
    if count > 0:
        if residue in positive:
            sign = "+"
        else:
            sign = "-"
        print(f"{residue}: {count} residues, charge {sign}{count}")

# Show the charge at each position in each chain
print("\nCharge at each position")
for name, chain in [("A chain", a_chain), ("B chain", b_chain)]:
    print("\n" + name)
    for start in range(0, len(chain), 10):
        block = chain[start:start + 10]
        line1 = ""
        line2 = ""
        for residue in block:
            line1 = line1 + residue + " "
            if residue in positive:
                line2 = line2 + "+ "
            elif residue in negative:
                line2 = line2 + "- "
            else:
                line2 = line2 + ". "
        print(" ", line1)
        print(" ", line2)

# ----- METHOD 2: ALLOW FOR pH -----
# Counting treats histidine as a full +1, but at pH 7 histidine is barely
# charged at all. This method uses the pKa of each group instead.
print("\n\nMETHOD 2 - allowing for pH")
print("-" * 40)

pka = {
    "K": 10.53, "R": 12.48, "H": 6.00,     # basic
    "D": 3.65, "E": 4.25, "C": 8.18, "Y": 10.07   # acidic
}

ph = 7.0
n_terminus = 9.69    # the free amino group at the start of each chain
c_terminus = 2.34    # the free carboxyl group at the end of each chain
chains = 2

total_charge = 0.0

# The chain ends
total_charge = total_charge + chains * (1 / (1 + 10 ** (ph - n_terminus)))
total_charge = total_charge - chains * (1 / (1 + 10 ** (c_terminus - ph)))

# The side chains
for residue in pka:
    count = insulin.count(residue)
    if count == 0:
        continue

    if residue in positive:
        fraction = 1 / (1 + 10 ** (ph - pka[residue]))
        contribution = count * fraction
    else:
        fraction = 1 / (1 + 10 ** (pka[residue] - ph))
        contribution = -count * fraction

    total_charge = total_charge + contribution
    print(f"{residue}: {count} residues, {fraction * 100:5.1f}% ionised, charge {contribution:+.3f}")

print(f"\nNet charge at pH {ph} = {total_charge:.2f}")

# ----- COMPARING THE TWO -----
print("\n\nCOMPARING THE TWO METHODS")
print("-" * 40)
print("Counting method:  ", net)
print(f"Allowing for pH:   {total_charge:.2f}")
print("\nThe difference is histidine. Insulin has 2 histidines and counting")
print("treats each as +1, but at pH 7 histidine is only about 9% charged.")
print("Insulin's isoelectric point is 5.3, so above that pH it must be")
print("negative - which is what the second method shows.")
