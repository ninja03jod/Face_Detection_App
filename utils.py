import cv2

def draw_bounding_boxes(img, detections):
    """
    Draws bounding boxes and confidence scores on the image.
    
    Args:
    img: numpy array of the image.
    detections: A dictionary of detected faces and their corresponding details.
    
    Returns:
    img: numpy array of the image with bounding boxes and confidence scores.
    """
    for key, detection in detections.items():
        if 'facial_area' in detection and 'score' in detection:
            x1, y1, x2, y2 = detection['facial_area']
            score = detection['score']

            # Draw rectangle around the face
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Draw confidence score just above the bounding box
            label = f"{score:.2f}"
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            top = max(y1, label_size[1])
            cv2.putText(img, label, (x1, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return img

def save_image_with_bounding_boxes(img, file_name):
    """
    Saves the image with bounding boxes to the given file name.
    
    Args:
    img: numpy array of the image.
    file_name: The file name to save the image as.
    """
    cv2.imwrite(file_name, img)

def save_annotations_to_txt(detections, file_name):
    """
    Saves the bounding box coordinates and confidence scores to a .txt file.
    
    Args:
    detections: A dictionary of detected faces and their corresponding details.
    file_name: The file name to save the annotations as.
    """
    with open(file_name, 'w') as f:
        for key, detection in detections.items():
            if 'facial_area' in detection and 'score' in detection:
                x1, y1, x2, y2 = detection['facial_area']
                score = detection['score']
                # Format: class x1 y1 x2 y2 confidence
                f.write(f"face {x1} {y1} {x2} {y2} {score:.2f}\n")