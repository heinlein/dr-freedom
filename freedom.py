#!/usr/bin/python
#
# Written by Paul Heinlein. Use, modify, or share this code as you
# see fit. Attribution is nice but not necessary.
#
# ======================================================================

import argparse
from datetime import date

parser = argparse.ArgumentParser(
  description = "Calculate time to reach Rob Berger's 7 Levels of Financial Freedom"
)

parser.add_argument( '-p', '--percent', type = float, default = 10.0,
  help = "Percentage of after-tax income saved [default: 10.0]" )
parser.add_argument( '-d', '--dollar', type = float, default = 0.00,
  help = "Dollar savings aka the latte effect [default: 0]" )
parser.add_argument( '-r', '--rate', type = float, default = 5.0,
  help = "Investment rate of return [default: 5.0]" )
parser.add_argument( '-i', '--income', type = int, default = 2500,
  help = "After-tax income [default: 2500]" )
parser.add_argument( '-s', '--start', type = int, default = 0,
  help = "Starting savings level [default: 0]" )

args = parser.parse_args()

### define rob's terms of engagement

# rob's levels of freedom
savings = [
  "1 month", "3 months", "6 months", "1 year",
  "5 years", "10 years", "25 years"
]

# those savings timeframes expressed as number of months
levels = [ 1, 3, 6, 12, 60, 120, 300 ]

### sling-shot effect

mysavings  = (args.income * (args.percent / 100.00)) + args.dollar
myexpenses = args.income - mysavings

### generate target dollar amounts based on those levels

targets = []
for i in levels:
  targets.append( myexpenses * i )

### a solitary subroutine, necessary because python has no standard
### library that allows simple month arithmatic.

def addmonths(months):
  start = date.today()
  y = start.year
  m = start.month
  d = start.day
  # rule out pathological cases like Feb 30
  if d > 28: d = 28
  mydate = date(y, m, d) 

  for x in range(months):
    y = mydate.year
    m = mydate.month
    d = mydate.day

    newmonth = m + 1
    if newmonth < 13:
      mydate = mydate.replace( month = newmonth )
    else:
      mydate = mydate.replace( year = (y + 1), month = 1 )

  return mydate

### main routine

mylevel = 0
bank = args.start

# banner
print( "Achieving Rob Berger's Levels of Financial Freedom" )
print( "" )

# header information
print ("Data used:" )
print ("* Monthly income:   %8d"      % args.income )
print ("* Percent saved:    %11.2f%%" % args.percent )
print ("* Dollars saved:    %11.2f"   % args.dollar )
print ("* Rate of return:   %11.2f%%" % args.rate )
print ("* Starting savings: %8d"      % bank )
print ("* Monthly expenses: %8d"      % myexpenses )
print ("* Monthly savings:  %8d"      % mysavings )
print ("")

# report on any levels already achieved
for i in range(len(targets)):
  if bank > targets[i]:
    mydesc = savings[i]
    mytgt  = targets[i]
    mylevel += 1
    print("Level %d: %8s expenses ($%8d) ACHIEVED" % (mylevel, mydesc, mytgt))

# report on estimated dates for reaching other targets
mymonth = 0
while bank < targets[-1]:
  mymonth += 1
  mytgt = targets[mylevel]
  # compound interest rate
  bank *= (1 + ((args.rate / 100.00) / 12.00))
  # add savings
  bank += mysavings
  if bank > mytgt:
    mydesc = savings[mylevel]
    then = addmonths(mymonth)
    mylevel += 1
    print("Level %d: %8s expenses ($%8d) estimated %s" % (mylevel, mydesc, mytgt, then))

