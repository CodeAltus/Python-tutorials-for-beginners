# Conditional operators and if statement

In this lesson, I will show you how to use conditional operators and if statements in Python.

## Video
[![Alt text](https://img.youtube.com/vi/heDBN1lrR0c/hqdefault.jpg)](https://www.youtube.com/watch?v=heDBN1lrR0c)

https://www.youtube.com/watch?v=heDBN1lrR0c

### Conditionals
Boolean datatype
- True
- False

---

Relational operators

- Used to compare two variables (of any datatype)

|Operator|Meaning|Example (radius is 10)|Result|
|---|---|---|---|
|<|Less than|radius < 0|False|
|>|More than|radius > 0|True|
|<=|Less than or equal to|radius <= 0|False|
|>=|More than or equal to|radius >= 0|True|
|==|Equal to|radius == 10|True|
|!=|Not equal to|radius != 10|False|

---

Logical operators

- Can be used to create composite conditions
- Bring together several conditions together
- `not` | `and` | `or`

---

Truth table: `not`

- Negates the conditional
- `True` becomes `False`
- `False` becomes `True`

|P|`not` P|
|---|---|
|`True`|`False`|
|`False`|`True`|

---

Truth table: `and`

- `and` of two boolean values will be `True` if and only if both boolean values are `True`

|P1|P2|P1 `and` P2|
|---|---|---|
|`True`|`True`|`True`|
|`True`|`False`|`False`|
|`False`|`True`|`False`|
|`False`|`False`|`False`|

---

Truth table: `or`

- `or` of two boolean values will be `True` if at least one of the boolean values is `True`

|P1|P2|P1 `or` P2|
|---|---|---|
|`True`|`True`|`True`|
|`True`|`False`|`True`|
|`False`|`True`|`True`|
|`False`|`False`|`False`|

---
