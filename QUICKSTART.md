# Quick Start Guide 🚀

Get the First Aid Assistant running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for installing packages)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Step-by-Step Setup

### 1. Navigate to Project Directory

```bash
cd first-aid-assistant
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or install individually
pip install Flask==3.0.0 Pillow==10.1.0 numpy==1.26.2
```

### 3. Run the Application

```bash
# Start the Flask server
python app.py
```

You should see output like:
```
======================================================
First Aid Assistant - Starting Server
======================================================

IMPORTANT NOTES:
- This is a DEMONSTRATION project
- Uses simple heuristics, not a trained ML model
- NOT for actual medical use
- Replace with trained model for production

Server running at: http://127.0.0.1:5000
======================================================
```

### 4. Open in Browser

1. Open your web browser
2. Navigate to: `http://127.0.0.1:5000`
3. You should see the First Aid Assistant interface

## Using the Application

### Upload an Image

**Option 1: Click to Upload**
1. Click the upload zone
2. Select an image file (PNG, JPG, JPEG, GIF, WEBP)
3. Click "Analyze Injury"

**Option 2: Drag & Drop**
1. Drag an image file from your computer
2. Drop it onto the upload zone
3. Click "Analyze Injury"

### View Results

After analysis, you'll see:
- **Injury Classification**: What type of injury was detected
- **Confidence Score**: How confident the system is (demo uses heuristics)
- **Immediate Steps**: First-aid instructions to follow
- **Warning Signs**: When to seek medical care
- **Additional Tips**: Extra care guidance

## Testing the System

### Method 1: Use the Test Script

```bash
# In a new terminal (keep server running in first terminal)
python test_api.py
```

This will run automated tests of all API endpoints.

### Method 2: Manual Testing

Try uploading images with different characteristics:
- **Reddish images** → May classify as cut or burn
- **Bluish images** → May classify as bruise
- **Other colors** → May classify as swelling or unknown

**Note**: The current demo uses simple color heuristics, not a trained AI model.

## Common Issues & Solutions

### Port Already in Use

If port 5000 is already in use:

```python
# Edit app.py, change the last line to:
app.run(debug=True, host='0.0.0.0', port=8080)
```

Then access at `http://127.0.0.1:8080`

### Package Installation Fails

Try using a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Images Not Uploading

Check:
1. File is a valid image format (PNG, JPG, JPEG, GIF, WEBP)
2. File size is under 16MB
3. Browser console for errors (F12 → Console tab)

### Module Not Found Error

Make sure you're in the right directory:

```bash
# Should see: app.py, classifier.py, first_aid_data.py, etc.
ls

# If not, navigate to project directory
cd path/to/first-aid-assistant
```

## Development Tips

### Run in Debug Mode

Debug mode is enabled by default and provides:
- Auto-reload on code changes
- Detailed error pages
- Debug toolbar

### View Logs

Server logs appear in the terminal where you ran `python app.py`

### Test API Directly

Using curl:

```bash
# Test info endpoint
curl http://127.0.0.1:5000/api/info

# Test with image (from file)
curl -X POST http://127.0.0.1:5000/api/analyze \
  -F "image=@path/to/image.jpg"
```

Using Python:

```python
import requests

# Analyze an image
with open('test_image.jpg', 'rb') as f:
    files = {'image': f}
    response = requests.post('http://127.0.0.1:5000/api/analyze', files=files)
    print(response.json())
```

## Next Steps

### 1. Explore the Code

- **app.py** - Flask routes and API endpoints
- **classifier.py** - Image classification logic
- **first_aid_data.py** - First-aid instructions database
- **templates/index.html** - Frontend interface

### 2. Customize First-Aid Instructions

Edit `first_aid_data.py` to:
- Add new injury categories
- Update instructions
- Change severity levels
- Modify disclaimers

### 3. Replace Demo Classifier

The current classifier uses simple heuristics. For production:

1. Collect labeled injury images
2. Train a CNN model (see README.md)
3. Replace `classify()` method in `classifier.py`
4. Test thoroughly

### 4. Enhance the Frontend

Edit `templates/index.html` to:
- Change colors and styling
- Add new features
- Improve mobile experience
- Add animations

### 5. Add Features

Ideas for enhancement:
- Save analysis history
- Multiple image comparison
- Video analysis
- Multi-language support
- PDF export of instructions
- Integration with emergency services

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Restarting the Server

```bash
python app.py
```

## Getting Help

1. Check the full README.md for detailed documentation
2. Review DEPLOYMENT.md for production setup
3. Run test_api.py to verify everything works
4. Check browser console (F12) for frontend errors
5. Check terminal for backend errors

## Important Reminders

⚠️ **This is a demonstration project**
- Uses heuristic classification (not AI/ML)
- NOT for actual medical use
- NOT a substitute for professional care
- Always call emergency services for serious injuries

✅ **Safe to experiment with**
- Try different images
- Modify the code
- Learn Flask and web development
- Build your ML/AI skills

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [NumPy Documentation](https://numpy.org/doc/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials) (for training models)

---

**Happy coding! 🎓**

Remember: This project demonstrates combining image processing and web development. It's a learning tool, not a medical device.
