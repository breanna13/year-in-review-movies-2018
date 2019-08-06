#!/usr/bin/env python
from urllib import request
import random
import requests
import urllib
import time
from datetime import date
import sys
import re
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)