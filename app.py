from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import solutionGenerator

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image file from the request
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)

            # Get the true/false value from the radio button
            option = request.form['option']

            # Pass the image path and option to the solution generator module
            result = solutionGenerator.generate_solution(filepath, option)

            # Send the result back to the frontend
            return jsonify({'result': result})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
