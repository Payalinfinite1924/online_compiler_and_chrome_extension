import subprocess
import os
from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)

# Directory to save the source code temporarily
CODE_DIR = "temp_code"

# Ensure the directory exists
if not os.path.exists(CODE_DIR):
    os.makedirs(CODE_DIR)
import os

def remove_all_files_in_directory(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file (not a subdirectory)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Failed to remove {file_path}. Error: {e}")

# Example usage: Remove all files in the specified directory


def extract_class_name(java_code):
    # Define the regex pattern
    pattern = r'class\s+(\w+)'
    
    # Search for the class name using regex
    match = re.search(pattern, java_code)
    
    if match:
        return match.group(1)  # Return the class name
    else:
        return None  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    user_code = request.form['code']
    language = request.form['language']
    
    # Save the code to a file based on the selected language
    if language == 'python':
        remove_all_files_in_directory(CODE_DIR)
        file_path = os.path.join(CODE_DIR, 'abc.py')
        with open(file_path, 'w') as code_file:
            code_file.write(user_code)
        # Run the Python code
        result = run_python(file_path)
    
    elif language == 'java':
        print(extract_class_name(user_code))
        remove_all_files_in_directory(CODE_DIR)
        file_path = os.path.join(CODE_DIR, f'{extract_class_name(user_code)}.java')
        with open(file_path, 'w') as code_file:
            code_file.write(user_code)
        # Compile and run the Java code
        result = run_java(file_path,extract_class_name(user_code))
    
    elif language == 'cpp':
        remove_all_files_in_directory(CODE_DIR)
        file_path = os.path.join(CODE_DIR, 'abc.cpp')
        with open(file_path, 'w') as code_file:
            code_file.write(user_code)
        # Compile and run the C++ code
        result = run_cpp(file_path)
    
    return jsonify(result)

def run_python(file_path):
    try:
        result = subprocess.run(['python', file_path], check=True, capture_output=True, text=True)
        return {'output': result.stdout, 'error': result.stderr if result.stderr else None}
    except subprocess.CalledProcessError as e:
        return {'output': None, 'error': e.stderr}

def run_java(file_path,name):
    try:
        # Compile the Java code
        compile_result = subprocess.run(['javac', file_path], check=True, capture_output=True, text=True)
        if compile_result.returncode == 0:
            # Run the compiled Java program
            java_result = subprocess.run(['java', '-cp', CODE_DIR, name], check=True, capture_output=True, text=True)
            return {'output': java_result.stdout, 'error': java_result.stderr if java_result.stderr else None}
        else:
            return {'output': None, 'error': compile_result.stderr}
    except subprocess.CalledProcessError as e:
        return {'output': None, 'error': e.stderr}

def run_cpp(file_path):
    try:
        # Compile the C++ code
        compile_result = subprocess.run(['g++', file_path, '-o', 'abc'], check=True, capture_output=True, text=True)
        if compile_result.returncode == 0:
            # Run the compiled C++ program
            cpp_result = subprocess.run(['./abc'], check=True, capture_output=True, text=True)
            return {'output': cpp_result.stdout, 'error': cpp_result.stderr if cpp_result.stderr else None}
        else:
            return {'output': None, 'error': compile_result.stderr}
    except subprocess.CalledProcessError as e:
        return {'output': None, 'error': e.stderr}

if __name__ == '__main__':
    app.run(debug=True)
