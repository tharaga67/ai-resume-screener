from flask import Flask, render_template, request, redirect, flash
from model.screener import get_resume_score
import os
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text

app = Flask(__name__)
app.secret_key = 'secret'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_desc = request.form['job_description']

    if resume_file and allowed_file(resume_file.filename):
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)

        resume_text = extract_text(filepath)
        score = get_resume_score(resume_text, job_desc)

        return render_template('result.html', score=score, filename=filename)
    else:
        flash('⚠️ Please upload a valid PDF file.')
        return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
