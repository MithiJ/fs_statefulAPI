from flask import Flask, session, request
from flask_session import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/set')
def set():
    filepath = request.args.get('filepath')
    # URL: http://127.0.0.1:5000/set?filepath=xyz
    session['key'] = str(filepath)
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')