import pandas as pd

from model import predict
from class_ids import class_dict

predict("img1.jpg")

labels = pd.read_csv('runs\detect\predict\labels\img1.txt', sep=' ', header=None)


# labels.head()
print("raw object detections sample (5):")
print(labels.head())

# Count number of objects detected
print("number of objects detected", len(labels))

# Get class names
labels['class'] = labels[0].map(class_dict)

# Print unique classes detected
print("unique classes detected", labels['class'].unique())

# Count number of detections for each detected class
print("number of detections for each detected class:")
print(labels['class'].value_counts())