# Week 14 Outline

## In the News

- [Efron Award for the Bootstrap](https://www.nature.com/articles/d41586-018-07349-2)


## Final Projects

#### Presentations (25%)

- 15-20 minutes
- Rough structure:
  - What is the question, problem, or challenge
  - How did you structure your code to answer the question, solve the problem or meet the challenge
  - What did you learn using your code?
- All team members need to participate in the presentation
- You are welcome to use whatever visuals you'd like (Powerpoint slides, websites, images, etc.)
- For this portion of the grade, I'll be looking for clarity and a well-designed presentation

#### Code (75%)

- While there are not specific guidelines for the number of lines of code you need to have, the scope of the project should represent significant effort over several weeks.
- All team members should contribute roughly equally. I should see commits from all team members in the code repository.
- The code itself should be clearly laid out and well commented. I shouldn't have to struggle to understand what you're trying to do.
- The code should be accompanied by some sort of README that tells a future user (or your future self) what the goal is and how to run the code to answer the question, solve the problem, etc. This explanation should be higher level than the comments in the code itself.


## Using Simulations to Test Hypotheses

    The Problem - Testing Against a Discrete Uniform Distribution

        Someone is trying to convince you to gamble with them in a dice game. To
        convince you that their die is not fake and has all six numbers on it,
        they give you the outcomes of 100 previous rolls.

        Are you willing to wager a serious amount of money in this game if the
        outcome depends on the coin being fair?

        >>> rolls = np.array([4, 6, 5, 5, 5, 5, 2, 5, 1, 5, 1, 6, 5, 2, 2, 2, 1, 6,
        1, 2, 3, 2, 5, 6, 2, 2, 3, 1, 2, 3, 3, 1, 1, 4, 1, 2, 2, 5, 2, 1, 3, 2,
        1, 1, 5, 5, 1, 5, 2, 3, 1, 1, 3, 3, 4, 4, 4, 1, 1, 2, 2, 6, 4, 1, 4, 6,
        3, 2, 4, 1, 4, 2, 6, 1, 3, 6, 1, 5, 3, 1, 1, 3, 1, 5, 6, 3, 2, 1, 3, 3,
        2, 1, 6, 1, 3, 1, 5, 4, 2, 2])

        HINT: Try simulating rolls of a fair dice and comparing them to these
        outcomes. How are you doing the comparison?

    Solution 1: Using the Bootstrap

        As we talked about last week, the bootstrap is a very flexible approach
        to estimating a confidence interval on the sum (or something related to
        the sum, like the mean) for a set of values drawn from an unknown
        distribution. If our die is fair, the values 1-6 should occur with equal
        frequency, so the expected mean is:

        1(1/6) + 2(1/6) + 3(1/6) + 4(1/6) + 5(1/6) + 6(1/6) = 3.5

        So if the 95% confidence interval on our observed mean excludes 3.5, we
        can be confident that the die is not fair. The estimated mean can be
        calculated as:

        >>> empMean = np.mean(rolls)
        >>> print(empMean)   # 2.9399999999999999

        The 95% confidence interval can then be estimated using the bootstrap as
        follows:

        >>> bootNum = 1000
        >>> bootMeans = np.zeros(bootNum)
        >>> for bootRep in range(bootNum):
        >>>     bootMeans[bootRep] = np.mean(np.random.choice(rolls,len(rolls)))
        >>> bootMeans = np.sort(bootMeans)
        >>> confInterval = (bootMeans[int(np.floor(bootNum*0.025))],bootMeans[int(np.ceil(bootNum*0.975))])
        >>> print(confInterval)  # (2.6099999999999999, 3.27)

        Since the 95% confidence interval does not include 3.5, we have evidence
        that the coin is biased towards small values.

    Solution 2: A Hypothesis Test

        In standard (known as frequentist) hypothesis testing, we begin with a
        default explanation (a null hypothesis) for what might be true and see if
        our data can reject this null. In our case, the null hypothesis is that
        our die is fair. We expect roughly equal frequencies of all values from
        1-6 in a large number of rolls. However, small numbers of rolls will
        vary from the expected proportions just due to chance. We need to ask if
        the deviations we see from equal proportions are more than we should
        reasonably expect if our die is fair.

        First, we need to generate a series of potential observations (in this
        case 1,000) if our null hypothesis is true:

        # Define our number of simulations
        >>> nullSims = 1000

        # Create an array of zeros
        >>> nullRolls = np.zeros((nullSims,100))

        # Simulate sets of 100 rolls, and add them to our array
        >>> for sim in range(nullSims):
        >>>     nullRolls[sim] = np.random.randint(1,7,100)

        Now we need some way to quantitatively compare our observed data to
        those simulated from our null distribution. To do this, we need to
        define a value that we can calculate for each data set. These values
        are known as test statistics. For instance, we could use either the
        number of 1s or the number of 6s (or any other number on a die face) as
        test statistics.

        Let's count the number of 1s and 6s in each of our simulated datasets.

        >>> simCounts_one = np.zeros(nullSims)
        >>> simCounts_six = np.zeros(nullSims)
        >>> for sim in range(nullSims):
        >>>     simCounts_one[sim] = sum(nullRolls[sim] == 1)
        >>>     simCounts_six[sim] = sum(nullRolls[sim] == 6)

        Now let's count the numbers of 1s and 6s in our observed rolls.

        >>> empCount_one = sum(rolls == 1)
        >>> empCount_six = sum(rolls == 6)

        Now we need to figure out how our observed values compare to the
        simulations. First, let's calculate how what percentage of simulated
        counts are less than (or equal to) our observed count for each number.
        This is an estimate of the lower one-tailed p-value.

        >>> lowOneTail_one = sum(simCounts_one <= empCount_one)/nullSims
        >>> print(lowOneTail_one)  # ~0.99
        >>> lowOneTail_six = sum(simCounts_six <= empCount_six)/nullSims
        >>> print(lowOneTail_six)  # ~0.05

        To get an intuitive sense for what these p-values mean, let's plot the
        simulated values relative to the empirical values.

        # Import pyplot
        >>> import matplotlib.pyplot as plt

        # Plot histogram of simulated 1 counts and compare to empirical
        >>> plt.hist(simCounts_one)
        >>> plt.axvline(x=empCount_one,color="red",linewidth=5.0)
        >>> plt.show()

        # Plot histogram of simulated 6 counts and compare to empirical
        >>> plt.hist(simCounts_six)
        >>> plt.axvline(x=empCount_six,color="red",linewidth=5.0)
        >>> plt.show()

        Looking at the counts of individual values can be useful, because it can
        tell us not only if our die is biased, but also HOW it is biased. However,
        looking at each value individually means that we're not able to use all
        of the information at once. Ideally, we'd like some way to do a general
        test of all values at once. The special statistic known as the chi-squared
        statistic is one way to do just that. To calculate this value, we use this
        formula (https://en.wikipedia.org/wiki/Chi-squared_test)

        [(observed_count - expected_count)^2] / expected_count

        and sum across all possible values. Let's write a function to do this:

        >>> def calcChiSq(rollVals,expProbs):
        >>>     counts = [0,0,0,0,0,0]
        >>>     for i in range(6):
        >>>         counts[i] = sum(rollVals == i+1)
        >>>     chiSqVal = 0.0
        >>>     for i in range(len(counts)):
        >>>         expCount = sum(counts) * expProbs[i]
        >>>         chiSqVal += (((counts[i] - expCount) ** 2) / expCount)
        >>>     return chiSqVal

        Now that we've got a function to calculate chi-squared values, let's
        compare the empirical value of this statistic to the values from the
        simulated datasets.

        >>> equalProbs = [1/6,1/6,1/6,1/6,1/6,1/6]

        >>> empChiSq = calcChiSq(rolls,equalProbs)

        >>> simChiSqs = []
        >>> for i in range(nullSims):
        >>>     simChiSqs.append( calcChiSq(nullRolls[i],equalProbs) )

        Now let's visually compare the simulated and empirical chi-squared values.

        >>> plt.hist(simChiSqs)
        >>> plt.axvline(x=empChiSq,color="red",linewidth=5.0)
        >>> plt.show()

        Because chi-squared values always get bigger as our observed and expected
        counts become more different, we are always interested in the upper
        one-tailed p-value. In this case, we can calculate it as:

        >>> upperOneTail_chiSq = sum(simChiSqs >= empChiSq)/nullSims
        >>> print(upperOneTail_chiSq)  # ~0.02

## Probability Distributions

- `import numpy as np`


### Discrete Distributions

- Discrete Uniform
  - Can take any set of values, depending on those specified by the user. All values have equal probability.
  - `np.random.randint(low,high,size)`
    - Draws numbers from a discrete uniform distribution of integers between _low_ and _high_. _size_ indicates the number of values to draw.
  - `np.random.choice(arrayOfValues,size)`
    - Draws values from an array, by default with equal probability. This array can hold any type of variable. Again, _size_ indicates the number of values that are drawn.


- Bernoulli
  - This distribution takes the value 1 with probability p and the value 0 with probability 1-p. An outcome of 1 is often termed _success_ and 1-p termed _failure_. Think of a coin flip. Only the values 0 or 1 can result from a Bernoulli trial.
  - `np.random.binomial(size,n=1,p)`
  - The Bernoulli distribution is a special case of the binomial when there's only one trial (`n=1`).


- Binomial
  - This distribution models the number of successes in multiple Bernoulli trials, where the probability of success is p. Therefore, this distribution can take any value between 0 and the total number of trials (n).
  - `np.random.binomial(size,n,p)`


  <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Binomial_distribution_pmf.svg" width=300>


- Poisson
  - This distribution models the number of events that occur in a given amount of time if there's a constant probability of an event occurring (for instance, the number of messages you receive if the senders are independent of one another). As with the binomial, this distribution can take any value greater than or equal to 0.
  - `np.random.poisson(lambda,size)` - _lambda_ is the rate parameter of the Poisson. Higher rates result in more events per unit time or space.


  <img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Poisson_pmf.svg" width=300>

- Geometric
  - This distribution (__on the left__, below) models the number of Bernoulli trials that must be run before the first success. Therefore, it can take values greater than or equal to 1.
  - `np.random.geometric(p,size)` - p is the probability of success in each trial


  <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Geometric_pmf.svg" width=400>


### Continuous Distributions

- Normal
  - This distribution can take any continuous value. Because of the Central Limit Theorem, this is a very commonly used distribution. Remember that the Central Limit Theorem says that the sum of a large number of random variables drawn from any distribution will approximate a Normal. So, anything in the real world that is the sum of many small effects can be modeled with a Normal. For instance, think about an organismal trait like height whose value is affected by many different genes.
  - `np.random.normal(loc,scale,size)` - _loc_ is the mean of the Normal and _scale_ is its standard deviation (i.e., its width or spread).


<img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg" width=400>

- Exponential
  - The exponential distribution is commonly used to describe the amount of time that elapses between independent events that each have a constant probability of occurring. It is closely tied to the Poisson. For a given amount of time, the Poisson describes how many events are expected to occur, and the exponential describes how much time elapses between them.
  - `np.random.exponential(scale,size)` - _scale_ is a parameter that controls the spread of the distribution. Higher _scale_ values result in distributions with more variance. _scale_ is the inverse of the rate, which describes how fast the events are expected to occur.

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Exponential_pdf.svg" width=400>


- Beta
  - The beta distribution is bounded by 0 and 1, but can take many different shapes (flat, unimodal, bimodal, etc.). The overall shape of the distribution is controlled by two shape parameters - alpha and beta. In general, small values of the shape parameters (< 1) put more probability on values near 0 and 1. Large values put more probability on intermediate values.
  - `np.random.beta(a,b,size)` - a and b are the two shape parameters.


<img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Beta_distribution_pdf.svg" width=400>


### Distribution Resources

- [Seeing Theory - Probability Distributions](https://seeing-theory.brown.edu/probability-distributions/index.html)

    ###### Discrete Distributions


- [Wikipedia - Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_distribution)
- [Wikipedia - Binomial](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Wikipedia - Poisson](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Wikipedia - Geometric](https://en.wikipedia.org/wiki/Geometric_distribution)

    ##### Continuous Distributions


- [Wikipedia - Normal](https://en.wikipedia.org/wiki/Normal_distribution)
- [Wikipedia - Exponential](https://en.wikipedia.org/wiki/Exponential_distribution)
- [Wikipedia - Chi-squared](https://en.wikipedia.org/wiki/Chi-squared_distribution)
