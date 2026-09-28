# Knowledge Check study guide - Python Programming module

Condensed from labs 108-130. Organised by the KC each section feeds, with the
traps that actually appear in the questions marked **⚠**.

---

## KC: Introduction to Programming (after lab 116)

- Python is **interpreted**, not compiled. The interpreter reads the file top to bottom.
- Indentation defines blocks. Four spaces. **⚠ Mixing tabs and spaces raises `TabError`.**
- `#` starts a comment. A string literal on the first line of a file, function or
  class is a **docstring**, readable at runtime as `__doc__`.
- A `.py` file is a **module**; running it makes it a **script**.
- `if __name__ == "__main__":` - code under this runs only when the file is executed
  directly, never when it is imported.

**Git**
- Three areas: working directory → (`git add`) → staging area → (`git commit`) → repository.
- `git status` tells you where everything is. `git log --oneline` shows history.
- A commit is identified by a SHA hash. `HEAD` points at the current commit.
- A branch is just a movable pointer. `git checkout -b name` creates and switches.
- **⚠ `.gitignore` only affects UNTRACKED files.** Already-committed files keep being
  tracked until `git rm --cached`.
- `git pull` = `git fetch` + `git merge`.

---

## KC: Introduction to Python (after labs 118)

**Types**
- `int`, `float`, `complex`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `NoneType`.
- **⚠ `bool` is a subclass of `int`.** `isinstance(True, int)` is `True`, `True + True` is `2`.
  When classifying types, test `bool` **before** `int`.
- `type(x)` is the exact class; `isinstance(x, C)` accepts subclasses.
- **⚠ Test `None` with `is None`, never `== None`.**

**Mutability**
| Immutable | Mutable |
|---|---|
| `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` | `list`, `dict`, `set`, `bytearray` |

- **⚠ Strings are immutable.** `s.upper()` returns a new string; `s[0] = "X"` is a `TypeError`.
- **⚠ Assignment copies a reference, not the data.** `b = a` then `b.append(1)` changes `a`.
  Use `a.copy()` / `list(a)`, or `copy.deepcopy()` for nested structures.

**Truthiness**
- Falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`.
- **⚠ `"0"`, `"False"` and `[0]` are TRUTHY** - only emptiness is falsy.

**Numbers**
- `/` always returns a float. `//` floors, `%` is the remainder, `**` is power.
- **⚠ `-7 // 2` is `-4`, not `-3`** - floor division rounds down, not toward zero.
- **⚠ `int(3.9)` is `3`** - it truncates. `round(3.9)` is `4`.
- **⚠ `round()` uses banker's rounding: `round(2.5)` is `2`, `round(3.5)` is `4`.**
- **⚠ `0.1 + 0.2 != 0.3`.** Compare floats with a tolerance.

**Strings**
- Zero-indexed; negative indexes count from the end.
- Slicing `s[start:stop:step]`, **stop is exclusive**. `s[::-1]` reverses.
- **⚠ Slicing out of range returns `""`; indexing out of range raises `IndexError`.**
- `split()` with no argument splits on any whitespace run and drops empties.
- Build strings with `"".join(parts)`, not `+=` in a loop.

**Collections**
| | Ordered | Mutable | Duplicates | Lookup by |
|---|---|---|---|---|
| `list` | yes | yes | yes | index |
| `tuple` | yes | **no** | yes | index |
| `dict` | yes (3.7+) | yes | keys unique | **key** |
| `set` | **no** | yes | **no** | membership |

- **⚠ A one-item tuple needs the comma: `(1,)`. `(1)` is the integer 1.**
- **⚠ `list.sort()` sorts in place and returns `None`.** `my_list = my_list.sort()`
  sets your variable to `None`. Use `sorted()` for a new list.
- `append(x)` adds one item; `extend([x, y])` adds each item.
- **⚠ `d[missing]` raises `KeyError`; `d.get(missing)` returns `None`.**
- Dict keys must be hashable - a tuple can be a key, a list cannot.
- `for key in my_dict:` iterates the **keys**. Use `.items()` for pairs.

---

## KC: Python Basics (after lab 120)

