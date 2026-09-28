# Lab 130 - Bugs found and fixed

## hello_world_buggy.py

### Bug 1 - the function does not return anything
```python
def get_greeting(name):
    greeting = "Hello, " + name + "!"
    # no return
```
The program printed `None`. A function without a `return` statement gives back
`None`, so `greeting` was never the text.

**Fix:** `return greeting`

### Bug 2 - repeat_greeting does not return the list
The caller does `len(messages)` but nothing was returned, so `messages` was
`None` and `len()` failed.

**Fix:** build a list, append each message, return it.

### Bug 3 - joining a string and a number
```python
print("The name has " + length + " characters")
```
`TypeError: can only concatenate str (not "int") to str`. Python will not turn
the number into text automatically.

**Fix:** `str(length)`, or use an f-string.

### Bug 4 - len() on None
This was caused by bug 2. Fixing bug 2 fixed this one as well.

### Bug 5 - going past the end of the list
```python
for i in range(len(names) + 1):
    print(get_greeting(names[i]))
```
`names` has 3 items with indexes 0, 1 and 2. `range(4)` gives 0, 1, 2, 3 and
index 3 does not exist, so it raised `IndexError`.

**Fix:** loop through the list directly with `for name in names:`. Then there is
no index to get wrong.

---

## caesar_buggy.py

These were harder because only one of them crashed. The rest just gave the wrong
answer.

### Bug 1 - wrong starting letter for capitals
```python
elif letter.isupper():
    start = ord("a")     # should be ord("A")
```
`ord("H")` is 72 and `ord("a")` is 97, so 72 - 97 is negative and the result
came out as punctuation instead of a letter.

**Found by:** testing capitals separately from lower case. Lower case on its own
looked fine.

### Bug 2 - no modulo
```python
position = ord(letter) - start + shift   # no % 26
```
`encrypt("xyz", 3)` gave `{|}` because z + 3 ran off the end of the alphabet
into the next characters in the ASCII table.

**Found by:** testing the end of the alphabet. `abc` worked, `xyz` did not.

### Bug 3 - = instead of +=
```python
result = shift_letter(letter, shift)     # should be result = result + ...
```
Only the last letter came out, because each pass through the loop replaced
`result` instead of adding to it.

**Found by:** the output was one character long instead of eleven.

### Bug 4 - decrypt encrypts again
```python
def decrypt(text, shift):
    return encrypt(text, shift)          # should be -shift
```
Encrypting twice shifts forward twice. It never shifts back.

**Found by:** checking that `decrypt(encrypt(message))` gives back the original
message. This one test catches bugs 1, 2, 3 and 4 at the same time.

---

## What I learned

- A function with no `return` gives back `None`. Most "why is my value None"
  problems are this.
- `=` replaces a value, `+=` adds to it. In a loop that builds something up,
  `=` throws away everything from the previous passes.
- Test the edges, not just the middle. `xyz` found a bug that `abc` did not.
- Test both cases of a condition. Lower case worked, capitals did not.
- Checking that something can be undone (encrypt then decrypt) is a strong test,
  because it catches several bugs at once without you needing to know which.
- Fix one bug at a time and run the program again. Fixing several at once means
  you cannot tell which fix actually worked.
- A program that runs is not the same as a program that works. The crashes were
  easy - Python said which line. The wrong answers were the hard ones.
