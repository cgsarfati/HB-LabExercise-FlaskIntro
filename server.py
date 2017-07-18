"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['stupid', 'ugly', 'smelly']


@app.route('/')
def start_here():
    """Home page."""

    return """<!DOCTYPE html>
                <html>
                  <head> </head>
                    <body>
                      <a href="/hello"> Hi! This is the home page.</a>
                    </body>
                </html>"""


def add_words(list_of_comp):
    """ """

    comp_list = []
    for word in list_of_comp:
        comp_list.append("<option value='" + word + "'>" + word.title() + "</option>")

    return " ".join(comp_list)


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Select a compliment <select name="compliment">
            {}
            </select>
            <input type="submit" value="Submit"> </br>
        </form>
        <form action="/diss">
          Select an insult <select name="insult">
            {}
            </select>
            <input type="submit" value="Submit"> </br>
        </form>
      </body>
    </html>
    """.format(add_words(AWESOMENESS), add_words(INSULTS))


@app.route('/diss')
def diss_person():
    """ """

    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi you're {insult}!
      </body>
    </html>
    """.format(insult=insult)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
