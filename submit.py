import os, gnupg
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from werkzeug import secure_filename
from pyPdf import PdfFileReader, PdfFileWriter

#This can handle the tmp folders
UPLOAD_FOLDER = 'data/'
EDITOR = 'bowserj@paroxysms.ca'

app = Flask(__name__)

@app.route("/")
def form():
    if(os.path.exists(UPLOAD_FOLDER)):
        return render_template('index.html')
    else:
        return render_template('maintenance.html')


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
        output.addPage(in_file.getPage(i))
    output_filename = os.path.join(UPLOAD_FOLDER, secure_filename(input_file.filename))
    outputStream = file(output_filename, "wb")
    output.write(outputStream)

# If we can load the file in memory, then encrypt, that'd be better
def encrypt_file(input_file):
    gpg = gnupg.GPG()
    fileStream = open(input_file)
    gpg_data = gpg.encrypt_file(fileStream, EDITOR)
    output = open(input_file + ".gpg", "w")
    output.write(str(gpg_data))
    output.close()
    os.remove(input_file)
    return redirect(url_for('success', filename=input_file))

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
                return encrypt_file(os.path.join(UPLOAD_FOLDER, filename))
                # return redirect(url_for('success',filename=filename))
            else:
                return redirect(url_for('fail',filename=filename))

if __name__ == "__main__":
    app.debug = True
    app.run()
