__author__ = "Simmi Mani"
__NetID__ = "simmi.mani123"
__GitHubID__ = "sma123"
__SelfGrade__ = "5"
__Challenge__ = "1"
__Answer1__ = "1"
__Answer2__ = "6"

"""
Simmi Mani
ECEN 303
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
#task 3
    if random.random() < p:
        return 1
    else:
        return 0
    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    #binomial.py
    cnt = 0
    for i in range(0, NumberFlips):
        cnt += biasedcoinflip(ParameterP)
    SumTrials.append(cnt)
    # Add NumberFlips coin flips for each SumTrials outcome
    #

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
#printing the sume of the elements
sum_total = 0
for Sum in range(0, len(Distribution)):
    sum_total += Distribution[Sum]  #adding each element in Distribution list.
print "The sum of the elements is", sum_total

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.

Answer: When ParameterP = 0, all the elements are zero. [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
When ParamenterP = 1, one element is 1 and the rest of the elements in the Trail are zero.
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

Answer: The sum of the elements is 1.0

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.

Answer: Most likely outcome is 6.
"""
