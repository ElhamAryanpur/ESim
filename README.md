# ESim
Let's simulate possible outcomes on number of times!

## USAGE
First of all, import it (DUH!)
`import ESim`

then assign a var to it

`s = ESim.Simulation()`

And now assign two arguments:
`s.PO = 2`
`s.TIMES = 100`
PO means Possible Outcomes which is how many possible choices is avaliable there.
and TIMES means how many times to run the simulation.

then run it:
`result = s.run()`

it returns a json object with each keys being the number of POs and values being how many times they were choosed! from above example, the data returned may look like: {0: 20, 1: 80}

From now on you know what to do with the data!

## VERSION 2 DOCS:
Version 2.0 was _added_ to bring advance simulations right in your hands! I have not deleted the first version, but rather called new version as v2. This version gives more options to tweak as you like:

1. PO_v2 (required): This is different Possible outcome as you would pass a list to this one! Rather than saying how many possible outcomes like in last version, now you will explicitly say which possible outcomes to choose!

EXAMPLE: `Simulation.PO_v2 = [0, 1]`

2. SIMS: Simulations (sims for short) is used to tell how many simulations to run in each times! so this will be below level of `TIMES` option. In math words, `SIMS` and `TIMES` are two dimentional matrix for your simulation results.

EXAMPLE: `Simulation.SIMS = 10`

3. BASE_SIZE (not required but recommended for accurate results): Now this is fun. What you need to specify in here is the how many times to the 10 your possible outcomes are below of. For example, your possible outcomes are 4 and 9; in this case, your BASE_SIZE will be 10 as all your possible outcomes are below digit 10! Or suppose your possible outcomes are 25, 488, 1, and 892; in this case, all the numbers are below 1000 BASE_SIZE. The bigger the BASE_SIZE, the bigger your simulation range will be! so try to adjust it for accurate results!

EXAMPLE: `Simulation.BASE_SIZE = 10`

4. run_v2: To run the new version simulation, just call `Simulation.run_v2()` function. Eazy Peazy Lemon Squezy!

5. extra: This function will turn raw result from run_v2 to simple result! just call `Simulation.extra()`!

These are all new features for version 2.0 other changes are:

1. Result lists: Now instead of `run()` returning results, the results will be stored in 4 different types of JSON-like objects: `string_result`, `int_result`, `raw_result`, and `simple_result`. as their name:

    1. `string_result` will save result's keys and values as strings. like: {"0": ["5", "2"]}

    2. `int_result` will save result's keys and values as integers. like: {0: [5, 2]}
    
    3. `raw_result` will save version two result's keys and values.
    
    4. `simple_result` will turn raw result into simple result. it will add all values and save all occurence as whole in the value of possible outcomes

The version 1 of simulation result will be saved on `string_result` and `int_result`. and the version 2 of simulation result will be saved on `string_result` and `raw_result`. The string result from version 2 will only turn keys as strings.

## HAVE PROBLEM OR NEED HELP

hit me up on [Facebook](https://www.facebook.com/elham.aryanpur.10)

## ENJOY
