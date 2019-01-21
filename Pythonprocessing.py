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
    athletes = []
    for year in range(1800,2001):
        data = process_csv(str(year), header)
        for person in data:
            if 'description' in person and 'ice hockey' in str(person['description']).lower():
                dict_athlete={}
                if 'rdf-schema#label' in person:
                    dict_athlete['name']=person['rdf-schema#label']
                if 'birthYear' in person:
                    dict_athlete['birthYear']=person['birthYear']
                if 'birthDate' in person:
                    dict_athlete['birthDate']=person['birthDate']
                if 'rdf-schema#comment' in  person:
                    descriptionWords = person['rdf-schema#comment'].lower().split()
                    if 'he' in descriptionWords:
                        dict_athlete['gender']='male'
                    elif 'she' in descriptionWords:
                        dict_athlete['gender']='female'
                if 'birthPlace_label' in person:
                    dict_athlete['birthplace']=person['birthPlace_label']
                
                athletes.append(dict_athlete)
                
    
    

import csv

header = ['name', 'birthYear', 'birthDate', 'gender', 'birthplace']
with open ('hockey_players.csv','w', encoding='utf-8') as file :
    writer = csv.DictWriter(file ,fieldnames=header, lineterminator ='\n', delimiter =',')
    writer.writeheader()
    for person in athletes :
        writer.writerow(person)







