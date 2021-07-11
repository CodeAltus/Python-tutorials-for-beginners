# Test 1

## Question 1
Write a program that asks the user to input a positive dividend and a positive divisor and print out the quotient and remainder

Sample output:

> `Enter dividend: 9`
>
> `Enter divisor: 2`
>
> `The quotient is 4`
>
> `The remainder is 1`

## Question 2
Write a function called "divisible_by_9" which takes a parameter called "n" and checks if it is divisible by 9. The function should return a string which is either `"The number is divisible by 9"` or `"The number is not divisible by 9"`

Starting code:

    def divisible_by_9(n):
        # Write your code here
    
    integer = int(input("Enter a positive integer: "))
    print(divisible_by_9(integer))

Sample output 1:

> `Enter a positive integer: 18`
> 
> `The number is divisible by 9`

Sample output 2:

> `Enter a positive integer: 14`
> 
> `The number is not divisible by 9`

## Question 3
Write a program that asks the user to input their age and checks if their age is below 25

Sample output 1:

> `Enter your age: 12`
> 
> `You are less than 25 years old`

Sample output 2:

> `Enter your age: 30`
> 
> `You are more than 25 years old`

## Question 4
Write a program that asks the user to input a temperature value and output "Cold", "Normal" or "Hot" depending on the value

- temperature < 25 then print "Cold"
- 25 <= temperature <= 35 then print "Normal"
- temperature > 35 then print "Hot"

Sample output 1:

> `Enter temperature: 10`
> 
> `Cold`

Sample output 2:

> `Enter temperature: 30`
> 
> `Normal`

Sample output 3:

> `Enter temperature: 40`
> 
> `Hot`

## Question 5
Write a program that asks the user to input a positive integer n and print out the sum: `1 ^ 2 + 2 ^ 2 + 3 ^ 2 + 4 ^ 2 + ... + n ^ 2` (This is the sum of squares of the consecutive integers from 1 to the positive integer n)

(Hint: Use a for loop)

Sample output 1:

> `Enter a positive integer: 3`
> 
> `14`

Sample output 2:

> `Enter a positive integer: 10`
> 
> `385`

Sample output 3:

> `Enter a positive integer: 15`
> 
> `1240`