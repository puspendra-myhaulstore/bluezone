from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template_string('''
        <h2>Upload an image</h2>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="file" multiple>
            <input type="submit" value="Upload">
        </form>
    ''')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return "No file selected."

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return "Uploaded successfully! Saved as: {file_path}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