- f-strings: `f"{value:.2f}"`, `f"{value:>10}"`, `f"{value:,}"`, `f"{value:.1%}"`.
- Alignment: `<` left, `>` right, `^` centre.
- **⚠ In an old-style `%` format string, a literal percent must be escaped as `%%`.**
- The accumulator pattern: initialise outside the loop, update inside.
  ```python
  total = 0
  for n in numbers:
      total += n
  ```
- Counting with a dict: `counts[key] = counts.get(key, 0) + 1`.
- `sum(expr for x in items)` - a generator expression, no intermediate list.

---

## KC: Flow Control (after lab 122)

- `elif` chains stop at the **first** true branch - order matters, most specific first.
- **⚠ `and`/`or` return an OPERAND, not a boolean:** `"a" or "b"` is `"a"`, `"" or "b"` is `"b"`.
- **Short-circuiting:** `if items and items[0]` is safe on an empty list.
- Chained comparisons work: `0 <= score <= 100`.
- Ternary: `value_if_true if condition else value_if_false`.

**Loops**
- `for` iterates a sequence; `while` repeats while a condition holds.
- **⚠ `range(stop)` is exclusive:** `range(5)` gives `0,1,2,3,4`.
- `range(start, stop, step)`; `range(10, 0, -1)` counts down.
- Use `enumerate(items)` for index+value, `zip(a, b)` for two sequences.
- **⚠ `zip` stops at the shortest input.**
- `break` leaves the loop, `continue` skips to the next pass.
- **⚠ A loop's `else` block runs only if the loop finished WITHOUT `break`.**
- **⚠ Never remove items from a list while iterating it** - items get skipped.
  Build a new list instead.
- **⚠ `break` only exits the innermost loop.**

---

## KC: Functions (after lab 124)

- `def name(parameters):` defines; `name(arguments)` calls.
- **⚠ A function with no `return` returns `None`.** This is the #1 source of
  "why is my value None?".
- Positional arguments match by order, keyword arguments by name.
  **⚠ Keyword arguments must come after positional ones.**
- **⚠ Default values are evaluated ONCE, at definition time.** Never use a mutable
  default:
  ```python
  def f(items=[]):      # WRONG - the list is shared between calls
  def f(items=None):    # RIGHT
      if items is None:
          items = []
  ```
- `*args` collects extra positional arguments into a **tuple**;
  `**kwargs` collects extra keyword arguments into a **dict**.
- `return a, b` returns a **tuple**; the caller can unpack it.
- **Scope (LEGB):** Local → Enclosing → Global → Built-in.
  Assigning inside a function creates a **local**. Use `global` / `nonlocal` to rebind.
- **⚠ Arguments are passed by object reference.** Rebinding a parameter does not
  affect the caller; **mutating** it does.
- Functions are objects: store them in dicts, pass them to `map()`/`sorted(key=...)`.

---

## KC: Modules and Libraries (after lab 126)

- `import module` / `from module import name` / `import module as alias`.
- **⚠ Avoid `from module import *`** - it hides where names came from and can
  silently overwrite your own.
- A module's body runs **once**, on first import; after that it is cached in `sys.modules`.
- `sys.path` is the search order; entry 0 is the script's own directory.
- `__name__` is `"__main__"` when run directly, the module name when imported.

**Files**
- **⚠ Always use `with open(...) as f:`** - it closes the file even on an exception.
- Modes: `r` read, `w` write (**truncates!**), `a` append, `x` create-or-fail,
  `r+` read/write. Add `b` for binary.
- `read()` whole file, `readline()` one line, **iterating the file object** streams
  it (best for large files).
- **⚠ Lines keep their `\n`** - use `.strip()`.
- Always pass `encoding="utf-8"`.
- **⚠ Use the `csv` module, not `line.split(",")`** - split breaks on quoted commas.
- Common exceptions: `FileNotFoundError`, `PermissionError`, `IsADirectoryError`.

**Useful standard library**
`math` `random` `datetime` `os` `sys` `json` `csv` `collections` (`Counter`,
`defaultdict`) `statistics` `pathlib` `shutil` `subprocess` `argparse` `logging` `re` `pdb`

---

## KC: Python for System Administration (after lab 128)

- `os` - environment, process, paths. `platform` - OS details.
  `shutil` - file operations and `disk_usage()`. `subprocess` - run commands.
- `os.walk(path)` yields `(current_dir, subdirs, files)` for each directory below `path`.
  **⚠ Edit `subdirs` in place to stop it descending** into a directory.
