# Task
Given a Divisor and a Bound , Find the largest integer N , Such that:
- N is divisible by divisor
- N is less than or equal to bound
- N is greater than 0.

The parameters (divisor, bound) passed to the function are only positive values .
It's guaranteed that a divisor is Found .

## Test Cases
```javascript
describe("Basic tests", function(){
  Test.assertEquals(maxMultiple(2,7),6);
  Test.assertEquals(maxMultiple(3,10),9);
  Test.assertEquals(maxMultiple(7,17),14);
  Test.assertEquals(maxMultiple(10,50),50);
  Test.assertEquals(maxMultiple(37,200),185);
  Test.assertEquals(maxMultiple(7,100),98);
});
```
