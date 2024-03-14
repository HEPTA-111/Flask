from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Route to render the file upload form
@app.route('/upload')
def upload_file():
    return render_template('upload.html')

# Route to handle file uploads
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_handler():
    if request.method == 'POST':
        # Access the uploaded file from the request object
        f = request.files['file']
        
        # Save the uploaded file to the server, ensuring a secure filename
        f.save(secure_filename(f.filename))
        
        # Display a success message upon successful file upload
        return 'File uploaded successfully'

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
