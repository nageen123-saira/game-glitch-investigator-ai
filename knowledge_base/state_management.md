# State Management Errors

## Definition

State management errors occur when important variables are updated incorrectly during program execution.

## Example

```python
score = score - penalty
```

If the penalty is larger than the score, the score becomes negative.

## Better Solution

```python
score = max(0, score - penalty)
```

## Common Symptoms

- Negative scores
- Incorrect game progress
- Variables not updating correctly
- Lost application state

## Prevention

- Protect important variables.
- Validate updates before saving.
- Test boundary conditions.