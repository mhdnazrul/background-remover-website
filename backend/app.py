from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No image part", 400

    file = request.files['image']
    
    if file.filename == '':
        return "No selected file", 400

    try:
        # Open the input image file
        inp = Image.open(file.stream).convert("RGB")

        # Remove the background
        output = remove(inp)

        # Save the output image to a BytesIO object
        img_byte_arr = io.BytesIO()
        output.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return send_file(img_byte_arr, mimetype='image/png')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
