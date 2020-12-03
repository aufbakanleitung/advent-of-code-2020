# Advent of Code: Python solutions
https://adventofcode.com/2020

## Lessons learned:
* assignment 2 - This is how you do a xor in python: `bool(a) ^ bool(b)`
* assignment 2 - Immediately assign split values to their variables for efficiency
```python 
n1, n2, letter, x, passw = re.split('[-:\s]', line)
```
* assignment 3 - If you're using the `x` coordinate to calculate the `y` coordinate by, don't forget to divide y over x's step size `xn` to make them independent again (`x*yn/xn`). Though it's probably better never to make the two depend on each other in the first place.
```python    
for x in range(0, len(trees), xn):
    y = int(x*yn/xn) % len(trees[0])
```
