from flask import Flask, render_template, request, send_file, redirect
import os
from redactor import redact_file #redactor.py
import uuid #to gen unique filenames so as to not overwrite files

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #uploaded and redacted files stored here

# ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True) #creates folder if doesnt exsist

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files: #sees if file uploaded
        return "No file part"
    file = request.files['file']
    if file.filename == '':  # if no name (ie no file selected) error
        return "No selected file"

    # save original file
    file_ext = file.filename.split('.')[-1] #extracts file ext 
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], f"original_{uuid.uuid4()}.{file_ext}") #unique file name for every file to avoid conflict
    file.save(original_path)

    # redaction
    redacted_path = redact_file(original_path)

    return send_file(redacted_path, as_attachment=True) #redacted file downloads
    #return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
