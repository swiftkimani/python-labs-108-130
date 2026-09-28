# Lab 128 - System Administration with Python
# Running shell commands from Python

import subprocess

# Run a command and capture what it prints
print("Running: echo Hello from the shell")
result = subprocess.run(["echo", "Hello from the shell"],
                        capture_output=True, text=True)

print("Return code:", result.returncode)
print("Output:", result.stdout.strip())

# A return code of 0 means the command worked
print("\nChecking return codes")
for command in [["true"], ["false"]]:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(command[0], "-> success")
    else:
        print(command[0], "-> failed with code", result.returncode)

# Capturing output and using it
print("\nListing files in the current directory")
result = subprocess.run(["ls", "-1"], capture_output=True, text=True)
files = result.stdout.split("\n")
files = [f for f in files if f != ""]
print("Found", len(files), "files:", files)

# Handling a command that fails
print("\nRunning a command that fails")
result = subprocess.run(["ls", "/does/not/exist"], capture_output=True, text=True)
if result.returncode != 0:
    print("Command failed:", result.stderr.strip())

# IMPORTANT: always pass the command as a list.
# Using shell=True with text from a user is a security risk, because
# someone could type "file.txt; rm -rf /" and the shell would run both.
print("\nSafe:   subprocess.run(['cat', filename])")
print("Unsafe: subprocess.run('cat ' + filename, shell=True)")
