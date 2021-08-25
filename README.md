# Monte Carlo simulations

Monte Carlo methods or otherwise known as simulations are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results - `N.T. Thomopoulos' “Essentials of Monte Carlo Simulation: Statistical Methods for Building Simulation Models”`

### estimate_pi.py

Let's estimate the the value of pi using Monte Carlo simulations.

Given a circle of radius **r = 1**, inside of a square that has the **l = 2**.

![Image of circle](https://ggcarvalho.dev/img/posts/montecarlo/circle.png)

If you draw points at random inside the area of the circle, some of them would be in the circle and some would be outside of the circle.

![](https://ggcarvalho.dev/img/posts/montecarlo/pi_simulation.gif)

The area of the circle is `π * r**2`.
The area of the square is `(2r)**2` or `4r**2`.

A value will fall inside the region of the circle if the value of `x**2 + y**2 < 1`.

We can prove it like so:

- generate 2 random numbers in the range of -1 to 1
- if (x ** 2) + (y ** 2) < 1, add one to a success value
- repeat this for N trials

Running the function will show that value of pi estimated by the simulation has a very low percentage of error. Initially the error rate is very high but after 10_000 trials it fluctuates around the value of pi.

```
Simulation ran for 1 points
Approx pi value: 4.0
Error % : 27.32395447351627%
Simulation ran for 10001 points
Approx pi value: 3.1392860713928608
Error % : 0.07342079165790977%
Simulation ran for 20001 points
Approx pi value: 3.1406429678516075
Error % : 0.03022943592322458%
Simulation ran for 30001 points
Approx pi value: 3.1368287723742543
Error % : 0.15163904875112647%
Simulation ran for 40001 points
Approx pi value: 3.1409214769630758
Error % : 0.021364215565961714%
Simulation ran for 50001 points
Approx pi value: 3.151296974060519
Error % : 0.30889811445277177%
Simulation ran for 60001 points
Approx pi value: 3.1554807419876334
Error % : 0.44207158372269634%
Simulation ran for 70001 points
Approx pi value: 3.1361837688033027
Error % : 0.17217015007689884%
Simulation ran for 80001 points
Approx pi value: 3.1422607217409784
Error % : 0.021265269716679323%
Simulation ran for 90001 points
Approx pi value: 3.139965111498761
Error % : 0.05180627377557591%
```

### estimate_euler.py

Lex Fridman made this interesting post, let's see if we can prove this using Monte Carlo simulations.

We can prove it like so:

- generate a random number in the range of 0 to 1
- add the random number to a moving total and add a count of 1 to moving number of selections
- if the total >= 1 add the number of selections to a list, set the total and selection to 0
- repeat this for N trials

![Lex Fridman Post](https://ggcarvalho.dev/img/posts/montecarlo/lex.png)

After running 1_000_000 trials we can see that the percentage of error is nearly 0%

```
Running 1000000 experiments
Expected # 2.716805359718973
Error % : 0.05431624950047546%
```

### birthday_paradox.py

    In a group of 23 people, the probability of a shared birthday exceeds 50%.

We can prove it like so:

- generate a list of random numbers in the range of 0 to 364(for all the days in a year)
- out of the entire list of random numbers if there are any non-unique numbers add 1 to our success value
- repeat this for N amount of trials
- get the probability of a shared birthday by dividing the number of successes by the number of trials

```
Probability : 0.499916 %
```

## Acknowledgements

- [Gabriel G. Carvalho](https://ggcarvalho.dev/), this repository is a port of his post [The art of solving problems with Monte Carlo simulations](https://ggcarvalho.dev/posts/montecarlo/) in Python.
