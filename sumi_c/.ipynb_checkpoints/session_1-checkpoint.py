
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''Q2 - Quick Implementation'''
day_i = ["Bob: 1200", "Alice: 2500", "Celia: 110"]

df = pd.DataFrame.from_dict(dict([i.split(': ') for i in day_i]), orient='index')
df = df.reset_index()
df.columns = ['Customer', 'Total Purchase']
df['Total Purchase'] = df['Total Purchase'].apply(int)
df

np.array([i.split(': ') for i in day_i])


"""Question 2:"""

#Examples (this cell)
day_i = ["Bob: 1200", "Alice: 2500", "Celia: 110"]

[x**2 for x in range(5)]

s1 = day_i[0]

s1.split(': ')

#Implementation:
day_i = ["Bob: 1200", "Alice: 2500", "Celia: 110", "Matt: 5"]

d = dict([s.split(': ') for s in day_i])

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
df = pd.DataFrame.from_dict(d, orient='index')
df = df.reset_index()
df.columns = ['Customer', 'Total Purchase']
df

#Example of default from_dict behavior:
pd.DataFrame.from_dict({'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']})

"""Matt's Solution for Question 3: (Use your own, it's cooler.)"""

g_meta_hist = []
for i in range(100):
    #Create random range and secret number within range:
    ns = sorted(np.random.randint(0,10000,20))
    low = ns[0]
    high = ns[-1]
    number = np.random.randint(low, high)
    #print(low, high, number)

    #Binary search for guess:
    guess_history = []
    guess = int(np.mean([low,high]))
    guesses = 1
    while guess != number:
        if guess < number:
            low = guess
            guess = int(np.mean([low,high]))
        if guess > number:
            high = guess
            guess = int(np.mean([low,high]))
        guesses += 1
        guess_history.append(guess)
        #print(guesses, '|', guess)
    #plt.plot(guess_history)
    g_meta_hist.append(len(guess_history))