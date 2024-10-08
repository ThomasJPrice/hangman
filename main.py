from flask import Flask, render_template
import random

app=Flask(__name__)

WORDS = [
    "giraffe", "umbrella", "jungle", "computer", "science", 
    "ocean", "mountain", "elephant", "chocolate", "invisible", 
    "dynamic", "horizon", "pyramid", "balloon", "whisper", 
    "marathon", "crystal", "adventure", "festival", "library", 
    "mystical", "thunder", "jigsaw", "umbrella", "happiness", 
    "notebook", "chameleon", "acoustic", "discover", "journey", 
    "puzzle", "octopus", "freedom", "velocity", "whistle", 
    "quantum", "laptop", "telescope", "fantasy", "network", 
    "sapphire", "galaxy", "tornado", "lantern", "magnet", 
    "dragonfly", "symphony", "computer", "pancake", "trolley"
]


@app.route('/')
def home():
  active_word = random.choice(WORDS)
  return render_template('index.html', word=active_word)

app.run(debug=True)