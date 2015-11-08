# -*- coding: utf-8 -*-

from textstat.textstat import textstat
import requests
from bs4 import BeautifulSoup
import re

""" Build the database """

# download each j! archive file so as not to be a jerk.
session = requests.session()
"""
for x in range(1,5090):
    exec("req = session.get('http://www.j-archive.com/showgame.php?game_id=%s')" % (x))
    exec("fullhtml = open('games/game_%s.html', 'w')" % (x))
    fullhtml.write(req.content)
    fullhtml.close()
"""

# cycle through each j! archive file on the local drive and turn it in to csvs
    # just get season, episode number, and answer
    #  ???, , .clue_text
    #Maybe just show number and each clue?  title and .clue_text?
"""
for x in range (1,5090):
    exec("metahtml = open('games/meta_%s.html', 'w')" % (x))
    exec("fullhtml = open('games/game_%s.html', 'r')" % (x))
    thisgame = BeautifulSoup(fullhtml, 'html.parser')
    title = thisgame.find('title')
    m = re.search('(?<=aired )\w+', str(title))
    if m:
        metahtml.write(m.group(0) + ". ")
        clue_text = thisgame.findAll("td",{"class":"clue_text"})
        if clue_text:
            for clues in clue_text:
                metahtml.write(clues.text.encode('utf8') + ". ")
            metahtml.close()
            fullhtml.close()
            print x, "is done"
        else:
            print "skipping", x, "for improper meta elements"
    else:
        print "skipping", x, "for improper meta elements"
"""


""" Evaluate the data """

# Organize the CSV so that all the seasons go together

# Lump all of the text of all of each season into one variable?
    # maybe also try just taking the reading level of each answer and then doing math to all of them?
    # print these to a separate CSV, I suppose…

# Find reading levels
    # https://pypi.python.org/pypi/textstat/
"""
thecsv = open('data.csv', 'w')
for x in range (1,5090):
#for x in range (1,10):
    exec("metahtml = open('games/meta_%s.html', 'r')" % (x))
    metatext = metahtml.read()
    if metatext:
        if (len(metatext) > 10):
            thereadability = textstat.automated_readability_index(metatext)
            year = metatext[:4]
            okayholdthis = str(year) + ", " + str(thereadability) + "\n"
            thecsv.write(okayholdthis)
    metahtml.close()
    print x, "is done"
"""

# Average it all



""" Send it to R? """
