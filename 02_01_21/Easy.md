# Maximum Length Difference

## Instructions
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

`Find max(abs(length(x) − length(y)))`

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
Bash note:
input : 2 strings with substrings separated by,
output: number as a string
```

## Tests:
```js
Test.describe("mxdiflg") do
    Test.it("Basic tests") do
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        Test.assert_equals(mxdiflg(s1, s2), 13)
        s3 = [ 'ejjjjmmtthh',  'zxxuueeg',  'aanlljrrrxx',  'dqqqaaabbb',  'oocccffuucccjjjkkkjyyyeehh' ]
        s4 = [ 'bbbaaayddqbbrrrv' ]
        Test.assert_equals(mxdiflg(s3, s4), 10)
        s5 = [ 'cccooommaaqqoxii', 'gggqaffhhh', 'tttoowwwmmww' ]
        s6 = []
        Test.assert_equals(mxdiflg(s5, s6), -1)
        s7 = [ 'ccct',  'tkkeeeyy',  'ggiikffsszzoo',  'nnngssddu',  'rrllccqqqqwuuurdd',  'kkbbddaakkk' ]
        s8 = [ 'tttxxxxxxgiiyyy',  'ooorcvvj',  'yzzzhhhfffaaavvvpp',  'jjvvvqqllgaaannn',  'tttooo',  'qmmzzbhhbb' ]
        Test.assert_equals(mxdiflg(s7, s8), 14)
        s9 = []
        s10 = []
        Test.assert_equals(mxdiflg(s9, s10), -1)
        s11 = [ 'jgggpp',  'ss',  'ffffz',  'nnnrrrnnnvvvss',  'vvooo',  'mmdqq',  'wwwkkkkggoooommmmxxxxfbbb',  'wwttt' ]
        s12 = []
        Test.assert_equals(mxdiflg(s11, s12), -1)
    end 
end
```
