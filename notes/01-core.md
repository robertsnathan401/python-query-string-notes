# Build a query string with repeated keys: implementation

## What the example does

doseq expands lists into repeated keys. Spaces use plus encoding; use an ordered list of pairs if key ordering has protocol significance.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "q": "hello world",
  "tag": [
    "a",
    "b"
  ]
}
```

Expected result:

```json
"q=hello+world&tag=a&tag=b"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
