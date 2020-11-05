#!/usr/bin/env python

import csv
import sys
import pprint

def csv_dict_list(variables_file):
    reader = csv.DictReader(open(variables_file, 'rb'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

def prediction(counties):
    candidates = {}
    for county in counties:
        reported = float(county['Reported'].strip('%')) / 100
        to_report = 1 - reported
        votes_left = (float(county['VotesCounted']) / reported) * to_report
        votes_to_gain = int(votes_left * float(county['Margin']) / 100 + 0.5)

        candidate = county['Candidate']
        if candidate not in candidates:
            candidates[candidate] = votes_to_gain
        else:
            candidates[candidate] += votes_to_gain

    first, second = sorted([(c, candidates[c]) for c in candidates], key=lambda x: -x[1])
    return {
        'candidate': first[0],
        'gain': first[1] - second[1] 
    }
 
votes_so_far = csv_dict_list(sys.argv[1])
gainer_and_gain = prediction(votes_so_far)
pprint.pprint(gainer_and_gain, indent=2, width=10)
