# Week 7 and 8: LLM Integration and Web Deployment

This is the final phase of the project, where the standalone AI model gets turned into a fully functional web application. Instead of just running code in a google colab, I built a user interface using Streamlit so that an actual inspector could use this tool on the factory floor.

The application combines two completely different types of AI:
1. Computer Vision: When a user uploads an image of a steel sheet, the custom YOLOv8 model from week 6 scans it and draws bounding boxes around any surface defects.
2. Large Language Model (LLM): The app takes the names and confidence scores of the defects YOLO found, and feeds them into a local Llama 3.2 model. The LLM then acts as a quality assurance expert, writing a formatted inspection report that includes a summary, severity level, and recommended maintenance actions.

I chose to use Ollama to run the Llama model locally. This is a big advantage for industrial setups because the data never leaves the computer—it doesn't need an internet connection or a paid cloud API to generate the reports.

If you want to run this project on your own machine, follow these steps:

1. Download and run the local LLM
First, install Ollama from their website. Then, open your terminal and run this command:
ollama run llama3.2

https://drive.google.com/file/d/1N4iHh9SNt_yYRp2zmBhB55q4VtQye2FI/view?usp=sharing
Since the best.pt file is too large to upload to github, I've added it to a drive link and it is to be with the app.py file in order to streamlit to run localhost.

This tells Ollama to download the Llama 3.2 model to your computer. It is a few gigabytes, so let it run. Once it finishes and opens a chat prompt, just type /bye to exit. The model is now ready in the background.

2. Install the required Python packages
Make sure your terminal is inside this project folder, then run:
pip install -r requirements.txt

This reads the text file and installs all the necessary libraries like Streamlit (for the web app), Ultralytics (for YOLO), and OpenCV (for image processing). 

3. Start the application
With everything installed, start the local server by running:
python -m streamlit run app.py

I recommend using the "python -m" prefix here because it helps bypass common Windows PATH errors. 

Once the server starts, it will open a new tab in your browser where you can upload steel images and test the whole pipeline.
