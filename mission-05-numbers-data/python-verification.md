# Python verification and converter observations

Python's `bin()` returns a binary string with a `0b` prefix, `hex()` returns a hexadecimal string with a `0x` prefix, and `int(text, base)` converts text in the requested base to a decimal integer. `ord()` returns the Unicode code point for a character; for basic ASCII characters those code points match the ASCII decimal values.

| Expression | Result | Matches hand work? |
|---|---:|---|
| `bin(13)` | `0b1101` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `hex(10)` | `0xa` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `int('1111', 2)` | `15` | Yes; 15 is F in hexadecimal. |
| `ord('A')` | `65` | ASCII A |
| `ord('a')` | `97` | ASCII a |

## Converter runs

| Decimal input | Binary output | Hexadecimal output |
|---:|---|---|
| 7 | `111` | `7` |
| 10 | `1010` | `A` |
| 255 | `11111111` | `FF` |

The converter reads a decimal integer with `input()`, converts the string with `int()`, then uses `format(value, 'b')` and `format(value, 'X')` to display binary and uppercase hexadecimal.
