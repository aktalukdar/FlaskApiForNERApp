from flask import Flask,redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return redirect("https://ner-streamlit-app.herokuapp.com/")

if __name__=='__main__':
    app.run(debug=True)