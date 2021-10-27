#hung push check check

# Cach 1
import itertools

s = input('input array of num: ')
s = list(map(int, s))  # convert from string to a list of integer number # can change int to float
print('Integer array:', s)
x = int(input('input the Target: '))
print('Target is:', x)
for i in itertools.combinations(s, 2):
    if sum(i) == x:
        print('Pair of number equal target', [s.index(number) for number in i])

# Cach 2
for t in range(0, len(s)):
    for j in range(t + 1, len(s)):
        if s[t] + s[j] == x:
            print([t, j])
