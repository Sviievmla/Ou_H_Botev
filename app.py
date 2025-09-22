from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/documents'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index(): return render_template('index.html')

@app.route('/za-uchilishteto')
def about(): return render_template('about.html')

@app.route('/uchiteli')
def teachers(): return render_template('teachers.html')

@app.route('/novini')
def news(): return render_template('news.html')

@app.route('/galeria')
def gallery(): return render_template('gallery.html')

@app.route('/proekti')
def projects(): return render_template('projects.html')

@app.route('/dokumenty', methods=['GET', 'POST'])
def documents():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('documents'))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('documents.html', files=files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
