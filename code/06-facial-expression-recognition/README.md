# Facial Expression Recognition: Bias Detection Using Clustering

### Description
This project explores biases in facial expression recognition (FER) systems using the UTKFace dataset. By applying unsupervised clustering on extracted facial features, the analysis highlights racial imbalances in the dataset and demonstrates how these biases affect the representation of underrepresented groups, such as Black individuals. The project leverages K-Means clustering and the elbow method to determine optimal clusters and evaluates how facial features are distributed across these clusters.

## Features
- **Data Preprocessing**: Resize and normalize facial images, extract metadata (age, gender, race).
- **Feature Extraction**: Utilize a pre-trained ResNet50 model to obtain latent facial features.
- **Clustering**: Perform K-Means clustering to group images based on latent feature similarity.
- **Bias Detection**: Analyze ethnicity distributions within clusters to identify dataset imbalances.
- **Visualization**: Generate scatterplots, ethnicity tables, and sample images for analysis.

## Requirements
This program is designed to be run on Google Colab. For optimal runtime efficiency, enabling GPU support is highly recommended. Follow these steps to configure GPU settings:
  1. Go to `Runtime` > `Change runtime type`.
  2. Set `Hardware accelerator` to any available GPU (if you're using the free version of Colab, a T4 GPU is likely to be your primary option).
     
Please note: For users on the free version, there are time limitations for GPU usage, and selecting a GPU does not guarantee that one will be allocated to you. For more details, visit the [Colab FAQ](https://research.google.com/colaboratory/faq.html).



## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. **Install Required Libraries**:
   Run the following commands to install dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn tensorflow keras kagglehub
   ```

You do not have to download the dataset because I have code withing the Colab that gets it directly from Kaggle

3. **Run the Notebook**:
   Open the Colab notebook in your browser or run locally
   ```

4. **Dataset**:
   Download the UTKFace dataset from [Kaggle](https://www.kaggle.com/datasets/jangedoo/utkface-new) and place it in the appropriate folder:
   ```plaintext
   data/UTKFace/
   ```

## Attribution
This project was inspired by principles of bias detection in facial recognition systems and draws on clustering methods outlined in the Scikit-Learn documentation, Towards Data Science articles, and related literature.
