from flask import Flask, render_template
import random
import pandas as pd

app=Flask(__name__)

df = pd.read_csv('static/WordList.csv', header=None)
dfArr = df[0].to_list()

WORDS = []

for i in dfArr:
  WORDS.append(i.lower())
  
@app.route('/')
def home():
  active_word = random.choice(WORDS)
  return render_template('index.html', word=active_word)

app.run(debug=True)