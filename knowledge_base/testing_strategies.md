# Testing Strategies

## Why Testing Is Important

Testing helps verify that software behaves correctly under different situations.

## Recommended Test Cases

- Normal input
- Empty input
- Invalid input
- Large input
- Boundary values

## Example

Instead of testing only:

```python
score = 50
```

Also test:

```python
score = 0
score = -10
score = 1000
```

## Best Practices

- Write automated unit tests.
- Test edge cases.
- Test invalid input.
- Verify expected output matches actual output.