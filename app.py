import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from model import load_model
from utils import draw_bounding_boxes, save_image_with_bounding_boxes, save_annotations_to_txt

def main():
    st.title("Face Detection Web App")

    # Sidebar for image uploads
    st.sidebar.header("Upload Images")
    uploaded_images = st.sidebar.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_images:
        model = load_model()

        all_scores = []
        for uploaded_image in uploaded_images:
            # Load image
            img = Image.open(uploaded_image)
            img_cv2 = np.array(img.convert('RGB'))  # Convert PIL image to cv2

            # Perform face detection
            detections = model.detect_faces(img_cv2)

            # Calculate and collect confidence scores
            scores = [detection['score'] for detection in detections.values()]
            all_scores.extend(scores)
            
            # Draw bounding boxes and display
            img_with_boxes = draw_bounding_boxes(img_cv2.copy(), detections)
            st.image(img_with_boxes, caption=f"Image with Bounding Boxes: {uploaded_image.name}", use_column_width=True)

            # Prepare downloads
            # Save images with bounding boxes
            img_with_boxes_pil = Image.fromarray(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
            buffered = BytesIO()
            img_with_boxes_pil.save(buffered, format="JPEG")
            st.download_button(
                label=f"Download Image with Bounding Boxes ({uploaded_image.name})",
                data=buffered.getvalue(),
                file_name=f"{uploaded_image.name.split('.')[0]}_with_boxes.jpg",
                mime="image/jpeg"
            )

            # Save annotations to .txt
            annotations_txt = f"{uploaded_image.name.split('.')[0]}_annotations.txt"
            save_annotations_to_txt(detections, annotations_txt)
            with open(annotations_txt, "rb") as file:
                st.download_button(
                    label=f"Download Annotations ({uploaded_image.name.split('.')[0]}_annotations.txt)",
                    data=file,
                    file_name=annotations_txt,
                    mime="text/plain"
                )

        # Display overall "accuracy" based on confidence scores
        if all_scores:
            overall_accuracy = np.mean(all_scores)
            st.sidebar.write(f"Overall Confidence Score (as accuracy proxy): {overall_accuracy:.2f}")

if __name__ == "__main__":
    main()