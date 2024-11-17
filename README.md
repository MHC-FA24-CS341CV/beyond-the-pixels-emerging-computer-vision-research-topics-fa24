{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN2VWV2AIB44yUu7E4/26Gq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MHC-FA24-CS341CV/beyond-the-pixels-emerging-computer-vision-research-topics-fa24/blob/main/README.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Analyzing Performance of SimCLR on Different Images\n",
        "\n",
        "The SimCLR model used for this study was trained by [Chen et al. (2020)](https://arxiv.org/abs/2002.05709) on the [ImageNet ILSVRC-2012](https://arxiv.org/abs/1409.0575) dataset. This is a dataset comprised of images from 1,000 object classes for a total of ~1.28 million available images. These images span a wide range of different classes, making the SimCLR pre-trained model ideal as a generalized image classifier.\n",
        "\n",
        "## Test Datasets\n",
        "\n",
        "The three example datasets used for testing come from [TensorFlow](https://www.tensorflow.org/datasets/catalog/overview?hl=en).\n",
        "1. The [`tf_flowers`](https://www.tensorflow.org/datasets/catalog/tf_flowers?hl=en) dataset is comprised of up-close images of flowers including sunflowers, dandelions, daisies, and tulips.\n",
        "2. The [`imagenette`](https://www.tensorflow.org/datasets/catalog/imagenette?hl=en) dataset is a subset of the ImageNet dataset and contains 10 different classes.\n",
        "3. The final test dataset is [`cifar100`](https://www.tensorflow.org/datasets/catalog/cifar100?hl=en) which consists of 100 classes and 20 superclasses. These images are significantly more blurred than that of the other two datasets.\n",
        "\n",
        "## Running the program\n",
        "\n",
        "The code is designed to be run in Google Colab. Open the [`.ipynb file`](https://github.com/MHC-FA24-CS341CV/beyond-the-pixels-emerging-computer-vision-research-topics-fa24/blob/main/code/13-self-supervised-learning/Self_Supervised_Learning.ipynbcan) in colab and select `Runtime -> Run all`. The process should take around 10 minutes depending on your GPU. The outputted images display the models’ predictions alongside the true labels.\n"
      ],
      "metadata": {
        "id": "5efxfhGnuOpx"
      }
    }
  ]
}