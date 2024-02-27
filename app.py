from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form['command']

    # Input validation to prevent command injection
    if ';' in command:
        return 'Invalid command', 400

    try:
        output = subprocess.check_output(command, shell=True)
        return output
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)



flask
