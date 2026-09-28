# AWS re/Start - Python Labs 108 to 130

My work for the Python Programming module of AWS re/Start (cohort KENAI52).

Every script uses only the Python standard library, because that is what the
Cloud9 lab environment provides. Nothing needs installing.

## The labs

| Lab | Folder | What it covers |
|---|---|---|
| 108 | [lab108-hello-world](lab108-hello-world) | First program, variables, input |
| 109 | [lab109-numeric-data-types](lab109-numeric-data-types) | int, float, complex, operators, conversion |
| 110 | [lab110-string-data-type](lab110-string-data-type) | Indexing, slicing, string methods |
| 111 | [lab111-list-tuple-dictionary](lab111-list-tuple-dictionary) | Lists, tuples, dictionaries, sets |
| 112 | [lab112-categorize-values](lab112-categorize-values) | Identifying and grouping data types |
| 113 | [lab113-composite-data-types](lab113-composite-data-types) | Nested lists and dictionaries |
| 114 | [lab114-conditionals](lab114-conditionals) | if, elif, else, logical operators |
| 115 | [lab115-loops](lab115-loops) | for, while, break, continue, range |
| 116 | [lab116-create-git-repository](lab116-create-git-repository) | git init, add, commit, branch, merge |
| 118 | [lab118-preparing-insulin-analysis](lab118-preparing-insulin-analysis) | Loading and checking the insulin data |
| 120 | [lab120-sequence-and-weight](lab120-sequence-and-weight) | String operations and molecular weight |
| 122 | [lab122-net-charge](lab122-net-charge) | Net charge using lists and loops |
| 124 | [lab124-caesar-cipher](lab124-caesar-cipher) | Writing functions |
| 126 | [lab126-file-handlers-modules](lab126-file-handlers-modules) | Reading and writing files, making a module |
| 128 | [lab128-system-administration](lab128-system-administration) | os, shutil, subprocess, system scripts |
| 129 | [lab129-using-the-debugger](lab129-using-the-debugger) | Finding a bug with pdb |
| 130 | [lab130-debugging](lab130-debugging) | Fixing 9 bugs in two programs |

Labs 117, 119, 121, 123, 125 and 127 are the Knowledge Checks and lecture
content in Canvas, not labs.

## Running the code

Each lab folder is self-contained. Run any script from inside its own folder:

```bash
cd lab120-sequence-and-weight
python3 molecular_weight.py
```

Some scripts ask for input:

```bash
python3 lab114-conditionals/grade_checker.py
python3 lab128-system-administration/disk_usage.py /some/directory
```

## The insulin labs

Labs 118, 120, 122 and 126 are one project split across four labs. Each folder
has its own copy of `insulin.txt` so it runs on its own, the same way it does in
Cloud9.

Human insulin is two chains joined by three disulfide bonds:

```
A chain (21): GIVEQCCTSICSLYQLENYCN
B chain (30): FVNQHLCGSHLVEALYLVCGERGFFYTPKT
```

Results the labs produce, checked against published values:

| | My result | Published |
|---|---|---|
| Residues | 51 | 51 |
| Molecular weight | 5807.62 Da | 5807.57 Da |
| Net charge at pH 7 | -2.19 | negative (pI is 5.3) |
| Cysteine positions | A6, A7, A11, A20, B7, B19 | matches the 3 bonds |

## Notes

- [study-guide.md](study-guide.md) - my revision notes for the Knowledge Checks
- [lab129-using-the-debugger/debugger_notes.md](lab129-using-the-debugger/debugger_notes.md) - the pdb session that found the bug
- [lab130-debugging/bug_notes.md](lab130-debugging/bug_notes.md) - every bug and how I found it
