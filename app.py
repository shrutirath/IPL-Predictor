from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)


#IPL_pred = pickle.load(open('IPLPred.pkl','rb'))


@app.route('/')
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port = 3000)