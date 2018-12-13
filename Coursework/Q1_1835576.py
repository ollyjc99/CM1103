#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:02:17 2018

@author: olivercarter
"""

import csv
import matplotlib.pyplot as plt
from numpy import random as r
from random import randint
from collections import Counter

def series_score(a, discard=1):
    for x in range(discard):
        a[1].pop(a[1].index(max(a[1])))
    print(sum(a[1]))
    #   discard is an optional parameter with a default value of 1
    #   This means that series_score() by default removes 1 race but
    
def sort_series(a):
    print(sorted(a, key=lambda x: a))

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

def gen_counts(standing):
	count = []
	count_out = []
	for s in standing:
		count.append(int(standing[s]))
	data = (Counter(count))
	for numbers in data:
		count_out.append([numbers,data[numbers]])
	return count_out

def plot_graph():
    
    standing = (generate_performances(read_sailor_data()))
    
    x=[]; y=[]
    
    s_count = sorted(gen_counts(standing))
    print(s_count)
    for items in s_count:
        x.append(items[0])
        y.append(items[1])

    plt.plot(x, y, 'ro')
    plt.title('Score')
    plt.xlabel('Skill')
    plt.ylabel('Frequency of people that got Race Score')
    #   Labels the x and y axis of the graph
    
    plt.axis([min(x), max(x)*1.1, min(y), max(y)*1.1])
    #   plots the x and y axis of the graph
    
    plt.show()

def graph_add_sailor(loops):
    with open('sailor_performances For Graphs.csv', mode='w') as x:
        writer = csv.writer(x)
     #   writer.writerow([name,mean performance,std dev])
        for i in range(loops):
            writer.writerow(['Example'+str(i), randint(0,100), 20,])

def main():
    results = simulate_races()
    print(results)
    
if __name__ == '__main__':
	main()
