# Week 5 and 6: Exploratory Data Analysis and Computer Vision

During these two weeks, the main goal was to move from understanding our raw data to actually training a custom object detection model on it. 

Before touching any AI models, I spent time on Exploratory Data Analysis (EDA) and data cleaning. For an image dataset like this, EDA isn't just about spreadsheets; it involves looking at the distribution of the images, checking for class imbalances (making sure we don't have 1,000 images of scratches but only 10 images of crazing), and ensuring the bounding box labels correctly line up with the defects. 

Once the data was prepped, I moved on to the computer vision phase. I chose to use the YOLOv8 architecture because it is incredibly fast and highly accurate for real-time object detection. I trained the model on the NEU Surface Defect Database from Kaggle using Google Colab, since training on a local laptop takes too long. 

I experimented with a few different model sizes (like YOLOv8-nano and YOLOv8-medium) to find the right balance between how fast the model runs and how accurately it detects the steel defects. 

Here is how the final model performed:
Precision: 0.712 
Recall: 0.735
mAP@50: 0.804
mAP@50-95: 0.481

Inside this folder, you will find a "metrics_screenshots" directory containing the training curves, the confusion matrix, and some sample predictions to show how the model learns over time. The actual trained model weights are saved here as best.pt.

