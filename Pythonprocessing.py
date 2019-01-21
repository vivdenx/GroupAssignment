#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

## In python3,

import argparse, json, logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header):
    out=[]
    stdin = file == "-"
    file = 'years/' + file
    fd = sys.stdin if stdin else codecs.open(file, "r", "UTF-8")
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

if __name__ == "__main__":
    header = read_header()
    athletes = []# make list to fill with dictionaries
    for year in range(1800,2001): #For loop to go through each year in range 1800-2001(not including 2001)
        data = process_csv(str(year), header)#this was already in the code
        for person in data:# for loop to go through each person in the data 
            if 'description' in person and 'ice hockey' in str(person['description']).lower():#if there is a description entry, and if it has ice hockey in it. #Make description to string because it gave an integer error 
                dict_athlete={} # make dictionary to fill for each hockey player
                if 'rdf-schema#label' in person:# If there is an entry for this
                    dict_athlete['name']=person['rdf-schema#label'] # then save it as name in dictionary
                if 'birthYear' in person: # if there is a birthyear
                    dict_athlete['birthYear']=person['birthYear']# then add it to dictionary
                if 'birthDate' in person:# if there is a birthdate
                    dict_athlete['birthDate']=person['birthDate']#then add it to dictionary
                if 'rdf-schema#comment' in  person:# if there is an entry for this
                    descriptionWords = person['rdf-schema#comment'].lower().split() # then split comment in words
                    if 'he' in descriptionWords: #If he is in the comment then we take it as a male
                        dict_athlete['gender']='male'
                    elif 'she' in descriptionWords: # if she is in the comment then we take it as a female
                        dict_athlete['gender']='female'
                if 'birthPlace_label' in person: # if there is a brithplace entry 
                    dict_athlete['birthplace']=person['birthPlace_label'] # then add it to dictionary
                
                athletes.append(dict_athlete)# append the dictionary to the list of dictionary
                
    
    
# save into csv
import csv

header = ['name', 'birthYear', 'birthDate', 'gender', 'birthplace']
with open ('hockey_players.csv','w', encoding='utf-8') as file :
    writer = csv.DictWriter(file ,fieldnames=header, lineterminator ='\n', delimiter =',')
    writer.writeheader()
    for person in athletes :
        writer.writerow(person)







