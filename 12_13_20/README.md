# Challenge
Complete the function that determines if a given non-negative integer is a power of two. From the corresponding Wikipedia entry:

```a power of two is a number of the form 2^n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.```

You may assume the input is always valid.

# Test Cases
```javascript
test.assert_equals(power_of_two(0), False)
test.assert_equals(power_of_two(1), True)
test.assert_equals(power_of_two(2), True)
test.assert_equals(power_of_two(5), False)
test.assert_equals(power_of_two(6), False)
test.assert_equals(power_of_two(4096), True)
```
