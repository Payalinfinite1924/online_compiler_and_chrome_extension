# Online Compiler Chrome Extension

This project is an **Online Compiler Chrome Extension** that allows users to write and execute code directly from their browser. It supports **Python**, **Java**, and **C++** programming languages. The extension interacts with a backend server built using **Flask** to compile and run the code, and displays the results directly in the popup.

---

## Features

- **Supports Multiple Languages**: Python, Java, and C++.
- **Real-Time Output**: Get immediate feedback of your code execution in the popup.
- **Cross-Platform**: Works seamlessly across all platforms (Windows, macOS, Linux).
- **Interactive UI**: Simple and easy-to-use interface for writing and running code.

---

## Demo

You can view a live demo of the project on the Chrome Web Store once it's uploaded, or you can try it locally by following the steps below.

---

## Table of Contents

- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Installation

### 1. Download the Repository

First, clone the repository to your local machine:
git clone https://github.com/payalinfinite1924/online-compiler-chrome-extension.git

### 2. Set Up the Backend
This extension requires a Flask server to execute the code. Here are the steps to set up the server:

#### Navigate to the backend folder:
-bash
-Copy
-cd backend
#### Install dependencies:
-bash
-Copy
-pip install -r requirements.txt
#### Run the Flask server:
-bash
-Copy
-python app.py
-The backend will be accessible at http://localhost:5000.

### 3. Install the Extension Locally

Open Chrome and go to the chrome://extensions/ page.
Turn on Developer Mode in the top-right corner.
Click on Load unpacked and select the extension folder (online-compiler-chrome-extension).
The extension will now be installed, and you can use it from the Chrome toolbar.
How It Works
The extension uses a popup interface where users can select the language and write their code.

Upon submitting the form, the code is sent to a Flask backend (via AJAX), which executes the code in the selected language.
The output or error message is then returned to the extension and displayed in the popup.
### Backend Technologies:
Flask: Lightweight Python web framework.
Subprocess: Used to run code on the server and capture output.
CORS: Allows requests from the Chrome extension to the Flask backend.
Regex: Used to extract the class name from Java code.
#### Supported Languages:
Python: Runs Python scripts.
Java: Compiles and runs Java programs.
C++: Compiles and runs C++ programs.
### Usage
Write Code: Open the extension's popup and write your code in the provided text area.
Select Language: Choose between Python, Java, or C++.
Run Code: Click on Run Code, and the output or error message will appear in the result box below the text area.
### Features
Real-time code execution: Get immediate feedback for your code in Python, Java, and C++.
Responsive UI: The extension’s interface is designed to be user-friendly and simple.
Developed by Payal: A personal project to enhance coding skills and demonstrate the power of Chrome Extensions.
### Contributing
We welcome contributions! If you'd like to improve the extension, here’s how you can help:

Fork the repository.
Clone your fork to your local machine.
Create a branch for your feature or bug fix.
Submit a Pull Request with a clear description of your changes.
### Guidelines:
Follow the PEP 8 guidelines for Python code.
Ensure your code is well-documented.
Write tests for new features or bug fixes.
### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements
Flask: Web framework for Python.
CORS: Cross-Origin Resource Sharing support for Flask.
Subprocess: For executing code from the backend.
Regex: Used to extract Java class names.
### Contact
If you have any questions or need support, feel free to reach out to the project maintainer.

Email: payal24102003@gmail.com
LinkedIn: [https://www.linkedin.com/in/payal-kumari-5432235](https://in.linkedin.com/in/payal-kumari-543ba2235)

### Important Notes:
This extension uses a backend server (Flask) for running code. You need to deploy or run this server locally for the extension to function.
The extension can also be improved with additional features such as supporting more programming languages, adding a code editor like Monaco Editor, or integrating with cloud-based code execution services.
How to Update the Extension:
When making changes to your extension, update the manifest.json and popup.html files.
Zip the new version and upload it again to the Chrome Web Store if you want to update it for other users.
