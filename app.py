import os
from cgitb import html

from flask import Flask, render_template, request, send_from_directory
import pdfkit
import re

app = Flask(__name__)
app.config['PDF_FOLDER'] = 'static/pdf/'


@app.route('/')
def index():
    return render_template('/frontend/htmltopdf.html')


@app.route("/submit", methods=('GET', 'POST'))
def submit():
    if request.method == "POST":
        url_text = request.form['url']
        print(url_text)

        cleanurl = re.sub('\W+', '', url_text)
        pdffile = app.config['PDF_FOLDER'] + cleanurl + '.pdf'
        pdfkit.from_url(url_text, pdffile)

        fileDir = 'static/pdf/'
        filename = cleanurl + '.pdf'

        return send_from_directory(fileDir, filename ,as_attachment=True)
