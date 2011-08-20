import os
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from werkzeug import secure_filename
from pyPdf import PdfFileReader, PdfFileWriter

TMP_FOLDER = '/media/dropdrive'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)

@app.route("/")
def form():
    if(os.path.isfile("tmp/dropfile")):
        return render_template('index.html')
    else:
        return render_template('maintenance.html')

def allowed_file(filename):
    return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/fail")
def fail(filename):
    return render_template('fail.html')

# This removes the metadata, funny enough
# If anyone knows a faster way, please let me know
def write_pdf_data(input_file):
    in_file = PdfFileReader(input_file)
    output = PdfFileWriter()
    num_pages = in_file.getNumPages()
    #Copy the pages
    for i in range(0, num_pages):
        output.addPage(input.getPage(i))
    output_filename = os.path.join(UPLOAD_FOLDER, secure_filename(input_file.filename))
    outputStream = file(output_filename, "wb")
    output.write(outputStream)


@app.route("/submit/", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["document"]
        if file:
            #Do unspeakable things to the pdf before it sees human eyes
            filename = secure_filename(file.filename)
            doctype = filename.rsplit('.', 1)[1]
            success = False
            if(doctype == "pdf"):
                write_pdf_data(file)
                success = True
            else:
                success = True
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            if(success):
                return redirect(url_for('success',filename=filename))
            else:
                return redirect(url_for('fail',filename=filename))

if __name__ == "__main__":
    app.debug = True
    app.run()
