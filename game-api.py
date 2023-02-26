from flask import Flask, request, jsonify
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route('/play', methods=['POST'])
def play():
    # Get user choice from request body
    user_choice = request.json.get('choice')

    # List of possible choices
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # Check if user's choice is valid
    if user_choice not in choices:
        return jsonify({'error': 'Invalid choice!'}), 400

    # Choose a random computer choice
    computer_choice = random.choice(choices)

    # Determine the winner based on the rules of the game
    if user_choice == computer_choice:
        result = 'tie'
    elif user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard'):
        result = 'win'
    elif user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock'):
        result = 'win'
    elif user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard'):
        result = 'win'
    elif user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'spock'):
        result = 'win'
    elif user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissors'):
        result = 'win'
    else:
        result = 'lose'

    # Return the result
    response = jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    }), 200

    return response

if __name__ == '__main__':
    app.run(debug=False)
