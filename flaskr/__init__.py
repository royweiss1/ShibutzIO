import json

import flask
from flask import Flask, render_template, request

import backend.mainGame


app = Flask(__name__)

@app.route('/leaderboards', methods=['GET'])
def leaderboards():
    # Sample leaderboard data
    leaderboard_data = [
        {'player': 'John Doe', 'score': 500},
        {'player': 'Jane Smith', 'score': 750},
        {'player': 'Mark Johnson', 'score': 900},
        {'player': 'Sarah Williams', 'score': 600}
    ]
    return render_template('leaderboards.html', leaderboard_data=leaderboard_data)
@app.route('/')
def index():
    return render_template('index.html')

uploaded_files = []

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            if file:
                #uploaded_files.append(file)
                # Convert Python file to text file
                text = file.read().decode("utf-8")
               # text_filename = file.filename + ".txt"
              #  with open(text_filename, 'w') as text_file:
              #      text_file.write(text)
                # Add text file to the list of uploaded files
                uploaded_files.append(text)
        backend.mainGame.main(uploaded_files)
        return "Files uploaded successfully!"

        #do stuff with the files

    return render_template('upload.html')


@app.route('/simulate_json')
def simulateJson():
    # some JSON:
    x = '[{"turnIndex": 1, "Score": {"0": 1, "1": 2, "2": 3, "3": 4}, "SquareChanges": [{"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 3}, {"xPosition": 2, "yPosition": 2, "playerIndex": 0, "Status": 3}, {"xPosition": 3, "yPosition": 3, "playerIndex": 1, "Status": 3}, {"xPosition": 4, "yPosition": 4, "playerIndex": 1, "Status": 3}, {"xPosition": 5, "yPosition": 5, "playerIndex": 0, "Status": 2}, {"xPosition": 6, "yPosition": 6, "playerIndex": 0, "Status": 2}, {"xPosition": 7, "yPosition": 7, "playerIndex": 1, "Status": 2}, {"xPosition": 8, "yPosition": 8, "playerIndex": 1, "Status": 2}, {"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 1}, {"xPosition": 2, "yPosition": 2, "playerIndex": 1, "Status": 1}, {"xPosition": 3, "yPosition": 3, "playerIndex": 2, "Status": 1}, {"xPosition": 4, "yPosition": 4, "playerIndex": 3, "Status": 1}]}, {"turnIndex": 2, "Score": {"0": 1, "1": 2, "2": 3, "3": 4}, "SquareChanges": [{"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 3}, {"xPosition": 2, "yPosition": 2, "playerIndex": 0, "Status": 3}, {"xPosition": 3, "yPosition": 3, "playerIndex": 1, "Status": 3}, {"xPosition": 4, "yPosition": 4, "playerIndex": 1, "Status": 3}, {"xPosition": 5, "yPosition": 5, "playerIndex": 0, "Status": 2}, {"xPosition": 6, "yPosition": 6, "playerIndex": 0, "Status": 2}, {"xPosition": 7, "yPosition": 7, "playerIndex": 1, "Status": 2}, {"xPosition": 8, "yPosition": 8, "playerIndex": 1, "Status": 2}, {"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 1}, {"xPosition": 2, "yPosition": 2, "playerIndex": 1, "Status": 1}, {"xPosition": 3, "yPosition": 3, "playerIndex": 2, "Status": 1}, {"xPosition": 4, "yPosition": 4, "playerIndex": 3, "Status": 1}]}]'

    # parse x:
    y = json.loads(x)
    response = flask.jsonify(x)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()