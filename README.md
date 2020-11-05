# Vote Extrapolator

This is a very basic, back-of-the-envelope type predictor of election results
based on the incorrect premise that votes counted and votes yet to be counted will
have identical proportions between candidates.

## Example

The repo has [stats from Georgia taken from the NYTimes website](https://www.nytimes.com/interactive/2020/11/03/us/elections/results-georgia.html)
at around 23:00 UTC on 4th November 2020.
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
  'gain': 94354}
```

which suggests _only_ that Biden will gain 94354 votes in the counties described in `georgia-votes.csv`.

### Running your own

If you have custom data in another CSV in the same format,
say in a file called `arizona-votes.csv`, you can run the script as

```sh
python vote-extrapolator.py arizona-votes.csv
```