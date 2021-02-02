# Delete occurrences of an element if it occurs more than n times

## Instructions
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

## Tests
```js
Test.assertSimilar(deleteNth([20,37,20,21], 1), [20,37,21])
Test.assertSimilar(deleteNth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
Test.assertSimilar(delete_nth([39, 39, 30, 30, 39, 30, 39, 44, 44, 44, 8, 44, 30, 23, 39, 8, 30, 30, 44, 44, 39, 39, 30, 8, 8, 44, 8, 39, 23, 30, 44, 8, 30, 44, 8, 44, 8, 30], 2), [39, 39, 30, 30, 44, 44, 8, 23, 8, 23])
Test.assertSimilar(delete_nth([16, 10, 16, 47, 47, 16, 47, 47, 46, 47, 10, 39, 20, 16, 20, 46, 47, 32, 47, 46, 47, 39, 39, 20, 20, 16, 20, 10, 39, 39, 20, 47, 10, 47, 39, 16, 47, 47, 47, 16, 46, 10, 20, 47, 47, 16, 16, 20, 46, 10, 20, 10, 47, 10, 16, 47, 47, 10, 20, 46, 46, 10], 5), [16, 10, 16, 47, 47, 16, 47, 47, 46, 47, 10, 39, 20, 16, 20, 46, 32, 46, 39, 39, 20, 20, 16, 20, 10, 39, 39, 10, 46, 10, 46])
Test.assertSimilar(delete_nth([22, 5, 22, 22, 5, 5, 22, 22, 5, 19, 5, 22, 5, 22, 48, 22, 22, 5, 5, 19, 22, 5, 22, 22, 5, 5, 5, 48, 22, 5, 5, 5, 22, 22], 4), [22, 5, 22, 22, 5, 5, 22, 5, 19, 48, 19, 48])
Test.assertSimilar(delete_nth([4, 4, 26, 26, 4, 4, 4, 26, 4, 7, 4, 7, 7, 7, 4, 7, 4], 8), [4, 4, 26, 26, 4, 4, 4, 26, 4, 7, 4, 7, 7, 7, 4, 7])
Test.assertSimilar(delete_nth([18, 18, 7, 18, 49, 18, 45, 45, 49, 49, 18, 45, 45, 7, 7, 7, 7, 49, 45, 7, 17, 18, 49, 49, 18, 45, 49, 49, 17, 45, 45, 17, 7, 18, 49], 3), [18, 18, 7, 18, 49, 45, 45, 49, 49, 45, 7, 7, 17, 17, 17])
```
