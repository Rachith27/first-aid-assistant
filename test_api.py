"""
Test Script for First Aid Assistant - Python 3.14 Compatible
Tests API endpoints and classifier functionality
"""

import requests
import json
from PIL import Image
import io

BASE_URL = "http://127.0.0.1:5000"

def test_health_check():
    """Test the health check endpoint"""
    print("\n" + "="*60)
    print("Testing Health Check Endpoint")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 200
        print("✓ Health check passed")
    except Exception as e:
        print(f"✗ Health check failed: {e}")

def test_info_endpoint():
    """Test the info endpoint"""
    print("\n" + "="*60)
    print("Testing Info Endpoint")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/api/info")
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Supported Categories: {data['supported_categories']}")
        print(f"Model Type: {data['model_info']['type']}")
        assert response.status_code == 200
        print("✓ Info endpoint passed")
    except Exception as e:
        print(f"✗ Info endpoint failed: {e}")

def create_test_image(color_type='red'):
    """Create a synthetic test image using pure Python"""
    # Create image with solid color for testing
    if color_type == 'red':
        # Red-dominant image (simulating cut/burn)
        img = Image.new('RGB', (224, 224), color=(200, 80, 80))
    elif color_type == 'blue':
        # Blue-dominant image (simulating bruise)
        img = Image.new('RGB', (224, 224), color=(80, 80, 150))
    else:
        # Random-ish image
        img = Image.new('RGB', (224, 224), color=(120, 120, 120))
    
    # Add some variation to make it more realistic
    pixels = img.load()
    for i in range(0, 224, 10):
        for j in range(0, 224, 10):
            if color_type == 'red':
                pixels[i, j] = (220, 60, 60)
            elif color_type == 'blue':
                pixels[i, j] = (60, 60, 180)
    
    # Convert to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def test_analyze_endpoint(color_type='red', description='red-dominant'):
    """Test the analysis endpoint with a synthetic image"""
    print("\n" + "="*60)
    print(f"Testing Analysis Endpoint ({description})")
    print("="*60)
    
    try:
        # Create test image
        test_image = create_test_image(color_type)
        
        # Send request
        files = {'image': ('test.png', test_image, 'image/png')}
        response = requests.post(f"{BASE_URL}/api/analyze", files=files)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if data['success']:
                classification = data['classification']
                instructions = data['instructions']
                
                print(f"\nClassification Results:")
                print(f"  Category: {classification['category']}")
                print(f"  Name: {classification['name']}")
                print(f"  Confidence: {classification['confidence']:.2%}")
                print(f"  Severity: {classification['severity']}")
                
                print(f"\nFirst-Aid Steps ({len(instructions['immediate_steps'])} steps):")
                for i, step in enumerate(instructions['immediate_steps'][:3], 1):
                    print(f"  {i}. {step}")
                
                print(f"\nWarning Signs ({len(instructions['warning_signs'])} signs):")
                for i, warning in enumerate(instructions['warning_signs'][:2], 1):
                    print(f"  - {warning}")
                
                print("\n✓ Analysis successful")
            else:
                print(f"✗ Analysis returned error: {data.get('error')}")
        else:
            print(f"✗ Request failed with status {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"✗ Analysis failed: {e}")

def test_invalid_file():
    """Test with invalid file type"""
    print("\n" + "="*60)
    print("Testing Invalid File Handling")
    print("="*60)
    
    try:
        # Create a text file instead of image
        text_file = io.BytesIO(b"This is not an image")
        files = {'image': ('test.txt', text_file, 'text/plain')}
        response = requests.post(f"{BASE_URL}/api/analyze", files=files)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 400:
            print("✓ Correctly rejected invalid file")
        else:
            print("✗ Should have rejected invalid file")
    
    except Exception as e:
        print(f"Error during test: {e}")

def test_no_file():
    """Test with no file uploaded"""
    print("\n" + "="*60)
    print("Testing No File Handling")
    print("="*60)
    
    try:
        response = requests.post(f"{BASE_URL}/api/analyze")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 400:
            print("✓ Correctly rejected missing file")
        else:
            print("✗ Should have rejected missing file")
    
    except Exception as e:
        print(f"Error during test: {e}")

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print("FIRST AID ASSISTANT - TEST SUITE (Python 3.14 Compatible)")
    print("="*70)
    print("\nMake sure the Flask server is running on http://127.0.0.1:5000")
    print("Start server with: python app.py")
    print("\nStarting tests...")
    
    # Run tests
    test_health_check()
    test_info_endpoint()
    test_analyze_endpoint('red', 'red-dominant (potential cut/burn)')
    test_analyze_endpoint('blue', 'blue-dominant (potential bruise)')
    test_analyze_endpoint('random', 'random colors')
    test_invalid_file()
    test_no_file()
    
    print("\n" + "="*70)
    print("TEST SUITE COMPLETED")
    print("="*70)
    print("\nNote: This is a demo system using heuristic classification.")
    print("For production use, replace with a trained deep learning model.")
    print("This version is optimized for Python 3.14 compatibility.")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_all_tests()
