# This is the numbers kata

## Task: Spell out a number. 

### For example:

-  99 --> ninety nine
-  300 --> three hundred
-  310 --> three hundred and ten
-  1501 --> one thousand, five hundred and one
-  12609 --> twelve thousand, six hundred and nine
-  512607 --> five hundred and twelve thousand, six hundred and seven
-  43112603 --> forty three million, one hundred and twelve thousand, six hundred and three

Source http://rosettacode.org

### Some Observations:
 
We need to look at the length of the number before we start calculations.
 
-  length:
-  1 == units
-  2 == tens (of units -- we do not mention those. they are the default)
-  3 == hundreds (of units)
-  ----------
-  4 == thousands
-  5 == tens of thousands
-  6 == hundreds of thousands
-  ----------
-  7 == millions
-  8 == tens of millions
-  9 == hundreds of millions ...
 
We need to split the number in segments of three digits - right to left
We need to print segments - left to right
segments are divided by a comma - omitting empty ones
zero needs to be handled separately
Multiples of ten and teens need to be handled for length 2, 5, 8, (2+x*3)
Partial hundreds are appended with ' and '