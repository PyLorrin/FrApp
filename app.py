#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('FrVoc.html')

if __name__ == '__main__':
    app.run()
