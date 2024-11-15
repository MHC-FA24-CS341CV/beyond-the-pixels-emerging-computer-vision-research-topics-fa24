# Visual Question Answering with Clarification: A BLIP-2 Demo
This program demonstrates a basic Visual Question Answering (VQA) concept and introduces a clarification feature based on my research idea. The clarification feature addresses the challenge of ambiguity in questions, a common issue when humans interact with VQA systems. While existing VQA datasets generally assume that questions are clearly defined and lead to unique answers, real-world questions often include ambiguous expressions, vague references, or unspecified objects. 

In this program, ambiguous questions are defined as those containing vague pronouns (e.g., "it," "this," "that") or other general terms (e.g., "thing," "object") without sufficient contextual information. For instance:
  Ambiguous question:
  > "What is it?"
  Clarified question:
  > "What is it on the sofa?" 

This feature aims to handle these ambiguities by prompting the user for clarification when their question lacks sufficient context, thus improving the system's response accuracy. The model used is BLIP-2, proposed in the paper "[BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597)," and is implemented using the Hugging Face [transformers](https://huggingface.co/docs/transformers/en/index) library. 

**About BLIP-2:** Proposed in 2023, BLIP-2 builds upon Salesforce's 2022 BLIP model by using pre-trained image encoders and large language models (LLMs). This model achieves state-of-the-art performance on various vision-language tasks with fewer trainable parameters.

**About Hugging Face:** Hugging Face is a leading platform for AI and machine learning development. This program uses its `transformers` library, which supports state-of-the-art pre-trained models for tasks such as Natural Language Processing (NLP), Computer Vision, and more. This library integrates seamlessly with PyTorch, TensorFlow, and JAX, allowing developers to train, fine-tune, and deploy models with minimal effort while optimizing compute costs and resources. 

## Requirements
This program is designed to be run on Google Colab. For optimal runtime efficiency, enabling GPU support is highly recommended. Follow these steps to configure GPU settings:
  1. Go to `Runtime` > `Change runtime type`.
  2. Set `Hardware accelerator` to any available GPU (if you're using the free version of Colab, a T4 GPU is likely to be         your primary option).
Please note: For users on the free version, there are time limitations for GPU usage, and selecting a GPU does not guarantee that one will be allocated to you. For more details, visit the [Colab FAQ](https://research.google.com/colaboratory/faq.html).

## Dataset
This program uses the [VQA v2.0 dataset](https://visualqa.org/download.html), a significant benchmark dataset in computer vision and NLP. The dataset provides images, associated open-ended questions, and human-annotated answers. You'll need the following files:
  - `v2_OpenEnded_mscoco_val2014_questions.json` (Questions from *Validation questions 2017 v2.0**)
  * `v2_mscoco_val2014_annotations.json` (Annotations from *Validation annotations 2017 v2.0**)
  + `val2014.zip` (Images from *Validation images*)

To set up the required dataset:
  1. Use [this shared Google Drive link](https://drive.google.com/drive/folders/1ZGNVw2FkCzoyXPhuf_eLygYz6L4Ud4P5?usp=drive_link) to download these three files to your local computer. 
  3. Upload these three files to a suitable location in your Google Drive.

Note: In the program, you'll need to modify file paths to match the location where you've uploaded the files in your Google Drive. 

## Running the program
Once the dataset is uploaded and paths are adjusted, follow the instructions in each cell of the program. First, the program demonstrates the model's functionality using a specific cat image and its associated question/answer pairs, allowing you to observe the model's response.

In the final interactive section, you can ask your own questions about the image. If your question is ambiguous, the clarification feature will prompt you to refine your question by providing more context. Once clarified, the model generates a response based on the refined question.
