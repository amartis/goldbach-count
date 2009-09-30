# What this repository is about
This repository presents Python 3 script which is supposed to give new insight into Goldbach's Conjecture.

# Goldbach's Conjecture
([Definition on Wikipedia](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture))
`Every even integer greater than 2 can be expressed as the sum of two primes.`
Examples:
```
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
```
# Goldbach's Combination Count (Simply Goldbach Combination or Goldbach Count)
(Defined [here](https://github.com/amartis/goldbach-count))
Given any even integer N which greater than 2, Goldbach combination GC(N) is defined as
`The count of prime number pairs that sum up to N.`
Examples:
```
6 = 3 + 3
Thus GC(6) = 1
8 = 3 + 5
Thus GC(8) = 1
10 = 3 + 7 = 5 + 5
Thus GC(10) = 2
12 = 7 + 5
Thus GC(12) = 1
```
# And so?
`CountGoldbachCombination.py` calculates Goldbach Counts.