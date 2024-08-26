# Face_Detection_App

## Project Overview
This project is a face detection application that leverages the `RetinaFace` model for detecting faces in images. The application is designed as a web app using Streamlit, where users can upload one or more images, and the app will process these images to detect faces, draw bounding boxes with confidence scores, and allow users to download the processed images and their corresponding annotations.

## Key Features
- Face Detection: Detects faces in uploaded images using the RetinaFace model.
- Bounding Boxes: Draws bounding boxes around detected faces with associated confidence scores.
- Downloadable Outputs: Users can download processed images with bounding boxes and corresponding annotations in .txt format.
- User Interface: Built with Streamlit for a simple and interactive user experience.

## File Structure
`app.py`: The main file that runs the Streamlit web application. It handles the user interface, image uploads, and calls the functions for face detection, drawing bounding boxes, and saving the results.

`model.py`: Contains the function to load the RetinaFace model. This file abstracts the model loading, making it easy to switch models if needed.

`utils.py`: Provides utility functions for:

- Drawing bounding boxes and confidence scores on images.
- Saving images with bounding boxes.
- Saving bounding box coordinates and confidence scores to a .txt file for annotations.

`requirements.txt`: Lists all the Python dependencies required to run the project, including Streamlit, OpenCV, and RetinaFace.

## Installation and Setup

### 1. Clone the Repository:
```
git clone https://github.com/ninja03jod/Face_Detection_App.git
cd Face_Detection_App
```

### 2. Create Virtual Environment:
```
python -m venv venv
venv\Scripts\activate
```

### 3.Install the Required Dependencies:
```
pip install -r requirements.txt
```

### 4. Run the Application:
```
streamlit run app.py
```

## Usage

- Upload Images: Use the sidebar to upload one or more images that you want to process.

- View Results: The application will display the images with bounding boxes and confidence scores around detected faces.

- Download Outputs: You can download the processed images with bounding boxes and the corresponding annotations in a .txt file.

## Code Documentation

### The codebase is structured into three main files:

`app.py`: The main Streamlit application file. It handles user interactions, image uploads, and displays results.

`model.py`: Contains the model loading function. It utilizes the RetinaFace model for face detection.

`utils.py`: Includes utility functions for drawing bounding boxes and saving annotations.

## Code Structure

#### 1. `app.py`:

- `upload_images`: Handles image uploads and displays results.
- `display_images`: Shows images with bounding boxes and confidence scores.
- `download_files`: Provides options for downloading annotated images and text files.

#### 2. `model.py`:

- `load_model`: Loads and returns the RetinaFace model.

#### 3. `utils.py`:

- `draw_bounding_boxes`: Draws bounding boxes and confidence scores on images.
- `save_annotations`: Saves face detection results in .txt format.

## Report

### Approach
The application uses the `RetinaFace` model for face detection, which provides high accuracy in detecting faces in various conditions. The model is integrated with a Streamlit interface for ease of use.

### Design Decisions

#### Model Choice: 
RetinaFace was selected for its accuracy and robustness in face detection.
#### Interface Design: 
Streamlit was chosen for its simplicity and ease of building interactive web applications.
#### Annotation Format: 
Annotations are saved in .txt format to provide a simple and universally readable format for detected face coordinates.

### Challenges
#### Selecting Algo:
Gone through lots of Blogs and various algo like mtcnn, dnn, yunuet and finally got algorithm which converges and trains and give fastest inference.
#### Confidence Score Clarity: 
Adjusting the display of confidence scores to ensure they are clear and visible.
#### Multiple Image Handling: 
Ensuring that the application handles multiple image uploads and provides accurate results for each image.

## Test Results

#### Accuracy: 
The RetinaFace model demonstrates high accuracy in detecting faces with a high confidence score.
