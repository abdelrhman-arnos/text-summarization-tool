# Text Summarization Tool

This is a simple Python script that demonstrates a text summarization tool using extractive summarization with the help of the NLTK library.

## Overview

Text summarization is the process of generating a concise and meaningful summary of a longer text while preserving its key information. This tool utilizes extractive summarization, which involves selecting the most important sentences from the input text to construct the summary.

## Features

- Extractive summarization based on sentence scores
- Preprocessing of the input text to remove stopwords and punctuation
- Customizable number of sentences in the generated summary

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository or download the `main.py` and `requirements.txt` files.
3. Install the required dependencies by running the following command: `pip install -r requirements.txt`

## Usage

1. Open the `main.py` file in a Python IDE or text editor.
2. Replace the placeholder text in the `text` variable with your desired input text.
3. Adjust the `num_sentences` parameter in the `generate_summary` function to set the number of sentences in the generated summary.
4. Run the script using Python: `python main.py`
5. The summary will be displayed in the console.

## Customization

Feel free to customize the code according to your specific needs. You can experiment with different preprocessing techniques, modify the summarization algorithm, or incorporate additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- This tool was developed using the NLTK library, which is a powerful and widely used library for natural language processing tasks.