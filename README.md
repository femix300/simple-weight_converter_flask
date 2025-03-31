# Flask Weight Converter App

A simple web application built with Flask that converts weights between **KG**, **LB**, and **OZ**. This app features a modern, Discord-inspired dark UI with responsive design and a clean interface.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)

## Features
- **Weight Conversion:**  
  Convert weights from one unit to another (KG, LB, OZ) with accurate calculations.
- **Responsive UI:**  
  A modern dark-themed interface inspired by Discord, using custom CSS and Google Fonts.
- **Form Data Retention:**  
  The user’s input is retained after form submission to provide a better user experience.
- **Error Handling:**  
  Provides validation for user input to ensure only valid numbers are processed.

## Demo
Check out the live app on Railway:  
[Live Demo URL](https://web-production-89c2.up.railway.app/)  


## Installation

### Prerequisites
- Python 3.x installed on your system.
- [pip](https://pip.pypa.io/en/stable/) for installing Python packages.
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/) for creating a virtual environment.

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/femix300/simple-weight_converter_flask.git
    cd simple-weight_converter_flask
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running Locally
To run the Flask Weight Converter app on your local machine:
```bash
    python app.py
```
Then, navigate to http://127.0.0.1:5000 in your web browser to use the app.


## Deployment

### Deploying on Railway

This project is set up for deployment on Railway. Follow these steps:

1. **Push your project to GitHub.**
2. **Log in to Railway** and create a new project from your GitHub repository.
3. Ensure the build command is set to:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the start command is set to:

    ```bash
    gunicorn app\:app
    ```

5. **Deploy the project** and share the live URL with your friends!
