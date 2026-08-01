# Logic Errors

## Definition

A logic error occurs when a program runs successfully but produces incorrect results because the program's logic is wrong.

## Common Symptoms

- Incorrect score calculation
- Wrong comparison operators
- Incorrect loop conditions
- Incorrect branching with if/else statements

## Example

```python
if score > 100:
    level = "Expert"
```

If a score of exactly 100 should also be considered Expert, the condition is incorrect.

Correct version:

```python
if score >= 100:
    level = "Expert"
```

## Debugging Strategy

- Compare expected output with actual output.
- Print variable values during execution.
- Test edge cases.
- Verify every condition carefully.