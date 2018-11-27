rolls = np.array([4, 6, 5, 5, 5, 5, 2, 5, 1, 5, 1, 6, 5, 2, 2, 2, 1, 6,
1, 2, 3, 2, 5, 6, 2, 2, 3, 1, 2, 3, 3, 1, 1, 4, 1, 2, 2, 5, 2, 1, 3, 2,
1, 1, 5, 5, 1, 5, 2, 3, 1, 1, 3, 3, 4, 4, 4, 1, 1, 2, 2, 6, 4, 1, 4, 6,
3, 2, 4, 1, 4, 2, 6, 1, 3, 6, 1, 5, 3, 1, 1, 3, 1, 5, 6, 3, 2, 1, 3, 3,
2, 1, 6, 1, 3, 1, 5, 4, 2, 2])

empMean = np.mean(rolls)
print(empMean)   # 2.9399999999999999

bootNum = 1000
bootMeans = np.zeros(bootNum)
for bootRep in range(bootNum):
    bootMeans[bootRep] = np.mean(np.random.choice(rolls,len(rolls)))
bootMeans = np.sort(bootMeans)
confInterval = (bootMeans[int(np.floor(bootNum*0.025))],bootMeans[int(np.ceil(bootNum*0.975))])
print(confInterval)  # (2.6099999999999999, 3.27)

nullSims = 1000

nullRolls = np.zeros((nullSims,100))

for sim in range(nullSims):
    nullRolls[sim] = np.random.randint(1,7,100)

simCounts_one = np.zeros(nullSims)
simCounts_six = np.zeros(nullSims)
for sim in range(nullSims):
    simCounts_one[sim] = sum(nullRolls[sim] == 1)
    simCounts_six[sim] = sum(nullRolls[sim] == 6)

empCount_one = sum(rolls == 1)
empCount_six = sum(rolls == 6)

lowOneTail_one = sum(simCounts_one <= empCount_one)/nullSims
print(lowOneTail_one)  # ~0.99
lowOneTail_six = sum(simCounts_six <= empCount_six)/nullSims
print(lowOneTail_six)  # ~0.05

import matplotlib.pyplot as plt

plt.hist(simCounts_one)
plt.axvline(x=empCount_one,color="red",linewidth=5.0)
plt.show()

plt.hist(simCounts_six)
plt.axvline(x=empCount_six,color="red",linewidth=5.0)
plt.show()

def calcChiSq(rollVals,expProbs):
    counts = [0,0,0,0,0,0]
    for i in range(6):
        counts[i] = sum(rollVals == i+1)
    chiSqVal = 0.0
    for i in range(len(counts)):
        expCount = sum(counts) * expProbs[i]
        chiSqVal += (((counts[i] - expCount) ** 2) / expCount)
    return chiSqVal

equalProbs = [1/6,1/6,1/6,1/6,1/6,1/6]

empChiSq = calcChiSq(rolls,equalProbs)

simChiSqs = []
for i in range(nullSims):
    simChiSqs.append( calcChiSq(nullRolls[i],equalProbs) )

plt.hist(simChiSqs)
plt.axvline(x=empChiSq,color="red",linewidth=5.0)
plt.show()

upperOneTail_chiSq = sum(simChiSqs >= empChiSq)/nullSims
print(upperOneTail_chiSq)  # ~0.02
