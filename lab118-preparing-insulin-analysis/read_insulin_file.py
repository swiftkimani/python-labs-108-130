# Lab 118 - Preparing to Analyze Insulin with Python
# Reading the sequence from a file instead of typing it in

filename = "insulin.txt"

# Read the file and store each chain
file = open(filename, "r")
lines = file.readlines()
file.close()

a_chain = lines[0].strip()
b_chain = lines[1].strip()

print("Read from", filename)
print("A chain:", a_chain, "(", len(a_chain), "residues )")
print("B chain:", b_chain, "(", len(b_chain), "residues )")

# The same thing using 'with', which closes the file automatically
print("\nUsing the with statement")
with open(filename, "r") as file:
    chains = []
    for line in file:
        chains.append(line.strip())

print("Chains read:", len(chains))
print("Total residues:", len(chains[0]) + len(chains[1]))
