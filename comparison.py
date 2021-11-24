"""
Compare list of integer array from 0-X with multiplication of 0-X first prime numbers
There is no worst and best case
"""


import sys

import plotly.graph_objects as go


def get_primes(size: int):
    numr = 100000
    primes = []

    for n in range(1, numr):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)

    return primes[1:size]


def get_multi_best_case(primes, size):
    output = 1
    for i in range(0, size):
        output *= primes[i]
    return output


def get_multi_worst_case(primes, size):
    output = 1
    i = size
    while i >= 1:
        output *= primes[i - 1]
        i -= 1

    return output


def get_multi_middle_case(primes, size):
    output = 1
    i = size
    while i >= 1:
        if i % 2 == 0:
            output *= primes[i - 1]
        else:
            output *= primes[size - 1 - i]
        i -= 1

    return output


def list_best_case(size):
    output = []
    for i in range(0, size):
        output.append(i)
    return output


def list_worst_case(size):
    output = []
    i = size
    while i >= 1:
        output.append(i)
        i -= 1

    return output


SIZE = 1100
PRIMES = get_primes(SIZE)

# Best list
best_list = []
for i in range(0, SIZE):
    best_list.append(sys.getsizeof(list_best_case(i)))

# Worst list
worst_list = []
for i in range(0, SIZE):
    worst_list.append(sys.getsizeof(list_worst_case(i)))

# Best Multi
best_multi = []
for i in range(0, SIZE):
    best_multi.append(sys.getsizeof(get_multi_best_case(PRIMES, i)))

# Worst Multi
worst_multi = []
for i in range(0, SIZE):
    worst_multi.append(sys.getsizeof(get_multi_worst_case(PRIMES, i)))


# Worst Multi
middle_multi = []
for i in range(0, SIZE):
    middle_multi.append(sys.getsizeof(get_multi_middle_case(PRIMES, i)))


x = []
for i in range(1, SIZE + 1):
    x.append(i)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=best_list,
    name='Best list',
))
fig.add_trace(go.Scatter(
    x=x,
    y=worst_list,
    name='Worst list',
))
fig.add_trace(go.Scatter(
    x=x,
    y=best_multi,
    name='Best multi',
))
fig.add_trace(go.Scatter(
    x=x,
    y=worst_multi,
    name='Worst multi',
))
fig.add_trace(go.Scatter(
    x=x,
    y=middle_multi,
    name='Middle multi',
))

fig.show()

# df = df.sort_values(by="x")
# fig = px.line(df, x="x", y="y", title="Sorted Input")
# fig.show()
