# Visual Question Answering Demo with BLIP-2 and Clarification Feature
This program demonstrates a basic Visual Question Answering (VQA) concept and introduces a clarification feature based on my research idea. The clarification feature addresses the challenge of ambiguity in questions, a common issue when humans interact with VQA systems. While existing VQA datasets generally assume questions are clearly defined and lead to unique answers, real-world questions often include ambiguous expressions, vague references, or unspecified objects. In this program, we consider ambiguous questions as those containing deictic terms (e.g., "it," "this," "that") or other general terms (e.g., "thing," "object") without sufficient contextual information. For example, in a question about the cat image we'll use in this program, phrases such as “on the sofa” or “next to the cat” provide clarity, whereas their absence makes the question ambiguous.

This feature aims to handle these ambiguities by prompting the user for clarification when their question lacks sufficient context, thus improving the system's interpretive accuracy. The model used is BLIP-2, proposed in the paper "[BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597)," and is implemented using the Hugging Face [transformers](https://huggingface.co/docs/transformers/en/index) library. 

About BLIP-2: 

## Requirements
This notebook can be run on Google Colab. For runtime efficiency, it is highly recommended to enable GPU support.
  1. Go to `Runtime` > `Change runtime type`.
  2. Set `Hardware accelerator` to any available GPUs (If you're using the free version of Colab, you will most likely have the option to select a T4 GPU).
Please note: for users on the free version, there are time limitations for GPU usage, and selecting a GPU does not guarantee that one will be allocated to you. For more detailes, visit https://research.google.com/colaboratory/faq.html.

## Dataset
This notebook uses the [VQA v2.0 dataset](https://visualqa.org/download.html). You'll need the following files:
  - `v2_OpenEnded_mscoco_val2014_questions.json`
  * `v2_mscoco_val2014_annotations.json`
  + `val2014.zip`

To set up the required dataset:
  1. Use [this shared Google Drive link](https://drive.google.com/drive/folders/1ZGNVw2FkCzoyXPhuf_eLygYz6L4Ud4P5?usp=drive_link) to download these three files to your local computer. 
  2. Upload these three files to a suitable location in your Google Drive.

Note: In the notebook, you'll need to modify file paths to match the location where you've uploaded the files in your Google Drive. 

## Runing the notebook
Once the dataset is uploaded and paths are adjusted, follow the instructions in each cell of the notebook. The notebook includes an interactive clarification feature to handle ambiguous user questions in the last part, which prompts for more context if necessary before generating a model response.
