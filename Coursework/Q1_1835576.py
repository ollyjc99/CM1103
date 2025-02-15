#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:02:17 2018

@author: olivercarter
"""

import csv
from numpy import random as r

def series_score(a, discard=1):
    for x in range(discard):
        a[1].pop(a[1].index(max(a[1])))
    print(sum(a[1]))
    #   discard is an optional parameter with a default value of 1
    #   This means that series_score() by default removes 1 race but
    
def sort_series(a):
    print(sorted(a, key=lambda x: x[1]))
	#Add the draw

def read_sailor_data():
    data = importing_csv_file('sailor_performances')
    sailors = {}
    #Reads the sailor performance CSV file and turns it into an ordered dictionary
    for people in data:
        if people !='':
            sailors.update({people[0]:(float(people[1]),float(people[2]))})
    return(sailors)
    
def importing_csv_file(filename):
	with open(filename+'.csv') as x:
		reader = csv.reader(x)
		data = [r for r in reader]
        #Opens CSV file which contains the sailor data
	return data
    #Returns data (names, mean performance & std deviation)    

def generate_performances(sailors):
	scores = {}
	for person in sailors:
		score = r.normal(sailors[person][0],sailors[person][1])
		scores.update({person : score})
	return scores

def calculate_finishing_order(sailor_scores):
	order = []
	for people in (sorted(sailor_scores.items(), key = lambda x: x[1], reverse=True)):
		order.append(people[0])
	return order

def simulate_races(races=6):
    #   races is an optional parameter which means that if nothing is entered then by default
    #   it runs 6 races, which means there is the option to chose the number of races to perform.
	results = {'Bob':[], 'Alice':[], 'Clare':[], 'Dennis':[], 'Eva':[]}
	for i in range(races):
		r = (calculate_finishing_order(generate_performances(read_sailor_data())))
		for person in r:
			results[person].append(r.index(person)+1)
	return results

def main():
    results = simulate_races()
    print(results)
    
if __name__ == '__main__':
	main()
