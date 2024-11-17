Run Instructions: To execute the Colab notebook for the
project, follow these steps:
Dataset Preparation: Upload the dataset to a Google Drive
folder. Ensure images are in a compatible format (e.g., .jpg or
.png) and structured into training and validation directories.
Google Colab Setup: Mount Google Drive by running the
provided from google.colab import drive command. Provide
the appropriate path to access the dataset from Google Drive.
Environment Setup:
Install the necessary libraries such as TensorFlow, NumPy,
OpenCV, and any other dependencies listed in the notebook.
Running the Code: Execute the notebook cells sequen-
tially: Data Preprocessing: Converts the dataset to Lab color
space and prepares training data. Model Training: Trains the
CNN model to predict a and b channels from the L channel.
Evaluation: Uses the test dataset to predict colorized outputs
of the grayscale images.
Visualizing Results: Generated images can be visualized
directly in the notebook or saved back to Google Drive for
offline access.

Link to reference code: https://www.kaggle.com/code/basu369victor/image-colorization-basic-implementation-with-cnn
Link to dataset used: https://www.kaggle.com/datasets/abhikalpsrivastava15/space-images-category
