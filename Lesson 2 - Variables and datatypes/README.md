# Variables and datatypes

In this lesson, I will introducing variable and datatypes in Python.

## Video
[![Alt text](https://img.youtube.com/vi/NUl16LRUgw8/hqdefault.jpg)](https://www.youtube.com/watch?v=NUl16LRUgw8)

https://youtu.be/NUl16LRUgw8

## Datatypes

There are 4 types of data in Python:

### 1. Boolean
- Can be either:
    - True
    - False
- Must start with a capital letter
- Reserved keywords - cannot be used as variable names
- true, TRUE, false and FALSE are not boolean values
- We will talk about boolean in greater detail later on

### 2. String
- Anything enclosed with double or single quotations
- Represent characters or text
- Example: "Hello world", "python", 'I am a string' and 'I said, "Hello!"'

### 3. Integer
- Any whole number
- Can be positive or negative
- Must **not** contain a decimal point
- Examples: 0, 1, 2, 3, -90, -123, 4072, -38

### 4. Float
- Any number
- **Must** have a decimal point or else it is an integer
- Examples: 0.0, 1.0, 2.0, 2.3, -123.8383, -52.90
- 2, -3, 8 are not floats

## Variables

Variables are containers for storing data.

After the program has finished executing, all data stored in variables is lost - short term memory

Rules for writing variable name:
- Variable name must start with a letter (a-z, A-Z) or underscore (_)
- Variable name cannot start with a number (0-9)
- Variable name can only contain letters (a-z, A-Z), numbers (0-9) and underscores (_)
- Variable name is case-sensitive (age and AGE are different variables)
- NO WHITESPACE in variable name
- No other special characters like punctuation in variable name

Examples of **invalid** variable names: 9age, my-name, hello there

Examples of **valid** variable names: my_name, Python1, AGE3, age3

## Quiz
### 1. What datatypes are these?:
- "5343"
- '7.898'
- true
- False
- 44.000
- -49
- -123
- "True"
- "I am definitely a string'
- "I said, "Hello there!", and walked into the room"

### 2. Are these valid variable names?:
- 12good
- this_name
- my name
- How_are_you?
- x
- zzzz
- PythonTM

### 3. Are these the same variables?
- true | True
- False | False
- Age | Age

## Quiz Answers
### 1. What datatypes are these?:
- "5343" (string)
- '7.898' (string)
- true (invalid (boolean must start with uppercase letter))
- False (boolean)
- 44.000 (float)
- -49 (integer)
- -123 (integer)
- "True" (string)
- "I am definitely a string' (invalid string since double and single quote is used)
- "I said, "Hello there!", and walked into the room" (invalid because double quotes within double quotes does not work)

### 2. Are these valid variable names?:
- 12good (no)
- this_name (yes)
- my name (no)
- How_are_you? (no)
- x (yes)
- zzzz (yes)
- PythonTM (yes)

### 3. Are these the same variables?
- true | True (second one is not a variable since it is a reserved keyword)
- False | False (not variables)
- Age | Age (yes)