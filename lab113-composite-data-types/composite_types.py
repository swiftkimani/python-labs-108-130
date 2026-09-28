# Lab 113 - Composite Data Types
# AWS re/Start - Python Programming
# Working with nested data structures

# A list of dictionaries - the usual shape for a set of records
students = [
    {"name": "Benard", "cohort": "KENAI52", "scores": [88, 92, 79]},
    {"name": "Asha", "cohort": "KENAI52", "scores": [95, 91, 98]},
    {"name": "Mwangi", "cohort": "KENAI51", "scores": [70, 65, 82]}
]

print("All students")
for student in students:
    print(student["name"], "-", student["cohort"], "-", student["scores"])

# Reaching a value inside the nested structure
print("\nFirst student's first score:", students[0]["scores"][0])
print("Second student's name:", students[1]["name"])

# Calculating an average from a nested list
print("\nAverages")
for student in students:
    scores = student["scores"]
    average = sum(scores) / len(scores)
    print(f"{student['name']}: {average:.1f}")

# A dictionary of lists
print("\nDictionary of lists")
cohorts = {
    "KENAI52": ["Benard", "Asha"],
    "KENAI51": ["Mwangi", "Fatuma"]
}

for cohort, names in cohorts.items():
    print(cohort, "has", len(names), "students:", names)

# A dictionary containing dictionaries
print("\nNested dictionary")
protein = {
    "name": "Insulin",
    "chains": {
        "A": {"sequence": "GIVEQCCTSICSLYQLENYCN", "length": 21},
        "B": {"sequence": "FVNQHLCGSHLVEALYLVCGERGFFYTPKT", "length": 30}
    }
}

print("Protein name:", protein["name"])
for chain_id, chain in protein["chains"].items():
    print(f"Chain {chain_id}: {chain['length']} residues")

# Filtering records
print("\nStudents in KENAI52")
kenai52 = []
for student in students:
    if student["cohort"] == "KENAI52":
        kenai52.append(student["name"])
print(kenai52)

# Sorting records by a value inside them
print("\nSorted by highest average")
def get_average(student):
    return sum(student["scores"]) / len(student["scores"])

ranked = sorted(students, key=get_average, reverse=True)
for student in ranked:
    print(f"{student['name']}: {get_average(student):.1f}")

# A list of tuples
print("\nList of tuples")
pairs = [("A", 21), ("B", 30)]
for chain, length in pairs:
    print("Chain", chain, "has", length, "residues")
