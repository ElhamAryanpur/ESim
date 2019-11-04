# This is where you get help understanding [WebApp Version](index.html)

The ESim is a program allowing you to run simulations according to data you
provide. The aim is to be able to run simulations as cheap, fast and easy as
possible. And now thanks to [Brython Project](https://brython.info/) you can run
simulations on the browser!

## Terms

While using the ESim, you will stumble upon many terms that might confuse you,
here is a list of them and explaining of what they are:

1. `Possible Outcomes`: Is what numbers are consider as outcomes. must be comma
   seperated.
2. `Base Of Possible Outcomes`: Is what you specify below which `10 to the power` of
   your outcomes exist. For example, if your outcomes be `1` and `4`, your base
   would be `10`. if your outcomes be `5` and `25` then your base become `100`.
3. `Times To Run`: is how many rounds to run simulations.
4. `Simulations Per Time`: is how many simulations to do per each round.
5. `Raw Result`: Is result of simulation uncompressed.
6. `Simple Result`: Is result of simulation compressed.

That is all you need to know.

## Usage

Upon loading the page, you will be presented with default data that you can
test. Default data contain 2 `PO` (Possible Outcomes), with `BASE` of 10,
running 100 `TIMES` and doing 10 `Simulations per time`. Default results is
choosen as `Simple Result` that shows a `JSON` of result.

Upon clicking the `RUN` button, you will see the `{ RESULTS }` text below change
to numbers looking like: `{0: 96, 1: 100}`.

The default data can be used to run simuations 1000 times and result can be used
on questions like `Would this happen or that`, which then you can use `0` or `1`
to get answers.

```
NOTE: This project will not be responsible for anything happening in the future
or past or present! This is pure work of randomness which depends on time you are and thus not be taken serious at all costs!
```

You can start using by click on [this](./index.html)