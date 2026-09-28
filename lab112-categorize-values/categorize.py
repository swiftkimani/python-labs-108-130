# Lab 112 - Categorize Values
# AWS re/Start - Python Programming
# Work out the data type of each value and group them

values = [
    42,
    3.14,
    "hello",
    True,
    [1, 2, 3],
    (4, 5),
    {"a": 1},
    {7, 8},
    None,
    0,
    "",
    False
]


def get_category(value):
    """Return the category name for a value."""
    # bool must be checked before int, because True is also an int
    if value is None:
        return "NoneType"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, tuple):
        return "tuple"
    elif isinstance(value, dict):
        return "dictionary"
    elif isinstance(value, set):
        return "set"
    else:
        return "unknown"


# Show each value with its category
print("Categorizing each value")
print("-" * 45)
for value in values:
    category = get_category(value)
    print(f"{str(value):<12} {category:<12} {str(type(value)):<20}")

# Group the values by category
print("\nGrouped by category")
print("-" * 45)
groups = {}
for value in values:
    category = get_category(value)
    if category not in groups:
        groups[category] = []
    groups[category].append(value)

for category in sorted(groups):
    print(f"{category:<12} {groups[category]}")

# Count how many of each category
print("\nCount of each category")
print("-" * 45)
for category in sorted(groups):
    print(f"{category:<12} {len(groups[category])}")

# Separate truthy from falsy values
print("\nTruthy and falsy values")
print("-" * 45)
truthy = []
falsy = []
for value in values:
    if value:
        truthy.append(value)
    else:
        falsy.append(value)

print("Truthy:", truthy)
print("Falsy: ", falsy)

# Note: isinstance(True, int) is True because bool is a subclass of int
print("\nisinstance(True, int) =", isinstance(True, int))
