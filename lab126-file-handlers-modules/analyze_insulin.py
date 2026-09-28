# Lab 126 - File Handlers and Modules
# AWS re/Start - Python Programming
# This program imports insulin_tools and uses it to analyse the data

import csv
import os

import insulin_tools

# ----- READING A FILE -----
print("Reading insulin.txt")
chains = insulin_tools.read_chains("insulin.txt")

a_chain = chains[0]
b_chain = chains[1]
insulin = a_chain + b_chain

print("A chain:", len(a_chain), "residues")
print("B chain:", len(b_chain), "residues")
print("Total:", len(insulin), "residues")

# ----- USING THE MODULE'S FUNCTIONS -----
print("\nAnalysing the sequence")
counts = insulin_tools.count_residues(insulin)
weight = insulin_tools.molecular_weight(insulin, chains=2, bonds=3)

print("Molecular weight:", round(weight, 2), "Da")
print("Different amino acids:", len(counts))
print("Cysteine positions in A chain:", insulin_tools.find_residue(a_chain, "C"))
print("Cysteine positions in B chain:", insulin_tools.find_residue(b_chain, "C"))

# ----- WRITING A TEXT FILE -----
print("\nWriting insulin_report.txt")
insulin_tools.save_report("insulin_report.txt", insulin, counts, weight)
print("File size:", os.path.getsize("insulin_report.txt"), "bytes")

# ----- WRITING A CSV FILE -----
print("\nWriting composition.csv")
with open("composition.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["residue", "count", "percent"])
    for residue in sorted(counts):
        percent = round(counts[residue] / len(insulin) * 100, 1)
        writer.writerow([residue, counts[residue], percent])

print("File size:", os.path.getsize("composition.csv"), "bytes")

# ----- READING THE CSV BACK -----
print("\nReading composition.csv back")
with open("composition.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print("Rows read:", len(rows))
print("First row:", rows[0])

# ----- APPENDING TO A FILE -----
print("\nAppending to the report")
with open("insulin_report.txt", "a") as file:
    file.write("\nReport complete.\n")

# ----- READING THE REPORT BACK -----
print("\nThe report file contains:")
print("-" * 30)
with open("insulin_report.txt", "r") as file:
    print(file.read())
