# Week 14 Outline

## In the News

- [Efron Award for the Bootstrap](https://www.nature.com/articles/d41586-018-07349-2)

## Probability Distributions

- `import numpy as np`


### Discrete Distributions

- Discrete Uniform
  - `np.random.randint(low,high,size)`
    - Draws numbers from a discrete uniform distribution of integers
  - `np.random.choice(arrayOfValues,size)`
    - Draws values from an array, by default with equal probability.


        Someone is trying to convince you to gamble with them in a dice game. To
        convince you that their dice is not fake and has all six numbers on it,
        they give you the outcomes of 100 previous rolls.

        Are you willing to wager a serious amount of money in this game?

        rolls = np.array([4, 6, 5, 5, 5, 5, 2, 5, 1, 5, 1, 6, 5, 2, 2, 2, 1, 6,
        1, 2, 3, 2, 5, 6, 2, 2, 3, 1, 2, 3, 3, 1, 1, 4, 1, 2, 2, 5, 2, 1, 3, 2,
        1, 1, 5, 5, 1, 5, 2, 3, 1, 1, 3, 3, 4, 4, 4, 1, 1, 2, 2, 6, 4, 1, 4, 6,
        3, 2, 4, 1, 4, 2, 6, 1, 3, 6, 1, 5, 3, 1, 1, 3, 1, 5, 6, 3, 2, 1, 3, 3,
        2, 1, 6, 1, 3, 1, 5, 4, 2, 2])

        HINT: Try simulating rolls of a fair dice and comparing them to these outcomes.


- Bernoulli
  - This distribution takes the value 1 with probability p and the value 0 with probability 1-p. An outcome of 1 is often termed _success_ and 1-p termed _failure_. Think of a coin flip.
  - `np.random.binomial(size,n=1,p)`
  - The Bernoulli distribution is a special case of the binomial when there's only one trial (`n=1`).


- Binomial
  - This distribution models the number of successes in multiple Bernoulli trials, where the probability of success is p.
  - `np.random.binomial(size,n,p)`


  <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Binomial_distribution_pmf.svg" width=300>


- Poisson
  - This distribution models the number of events that occur in a given amount of time if there's a constant probability of an event occurring (for instance, the number of messages you receive if the senders are independent of one another).
  - `np.random.poisson(lambda,size)` - _lambda_ is the rate parameter of the Poisson. Higher rates result in more events per unit time or space.


  <img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Poisson_pmf.svg" width=300>

- Geometric

### Continuous Distributions

- Normal

- Exponential

- Chi-squared


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
