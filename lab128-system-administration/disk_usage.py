# Lab 128 - System Administration with Python
# Walk through a directory and report on the files in it

import os
import sys


def get_size_text(size):
    """Turn a size in bytes into something readable."""
    if size < 1024:
        return str(size) + " B"
    elif size < 1024 * 1024:
        return str(round(size / 1024, 1)) + " KB"
    elif size < 1024 * 1024 * 1024:
        return str(round(size / 1024 / 1024, 1)) + " MB"
    else:
        return str(round(size / 1024 / 1024 / 1024, 1)) + " GB"


# Take the directory from the command line, or use the current one
if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    directory = "."

if not os.path.isdir(directory):
    print(directory, "is not a directory")
    sys.exit(1)

print("Scanning:", os.path.abspath(directory))
print("=" * 50)

file_count = 0
dir_count = 0
total_size = 0
file_list = []

# os.walk goes through every directory below the one we give it
for current_dir, subdirs, filenames in os.walk(directory):
    dir_count = dir_count + len(subdirs)

    for filename in filenames:
        path = os.path.join(current_dir, filename)
        try:
            size = os.path.getsize(path)
        except OSError:
            continue

        file_count = file_count + 1
        total_size = total_size + size
        file_list.append((size, path))

print("\nFiles:", file_count)
print("Directories:", dir_count)
print("Total size:", get_size_text(total_size))

if file_count > 0:
    print("Average file size:", get_size_text(total_size / file_count))

    # Sort by size, largest first
    file_list.sort(reverse=True)

    print("\nLargest 5 files")
    print("-" * 50)
    for size, path in file_list[:5]:
        print(f"{get_size_text(size):>10}  {path}")

    # Group by file extension
    print("\nBy file extension")
    print("-" * 50)
    extensions = {}
    for size, path in file_list:
        name, ext = os.path.splitext(path)
        if ext == "":
            ext = "(none)"
        if ext in extensions:
            extensions[ext] = extensions[ext] + size
        else:
            extensions[ext] = size

    for ext in sorted(extensions, key=extensions.get, reverse=True)[:8]:
        print(f"{ext:<12} {get_size_text(extensions[ext]):>10}")
