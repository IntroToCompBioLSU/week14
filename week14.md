# Week 14 Outline

## In the News

- [Efron Award for the Bootstrap](https://www.nature.com/articles/d41586-018-07349-2)

## Probability Distributions

- `import numpy as np`


### Discrete Distributions

- Discrete Uniform
  - Can take any set of values, depending on those specified by the user. All values have equal probability.
  - `np.random.randint(low,high,size)`
    - Draws numbers from a discrete uniform distribution of integers between _low_ and _high_. _size_ indicates the number of values to draw.
  - `np.random.choice(arrayOfValues,size)`
    - Draws values from an array, by default with equal probability. This array can hold any type of variable. Again, _size_ indicates the number of values that are drawn.


        Someone is trying to convince you to gamble with them in a dice game. To
        convince you that their dice is not fake and has all six numbers on it,
        they give you the outcomes of 100 previous rolls.

        Are you willing to wager a serious amount of money in this game?

        rolls = np.array([4, 6, 5, 5, 5, 5, 2, 5, 1, 5, 1, 6, 5, 2, 2, 2, 1, 6,
        1, 2, 3, 2, 5, 6, 2, 2, 3, 1, 2, 3, 3, 1, 1, 4, 1, 2, 2, 5, 2, 1, 3, 2,
        1, 1, 5, 5, 1, 5, 2, 3, 1, 1, 3, 3, 4, 4, 4, 1, 1, 2, 2, 6, 4, 1, 4, 6,
        3, 2, 4, 1, 4, 2, 6, 1, 3, 6, 1, 5, 3, 1, 1, 3, 1, 5, 6, 3, 2, 1, 3, 3,
        2, 1, 6, 1, 3, 1, 5, 4, 2, 2])

        HINT: Try simulating rolls of a fair dice and comparing them to these
        outcomes. How are you doing the comparison?


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
