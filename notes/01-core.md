# Compute Fibonacci numbers iteratively: implementation

## What the example does

Two running values avoid exponential recursion and use constant auxiliary slots. Integers still grow in size as n increases; negative n is rejected.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
10
```

Expected result:

```json
55
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
