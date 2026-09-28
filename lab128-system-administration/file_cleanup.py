# Lab 128 - System Administration with Python
# Find old files. This only LISTS them - it does not delete anything
# unless you pass --delete, and it asks first.

import os
import sys
import time

# Read the arguments
if len(sys.argv) < 2:
    print("Usage: python3 file_cleanup.py <directory> [days] [--delete]")
    print("Example: python3 file_cleanup.py /tmp 30")
    sys.exit(1)

directory = sys.argv[1]

days = 30
if len(sys.argv) > 2 and sys.argv[2].isdigit():
    days = int(sys.argv[2])

delete_mode = "--delete" in sys.argv

if not os.path.isdir(directory):
    print(directory, "is not a directory")
    sys.exit(1)

# Do not let this run on an important directory by mistake
protected = ["/", "/home", "/usr", "/etc", "/var", "/Users"]
if os.path.abspath(directory) in protected:
    print("Refusing to run on the system directory", directory)
    sys.exit(1)

print("Directory:", os.path.abspath(directory))
print("Looking for files older than", days, "days")

if delete_mode:
    print("Mode: DELETE")
else:
    print("Mode: list only (add --delete to remove them)")
print("=" * 50)

# Anything modified before this time counts as old
cutoff = time.time() - (days * 24 * 60 * 60)

old_files = []
for current_dir, subdirs, filenames in os.walk(directory):
    for filename in filenames:
        path = os.path.join(current_dir, filename)
        try:
            modified = os.path.getmtime(path)
            size = os.path.getsize(path)
        except OSError:
            continue

        if modified < cutoff:
            old_files.append((path, modified, size))

if len(old_files) == 0:
    print("\nNo files older than", days, "days were found")
    sys.exit(0)

total_size = 0
print()
for path, modified, size in old_files[:20]:
    age = int((time.time() - modified) / 86400)
    date = time.strftime("%Y-%m-%d", time.localtime(modified))
    print(f"{date}  {age:>5} days  {size:>10} B  {path}")
    total_size = total_size + size

if len(old_files) > 20:
    print("... and", len(old_files) - 20, "more")

print("\nFound", len(old_files), "old files")

if not delete_mode:
    print("Nothing was deleted. Run again with --delete to remove them.")
    sys.exit(0)

# Ask before deleting anything
answer = input("\nDelete these files? Type yes to confirm: ")
if answer.lower() != "yes":
    print("Cancelled. Nothing was deleted.")
    sys.exit(0)

deleted = 0
for path, modified, size in old_files:
    try:
        os.remove(path)
        deleted = deleted + 1
    except OSError as error:
        print("Could not delete", path, "-", error)

print("Deleted", deleted, "files")
