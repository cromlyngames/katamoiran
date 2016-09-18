#
#  https://exposit.github.io/katamoiran/articles/2016-09/txt-to-event-chart
#
#  Seed List Parser
#
#  Simple script to take text from a plain text file, sort it into rough parts of speech, and
# then save it as python lists and csv-formatted dXX charts for use in seeding 
#
#	Usage:
#
#		python seedparser.py <filename>
#
#	Flags:
#
#	    -x, --max	integer
#	    	Max number of elements in final lists. Set higher than target so you have extras for curated lists. Default 100.
#
#	    -m, --min	integer
#	    	Minimum length of words from source to include. Default is 4.
#
#	    -f, --fill	True or False
#		    Keep trying until the list is full (max 3x limiter), default is True
#
#	    -c, --case	u[pper] or l[ower
#	    	Results in title case or lowercase, default is lowercase
#
#	    -l, --lemmatize	True or False
#	    	Convert verbs to base form, default is True
#
#       -p, --proper  True or False
#           Include proper nouns, default is False.
#
#	    -t, --print	True or False
#	    	Print results to terminal, default is False
#


import nltk
from nltk import *
from nltk.stem.wordnet import WordNetLemmatizer

import os
import sys
import string
import time

import random
from random import sample

# a few logging variables
start_time = time.time()
paramstr = ""
wordcount = 0
usedcount = 0
total_string = ""

# declare defaults here
limiter = 110
repeat = True
case = 'lower'
lemmatize_verbs = True
include_proper_nouns = False
print_to_terminal = False
min_word_length = 4

try:
    filename = sys.argv[1]
except:
    print("\tUsage:\n\t\tpython seedparser.py <filename>")
    print("\tFlags:")
    print("\t-x, --max\tnumber\n\t\tMax number of elements in final lists. Set higher than target so you have extras for curated lists.")
    print("\t-f, --fill\tTrue or False\n\t\tKeep trying until the list is full (max 3x limiter), default is True")
    print("\t-c, --case\tu[pper] or l[ower\n\t\tResults in title case or lowercase, default is lowercase")
    print("\t-m, --min\tnumber\n\t\tMinimum length of words to include.")
    print("\t-l, --lemmatize\tTrue or False\n\t\tConvert verbs to base form, default is True")
    print("\t-p, --proper\tTrue or False\n\t\tInclude proper nouns, default is False")
    print("\t-t, --print\tTrue or False\n\t\tPrint results to terminal, default is False")
    sys.exit(1)
    
try:
    for i in range(1, len(sys.argv)):
        flag = sys.argv[i]
        parameter = sys.argv[i+1]
        if flag == '-f' or flag == '--fill':
            if parameter == 'False':
                repeat = False
        elif flag == '-c' or flag == '--case':
            if parameter == 'upper' or parameter == 'lower' or parameter == 'u' or parameter == 'l':
                case = parameter
        elif flag == '-l' or flag == '--lemmatize':
            if parameter == 'False':
                lemmatize_verbs = False
        elif flag == '-p' or flag == '--proper':
            if parameter == 'True':
                include_proper_nouns = True
        elif flag == '-t' or flag == '--print':
            if parameter == 'True':
                print_to_terminal = True
        elif flag == '-x' or flag == '--max':
            limiter = int(parameter)
        elif flag == '-m' or flag == '--min':
            min_word_length = int(parameter)
except:  
    pass
    
# set up lists
def parseFile(filename):

    words = []
    lines = []

    with open("." + os.sep + filename, 'r') as f:
        lines = f.readlines()

    adverbs = []
    adjectives = []
    nouns = []
    verbs = []

    postuples = word_tokenize(' '.join(lines))
    postuples = nltk.pos_tag(postuples)
    
    for word, pos in postuples:
        if len(word) >= min_word_length:
            if pos.startswith('J'):
                adjectives.append(word)
            if pos.startswith('V'):
                # convert to base form of the verb if requested
                if lemmatize_verbs == True:
                    word = WordNetLemmatizer().lemmatize(word,'v')
                verbs.append(word)
            if pos == 'NN' or pos == 'NNS':
                nouns.append(word)
            if pos == 'NNP' and include_proper_nouns == True:
                nouns.append(word + " (P)")
            if pos.startswith('RB'):
                adverbs.append(word)
    
    wordcount = len(postuples)
    usedcount = len(adverbs) + len(adjectives) + len(nouns) + len(verbs)
    
    return [adverbs, adjectives, nouns, verbs], wordcount, usedcount

# processing on the words in a list and saving
def processList(posList, limiter, wordtype, filename):

    nameList=["adverb", "adjective", "noun", "verb"]
    name = nameList[wordtype]
    
    try:
        filename, ext = filename.split('.')
    except:
        pass
    
    # standardize as lower case
    for i in range(len(posList)):
        if case == 'upper':
            posList[i] = string.capwords(posList[i])
        else:
            if posList[i].endswith('(P)') == False:
                posList[i] = posList[i].lower()
            else:
                posList[i] = posList[i].replace('(P)', '')
    
    # remove any duplicates
    posList = list(set(posList))

    tries = 0
    length = 0
    max_tries_exceeded = False
    while length < limiter and max_tries_exceeded == False:
        tries = tries + 1
        try:
            posList = sample(posList, limiter)
        except:
            #del posList[limiter:]
            pass
            
        length = len(posList)

        if tries > limiter*10:
            max_tries_exceeded = True
            
    posList.sort()

    # format as a list for using in python script
    format_py = '#!/usr/bin/env python \n # -*- coding: utf-8 -*-'
    format_py = 'chart = [\"' + '\", \"'.join(posList).replace('\n','') + "\"],"
    
    if print_to_terminal == True:
        print(format_py)

    # and save it
    with open("." + os.sep + filename + "_" + name + ".py", 'w') as f:
        f.write(format_py)

    # format as dXX table in comma-separated list
    format_csv = ""
    count = 0
    
    result = "\n" + string.capwords(name) + ":\n\t"
    
    for i in range(len(posList)):
        count = count + 1
        result = result + str(count) + ", " + posList[i].rstrip()
        if count % 5 == 0:
            result = result + "\n\t"
        else:
            result = result + ", "

    format_csv = result
    
    if print_to_terminal == True:
        print(format_csv)
    
    # and save it
    with open("." + os.sep + filename + "_" + name + ".csv", 'w') as f:
        f.write(format_csv)
        
    # now return a string for logging
    return " " + string.capwords(name) + "s [" + str(len(posList)) + "]"

# break the source file down into word lists sorted by type
typeList, wordcount, usedcount = parseFile(filename)

# process each word type
for i in range(len(typeList)):
    length = 0
    wordList = typeList[i]
    total_string = total_string + processList(wordList, limiter, i, filename)
    
# print a log of what happened and why
paramstr = "\nFile: " + filename + "\n" + "-"*50 + "\n\tfill: " + str(repeat) + "\n\tnumber of elements: " + str(limiter) + "\n\tcase: " + str(case) + "\n\tlemmatize: " + str(lemmatize_verbs) + "\n\tinclude proper nouns: " + str(include_proper_nouns) + "\n\tprint to terminal: " + str(print_to_terminal) + "\n\tminimum word length allowed: " + str(min_word_length)

print(paramstr)
print("-"*50)
print("Total Words: " + str(wordcount) + "\tSample Pool: " + str(usedcount) + "\n\t" + total_string)
print("\n--- in %s seconds ---" % (time.time() - start_time))

    
