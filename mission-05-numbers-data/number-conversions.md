# Number conversion working

## Decimal to binary

Repeated division by 2; read remainders from bottom to top.

- 13: 13÷2=6 r1; 6÷2=3 r0; 3÷2=1 r1; 1÷2=0 r1 → **1101₂**.
- 25: 25÷2=12 r1; 12÷2=6 r0; 6÷2=3 r0; 3÷2=1 r1; 1÷2=0 r1 → **11001₂**.

## Binary to decimal

Use each bit's place value, starting with 2⁰ at the right.

- 1010₂ = 1×8 + 0×4 + 1×2 + 0×1 = **10₁₀**.
- 1101₂ = 1×8 + 1×4 + 0×2 + 1×1 = **13₁₀**.

## Hexadecimal to decimal

Hexadecimal is base 16; A=10 and F=15.

- A₁₆ = **10₁₀**.
- 1F₁₆ = 1×16 + 15 = **31₁₀**.

## Binary to hexadecimal

Group bits in sets of four from the right.

- 1111₂ is one four-bit group, which is **F₁₆**.
