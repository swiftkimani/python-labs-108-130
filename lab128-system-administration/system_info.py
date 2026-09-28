# Lab 128 - System Administration with Python
# AWS re/Start - Python Programming
# Collect information about the system

import os
import platform
import shutil
import socket
import sys
import getpass

print("SYSTEM INFORMATION")
print("=" * 40)

# Python
print("\nPython")
print("Version:", platform.python_version())
print("Location:", sys.executable)

# Operating system
print("\nOperating system")
print("System:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

# Host and user
print("\nHost and user")
print("Hostname:", socket.gethostname())
print("Username:", getpass.getuser())
print("Home directory:", os.path.expanduser("~"))
print("Current directory:", os.getcwd())
print("Process ID:", os.getpid())
print("CPU cores:", os.cpu_count())

# Disk usage
print("\nDisk usage")
total, used, free = shutil.disk_usage("/")

gb = 1024 * 1024 * 1024
print("Total:", round(total / gb, 1), "GB")
print("Used: ", round(used / gb, 1), "GB")
print("Free: ", round(free / gb, 1), "GB")

percent = used / total * 100
print("Percent used:", round(percent, 1), "%")

if percent > 90:
    print("WARNING: disk is over 90% full")
else:
    print("Disk space is OK")

# Environment variables
print("\nSome environment variables")
for name in ["USER", "HOME", "SHELL", "LANG"]:
    value = os.environ.get(name)
    if value:
        print(f"{name}: {value}")

print("\nTotal environment variables:", len(os.environ))
