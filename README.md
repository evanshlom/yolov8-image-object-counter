# yolov8-detection-counter
Detected coco classes in an image then started a dataframe from the resulting labels.txt to count detections of each class in the image.

## How To
- **Environment**:
    - Run `pip install -r requirements.txt`
- **Program**:
    - Running `python main.py` will have the program...
        - 1. Download YOLO model.
        - 2. Detect COCO classes in the jpg image.
        - 3. Convert detections to pandas dataframe for data analysis.
        - 4. Print summary about the detections.
        - 5. Print counts of each class in the image.
