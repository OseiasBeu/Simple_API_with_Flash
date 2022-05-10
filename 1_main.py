from flask import Flask
app = Flask(__name__)

@app.route('/')
def beu_io():
    return "BEU_IO"

    