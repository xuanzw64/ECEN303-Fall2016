__author__ = " Rajiv Chockalingam "
__NetID__ = " rcwiz1296 "
__GitHubID__ = " rajchocolate "
__SelfGrade__ = " 5 "
__Challenge__ = "1"
__Answer1__ = " 1 "
__Answer2__ = " 6 "

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = .7
NumberFlips = 8
NumberTrials = 100000
FlipSum = 0
totalSum = 0
Trials = []


def biasedcoinflip(p=0.5):
   if random.random() < p :
       return 1
       # Trials.append(1)

   else :
       return 0
        #Trials.append(0)


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    FlipSum += biasedcoinflip(ParameterP)
    SumTrials.append(FlipSum)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)

for elements in Distribution:
    totalSum += elements

print(totalSum)

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
The distribution becomes more left skewed and with a higher probability to 8
What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.
"""
4
