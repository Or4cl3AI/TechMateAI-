# TechMateAI

TechMateAI is a friendly and engaging conversational AI chatbot virtual assistant that can scan, diagnose, and fix the device it's downloaded on, perform basic security functions like password management and malware detection, and provide explanations in a way that a non-tech savvy person can understand.

## Requirements

* Python 3.7+
* Flask
* NLTK
* PyTorch
* SpeechRecognition
* Pandas
* Selenium
* PyAutoGUI
* Passlib
* Malwarebytes API

## Installation

1. Install the required libraries and frameworks.

pip install -r requirements.txt

2.Clone the repository.

git clone <https://github.com/Or4cl3AI/TechMateAI->,

3.Create a virtual environment and activate it.

python -m venv venv
source venv/bin/activate

4.Run the app.py file.

## Usage

The TechMateAI chatbot can be used by sending it messages in the chat interface. The chatbot will respond to your messages in a way that is both informative and engaging.

For example, you can ask the chatbot to scan your device for malware, generate a strong password, or explain how to fix a common computer problem.

## Deployment

To deploy the TechMateAI project to Heroku, follow these steps:

1. Create a new Heroku app: `heroku create your-heroku-app-name`
2. Set the Heroku API key as a secret in your GitHub repository settings. Name the secret `HEROKU_API_KEY` and set its value to your Heroku API key.
3. Push your code to the main branch. The GitHub Actions workflow will automatically trigger and deploy the application to Heroku.
4. Open the app in a web browser: `heroku open`
