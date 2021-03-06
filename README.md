# Vote Extrapolator

This is a very basic, back-of-the-envelope type predictor of election results
based on the incorrect premise that votes counted and votes yet to be counted will
have identical proportions between candidates.

## Example

The repo has [stats from Georgia taken from the NYTimes website](https://www.nytimes.com/interactive/2020/11/03/us/elections/results-georgia.html)
at around 00:30 UTC on 5th November 2020.
They've been sanitised as a CSV file with the following columns:

```csv
County,Candidate,Margin,PartyMargin,Reported,VotesCounted,AbsenteeCounted
```

To run the example is simple:

```sh
make
```

This will output the conclusion

```json
{ 'candidate': 'Biden',
  'gain': 83053}
```

which suggests _only_ that Biden will gain 94354 votes in the counties described in `georgia-votes.csv`.

### Sanitisation

I sanitised a copy-and-paste from the website using a hasty Regex in a find-and-replace.

```perl
\s+(\w+)\s+\+(\d+)\s+([RD]\+\d+.\d)\s+\n(\d+%)\n+\s+(\d{1,3}),(\d{3})\s+(\d{1,3}),(\d{3})
```

and later upgraded to

```perl
\s*(\w+)\s*\+(\d+|\d+.\d+)\s*([RD]\+(?:\d+.\d|\d+|\d+.\d+))(?:\s|\n)*(\d+%)(?:\n|\s)*(\d{1,3})?,?(\d{3})\s+(\d{1,3})?,?(\d{3})
```

In both cases, the output was `,$1,$2,$3,$4,$5$6,$7$8`.

I don't like it either.

### JSON approach

As NYTimes are updating their pages with huge (~200kB) JSON files, it is an option to simply

```sh
curl https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/state-page/georgia.json -o georgia.json
```

And process the data from there instead.

### Running your own

If you have custom data in another CSV in the same format,
say in a file called `arizona-votes.csv`, you can run the script as

```sh
python vote-extrapolator.py arizona-votes.csv
```