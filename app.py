from chatterbot import ChatBot
from flask import Flask, render_template, request
from assistant.assistant import TechMateAI

app = Flask(__name__)

assistant = TechMateAI()

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Serve as the main route for the Flask web application.

    This function is triggered when the client sends a request to the specified URL route.
    It returns a rendered HTML template as a response to the client's request.

    Returns:
        str: The rendered HTML template as the response to the client's request.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

app = Flask(__name__)

# Initialize the TechMateAI assistant
assistant = ChatBot('TechMateAI')

app = Flask(__name__)

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat() -> str:
    """
    Handle incoming chat messages and generate a response using the TechMateAI assistant.

    Returns:
        str: The generated response from the TechMateAI assistant.
    """
    # Extract the 'message' field from the request form
    message = request.form.get('message')

    # Generate a response using the TechMateAI assistant
    response = assistant.get_response(message)

    return str(response)

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run()
