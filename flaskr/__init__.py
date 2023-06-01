import json

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
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)
    return y


if __name__ == '__main__':
    app.run()