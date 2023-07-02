```python
from flask import Flask, render_template, request
from assistant.assistant import TechMateAI

app = Flask(__name__)

assistant = TechMateAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = assistant.get_response(message)
    return response

if __name__ == '__main__':
    app.run()
```