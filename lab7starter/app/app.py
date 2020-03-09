'''
Created on Jan 20, 2020

@author: CS6252
'''
from flask import Flask
app = Flask(__name__)


@app.route('/synonyms')
def get_all_synonyms():
    all_synonyms = {"family": ["class" , "category", "folk", "kinsfolk", "fellowship"],
        "eat": ["consume", "use up", "deplete", "exhaust", "feed"],
        "house": ["household", "home", "firm", "mansion", "put up", "domiciliate"]}
    return all_synonyms

@app.route('/synonym/<string:word>')
def get_synonym(word):
    all_synonyms = {"family": ["class" , "category", "folk", "kinsfolk", "fellowship"],
        "eat": ["consume", "use up", "deplete", "exhaust", "feed"],
        "house": ["household", "home", "firm", "mansion", "put up", "domiciliate"]}
    if word in all_synonyms.keys():
        return {word: all_synonyms[word]}
    else: 
        return {"message": "No synonyms available for " + word} 