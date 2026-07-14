# Multi-Model-AI-System
An AI system that uses smart cameras (computer vision) to automatically spot product defects on factory lines, making sure everything is made perfectly without relying only on human eyes.

Week 1 — Python Basics
I got my coding environment ready on Google Colab and Kaggle to practice the basics of Python, like loops and functions. I wrote my first scripts and also read up on some basic machine learning theory.

Week 2 — Machine Learning Basics
This week was all about getting a feel for machine learning. I learned how to handle data using the Pandas library and studied different models up to bagging, figuring out how they actually train and get tested.

Week 3 — Deep Learning & CNNs
I jumped into deep learning and watched a video series to understand how Convolutional Neural Networks work. Since this project is about visual inspection, learning how these networks handle images was super important for the scanning part.

Week 4 — Intro to LLMs
I looked into Large Language Models to see how they are trained and used. Then, I started connecting the dots between these text models and the vision stuff from last week to build the final multi-modal quality check system.

Week 5 and 6: Exploratory Data Analysis and Computer Vision
For these two weeks, the focus shifted to data cleaning and actually training the computer vision model. I started with Exploratory Data Analysis on the NEU Surface Defect dataset to understand the distribution of the images and make sure the defect labels were accurate.

After prepping the data, I trained a YOLOv8 object detection model on Google Colab to recognize manufacturing flaws like scratches, crazing, and pitted surfaces. I experimented with different model sizes to find the best balance between speed and accuracy, and finally downloaded the best performing model weights to use in the final app.

Week 7 and 8: LLM Integration and Web Deployment
This was the final stretch where everything got tied together into a usable application. I built a web interface using Streamlit so an inspector can easily upload a photo of a steel sheet.

When a photo is uploaded, the custom YOLOv8 model scans the image and draws bounding boxes around any defects. It then passes those defect names and confidence scores to a local Llama 3.2 model running via Ollama. The LLM acts as the quality assurance expert and automatically writes a clean, professional inspection report detailing the severity of the damage and recommending maintenance actions.
