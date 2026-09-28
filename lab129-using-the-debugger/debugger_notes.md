# Lab 129 - Using the Debugger

## The problem

`average_buggy.py` should print an average of 89.0 but prints 445.0 instead.

```
Scores: [88, 92, 79, 95, 91]
Average: 445.0
Highest: 95
```

445 is the **sum** of the scores, not the average. That points at the division
in `calculate_average`, so that is where I started.

## Starting the debugger

```bash
python3 -m pdb average_buggy.py
```

The debugger stops before the first line runs.

## The session

```
(Pdb) break calculate_average
Breakpoint 1 at average_buggy.py:12

(Pdb) continue
Scores: [88, 92, 79, 95, 91]
> average_buggy.py(13)calculate_average()
-> total = 0

(Pdb) args
numbers = [88, 92, 79, 95, 91]
```

The input is correct, so the bug is inside the function.

```
(Pdb) next
> average_buggy.py(14)calculate_average()
-> count = 0

(Pdb) next
(Pdb) next
(Pdb) next
(Pdb) p total, count
(88, 0)
```

First pass through the loop: total is 88, count has not been set yet.

```
(Pdb) next
(Pdb) next
(Pdb) p total, count
(88, 1)

(Pdb) next
(Pdb) next
(Pdb) p total, count
(180, 1)
```

**There is the bug.** `total` has gone from 88 to 180, but `count` is still 1.
It should be 2 by now.

```
(Pdb) return
--Return--
> average_buggy.py(18)calculate_average()->445.0
-> return total / count

(Pdb) p total, count
(445, 1)
```

445 divided by 1 is 445. The division was never the problem - the counter was.

## The fix

```python
count = 1              # wrong - this sets count to 1 every time round
count = count + 1      # right - this adds one each time round
```

445 / 5 = 89.0. Correct.

## pdb commands I used

| Command | Short | What it does |
|---|---|---|
| `break funcname` | `b` | Stop when a function is entered |
| `continue` | `c` | Run until the next breakpoint |
| `next` | `n` | Run the next line, stepping over function calls |
| `step` | `s` | Run the next line, stepping into function calls |
| `return` | `r` | Run until the current function returns |
| `p variable` | | Print a value |
| `args` | `a` | Show the function's arguments |
| `list` | `l` | Show the code around the current line |
| `where` | `w` | Show the call stack |
| `quit` | `q` | Leave the debugger |

Pressing ENTER repeats the last command, which is how you step several lines
quickly.

## Things to remember

- `next` steps **over** a function call, `step` goes **into** it.
- In Python 3 the pdb command is `p total`, not `print total`. Writing
  `print total` gives a SyntaxError because that is Python 2 syntax.
- You can also add `breakpoint()` in the code to stop at one specific line
  instead of running the whole program under pdb.
- Read a traceback from the **bottom** - the last line is the actual error.