- **⚠ `subprocess.run(["ls", "-l"])` with a LIST is safe. `shell=True` with an
  f-string is a shell-injection vulnerability.** This is a favourite exam question.
- `capture_output=True, text=True` gives `.stdout`, `.stderr`, `.returncode`.
  `check=True` raises `CalledProcessError` on failure.
- **⚠ Exit status 0 means success; non-zero means failure.** `sys.exit(0)`.
- `argparse` gives `--help`, type conversion and validation for free.
- `logging` over `print()` for unattended scripts. Levels, lowest to highest:
  **DEBUG → INFO → WARNING → ERROR → CRITICAL**. Setting a level shows that level
  and above.
- Prefer a Python module over shelling out: `shutil.disk_usage()` over `df`,
  `shutil.copy2()` over `cp`, `os.walk()` over `find`.

---

## KC: Debugging and Testing (after labs 129, 130)

- **Breakpoint** = pause execution. **Watch** = track a value as it changes.
- **⚠ Step OVER (`next`)** runs a call without entering it.
  **Step INTO (`step`)** enters it. **Step OUT (`return`)** finishes the current function.
- Start pdb: `python3 -m pdb script.py`, or `breakpoint()` in the code (3.7+),
  or `import pdb; pdb.set_trace()`.
- Commands: `l` list, `n` next, `s` step, `c` continue, `p expr` print, `a` args,
  `w` where (call stack), `b N` breakpoint, `q` quit. ENTER repeats the last command.
- **⚠ In pdb, `print x` is Python 2 syntax and is a SyntaxError. Use `p x`.**
- **⚠ Read a traceback BOTTOM-UP.** The last line is the error; the frame above it
  is where it happened.
- `assert condition, "message"` documents an assumption.
  **⚠ Assertions are disabled by `python -O`** - never use them to validate user
  input or enforce security.
- **⚠ Never write a bare `except:`** - it swallows `KeyboardInterrupt` and `SystemExit`.

**Exception → usual cause**
| Exception | Usual cause |
|---|---|
| `TypeError` | Wrong type - often `str` + `int`, or calling something that is `None` |
| `NameError` | Misspelled or undefined name |
| `IndexError` | Past the end of a sequence - check your `range()` |
| `KeyError` | Missing dict key - use `.get()` |
| `AttributeError` | No such method, often because the object is `None` |
| `ValueError` | Right type, impossible value - `int("abc")` |
| `ZeroDivisionError` | A counter that was never incremented |

**Method**
1. Reproduce it reliably.
2. Minimise the input.
3. Bisect the code - breakpoint halfway, is the state already wrong?
4. Check the assumption you were most sure about.
5. Fix **one** bug at a time and re-run.
6. Write a failing test first; the same test passing proves the fix.

**⚠ The big one: a program that runs is not a program that works.** Crashes are
easy - Python tells you where. The dangerous bugs run happily and return the wrong
answer, and only a test that knows the right answer will catch them.

---

## Quick self-check

Answers at the bottom. No peeking.

1. What does `list.sort()` return?
2. Is `isinstance(True, int)` `True` or `False`?
3. What is `-7 // 2`?
4. What does `"a" or "b"` evaluate to?
5. When does a `for` loop's `else` block run?
6. What does a function with no `return` return?
7. Why is `def f(items=[])` a bug?
8. Which file mode destroys the existing contents?
9. Which is safe: `subprocess.run("ls " + path, shell=True)` or `subprocess.run(["ls", path])`?
10. In a traceback, which line is the actual error?
11. What is `round(2.5)`?
12. Does `.gitignore` stop tracking a file that is already committed?

<details>
<summary>Answers</summary>

1. `None` - it sorts in place. Use `sorted()` for a new list.
2. `True` - `bool` is a subclass of `int`.
3. `-4` - floor division rounds down.
4. `"a"` - `or` returns the first truthy operand, not a boolean.
5. Only when the loop completed without hitting `break`.
6. `None`.
7. The default list is created once at definition time and shared across all calls.
8. `w`.
9. The list form. `shell=True` with concatenated input is a shell-injection hole.
10. The **last** line. Read bottom-up.
11. `2` - banker's rounding sends ties to the even number.
12. No. Use `git rm --cached FILE` first.
</details>
