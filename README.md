# ESim
Let's simulate possible outcomes on number of times!

# USAGE
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
# ENJOY!
