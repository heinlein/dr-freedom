# Financial Freedom

In the [Dough Roller](https://www.doughroller.net/) podcast number 296,
Rob Berger describes what he calls the seven levels of financial freedom.
His definition is based on your monthly expenses. You reach the first
level of financial freedom, for example, when you have saved an amount
equal to one month of your expenses. There are seven levels, all based
on saving a multiple of your current expenses:

1. one month of expenses
2. three months of expenses
3. six months of expenses
4. one year of expenses
5. five years of expenses
6. ten years of expenses
7. 25 years of expenses

Rob emphasizes that these levels are *not* based on income but on
expenses.

The python script in this repository lets you generate various scenarios
to see how long it might take you reach each level given

* the percentage of your after-tax income you save
* your expected rate of return on investments

## Dollars and Percentages

Rob also mentions the possibility of "the latte effect," or how your
savings level changes if, for example, you give up your daily latte and
add it to your savings.

The trick with dollar-specific savings is that they don't map cleanly to
percentages. If someone is saving $125 per month by percentage and she
decides to give up her $75-per-month coffee habit, that's fairly hefty
percentage increase in savings. If she had been saving $600 per month,
the extra $75 is a smaller percentage increase.

To deal with dollar-specific savings, I had to use specific dollar
amounts of income, expenses, and savings. I also added an option so
you can build your scenarios around savings you've already accumulated.

Here's the upshot: if all you want to do is see time scenarios based
on percentage of income saved, the dollar amounts don't matter. The
timeframes for reaching each level will be identical.

If you want to specify current accumulated savings or add extra
dollar-specific savings, then you'll need to use real dollar amounts
to generate useful scenarios.

## Rate of Return

For most savers, return on investments won't alter too much the time
it takes to reach the three or four levels of freedom; that's especially
true if your money sits in a savings or money-market account.

By the time you reach the higher levels, interest rates to come into
play, so the program also includes an option to generate scenarios
based on different rates of return.

## Default values

Here are the default values built into the script:

* Monthly after-tax income: $2500
* Percent saved: 10.00%
* Monthly expenses: $2250
* Monthly savings: $250
* Starting savings: $0
* Additional dollars saved: $0
* Rate of return: 5.00%

Each of those values can be tweaked to generate different scenarios.

## Installation Note

Users of Macs or Linux systems will almost certainly have the Python
interpreter installed; it can be used from any terminal program.
Windows users will have to research [how to install
Python](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)
for themselves.

I've tested the code with Python 2.7 and 3.6; either version should work.

Also of note: this is a character-based program. There is no fancy
windowing system. This is quick-and-dirty code.

## Examples

Here's the output of the program using the default assumptions. It
was generated on April 3, 2018, in case you're interested to know
the timeframes involved. If you save 10% of your income with a 5%
rate of return, it will take roughly 50 years to reach level seven!

```nohighlight
[bash]$ python freedom.py
Achieving Rob Berger's Levels of Financial Freedom

Data used:
* Monthly income:       2500
* Monthly expenses:     2250
* Monthly savings:       250
* Starting savings:        0
* Percent saved:       10.00%
* Dollars saved:        0.00
* Rate of return:       5.00%

Level 1:  1 month expenses ($    2250) estimated 2019-01-03
Level 2: 3 months expenses ($    6750) estimated 2020-06-03
Level 3: 6 months expenses ($   13500) estimated 2022-05-03
Level 4:   1 year expenses ($   27000) estimated 2025-10-03
Level 5:  5 years expenses ($  135000) estimated 2041-12-03
Level 6: 10 years expenses ($  270000) estimated 2052-06-03
Level 7: 25 years expenses ($  675000) estimated 2068-07-03
```

Here's a different run using a 15% savings rate and 8% return on
investments. As Rob notes in the podcast, increasing the savings
rate boosts the amount you save *and* reduces your expenses. In
this scenario, it takes only 31 years to reach level seven. Quite
the improvement!

```nohighlight
[bash]$ python freedom.py --percent 15 --rate 8.0
Achieving Rob Berger's Levels of Financial Freedom

Data used:
* Monthly income:       2500
* Monthly expenses:     2125
* Monthly savings:       375
* Starting savings:        0
* Percent saved:       15.00%
* Dollars saved:        0.00
* Rate of return:       8.00%

Level 1:  1 month expenses ($    2125) estimated 2018-10-03
Level 2: 3 months expenses ($    6375) estimated 2019-09-03
Level 3: 6 months expenses ($   12750) estimated 2020-11-03
Level 4:   1 year expenses ($   25500) estimated 2023-01-03
Level 5:  5 years expenses ($  127500) estimated 2033-03-03
Level 6: 10 years expenses ($  255000) estimated 2039-10-03
Level 7: 25 years expenses ($  637500) estimated 2049-11-03
```

Finally, here is an example using most of the options: 15% savings rate,
$150 in additional ("latte") savings, return rate on investments of 7.5%,
monthly after-tax income of $4,000, and a preexisting savings account
with $87,500.

In this case, our hypothetical saver has reached the fourth level of
financial freedom, with the seventh level still 22 years in the future.

```nohighlight
[bash]$ python freedom.py -p 15 -d 150 -r 7.5 -i 4000 -s 87500
Achieving Rob Berger's Levels of Financial Freedom

Data used:
* Monthly income:       4000
* Monthly expenses:     3250
* Monthly savings:       750
* Starting savings:    87500
* Percent saved:       15.00%
* Dollars saved:      150.00
* Rate of return:       7.50%

Level 1:  1 month expenses ($    3250) ACHIEVED
Level 2: 3 months expenses ($    9750) ACHIEVED
Level 3: 6 months expenses ($   19500) ACHIEVED
Level 4:   1 year expenses ($   39000) ACHIEVED
Level 5:  5 years expenses ($  195000) estimated 2023-11-03
Level 6: 10 years expenses ($  390000) estimated 2030-05-03
Level 7: 25 years expenses ($  975000) estimated 2040-07-03
```

## All the Knobs

Here's the program's help screen so you can see all the knobs
you can adjust.

```nohighlight
usage: freedom.py [-h] [-p PERCENT] [-d DOLLAR] [-r RATE] [-i INCOME]
                  [-s START]

Calculate time to reach Rob Berger's 7 Levels of Financial Freedom

optional arguments:
  -h, --help            show this help message and exit
  -p PERCENT, --percent PERCENT
                        Percentage of after-tax income saved [default: 10.0]
  -d DOLLAR, --dollar DOLLAR
                        Dollar savings aka the latte effect [default: 0]
  -r RATE, --rate RATE  Investment rate of return [default: 5.0]
  -i INCOME, --income INCOME
                        After-tax income [default: 2500]
  -s START, --start START
                        Starting savings level [default: 0]
```

