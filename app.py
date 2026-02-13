"""
First Aid Assistant - Flask Backend
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from classifier import create_classifier
from first_aid_data import FIRST_AID_INSTRUCTIONS, GENERAL_DISCLAIMER, SAFETY_EXCLUSIONS

app = Flask(__name__)
CORS(app)  # ADD THIS LINE
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Initialize classifier
classifier = create_classifier()

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_injury():
    """
    Analyze uploaded injury image
    Returns classification and first-aid instructions
    """
    try:
        # Check if image was uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload an image (PNG, JPG, JPEG, GIF, WEBP)'}), 400
        
        # Read image bytes
        image_bytes = file.read()
        
        # Classify the injury
        category, confidence, features = classifier.classify(image_bytes)
        
        # Get first-aid instructions for this category
        instructions = FIRST_AID_INSTRUCTIONS.get(category, FIRST_AID_INSTRUCTIONS['unknown'])
        
        # Prepare response
        response = {
            'success': True,
            'classification': {
                'category': category,
                'name': instructions['name'],
                'confidence': confidence,
                'severity': instructions['severity']
            },
            'instructions': {
                'immediate_steps': instructions['immediate_steps'],
                'warning_signs': instructions['warning_signs'],
                'when_to_seek_help': instructions['when_to_seek_help'],
                'additional_tips': instructions.get('additional_tips', [])
            },
            'disclaimer': GENERAL_DISCLAIMER,
            'safety_exclusions': SAFETY_EXCLUSIONS
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get general information about the system"""
    return jsonify({
        'supported_categories': list(FIRST_AID_INSTRUCTIONS.keys()),
        'disclaimer': GENERAL_DISCLAIMER,
        'safety_exclusions': SAFETY_EXCLUSIONS,
        'model_info': {
            'type': 'Demo heuristic-based classifier',
            'note': 'This is a demonstration. In production, use a trained deep learning model.',
            'training_recommendation': classifier.get_training_recommendation()
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'first-aid-assistant'})

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    print("=" * 60)
    print("First Aid Assistant - Starting Server")
    print("=" * 60)
    print("\nIMPORTANT NOTES:")
    print("- This is a DEMONSTRATION project")
    print("- Uses simple heuristics, not a trained ML model")
    print("- NOT for actual medical use")
    print("- Replace with trained model for production")
    print("\nServer running at: http://127.0.0.1:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
