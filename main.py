import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words, removing stopwords and punctuation
    tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
    stop_words = set(stopwords.words("english"))
    tokenized_sentences = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in tokenized_sentences]
    
    return tokenized_sentences

def calculate_sentence_scores(sentences):
    # Calculate the word frequency distribution
    word_frequencies = FreqDist([word for sentence in sentences for word in sentence])
    
    # Assign a score to each sentence based on the sum of its word frequencies
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        score = sum([word_frequencies[word] for word in sentence])
        sentence_scores[i] = score
    
    return sentence_scores

def generate_summary(text, num_sentences):
    tokenized_sentences = preprocess_text(text)
    sentence_scores = calculate_sentence_scores(tokenized_sentences)
    
    # Sort the sentences based on their scores in descending order
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Select the top N sentences for the summary
    summary_sentences = sorted_sentences[:num_sentences]
    
    # Join the selected sentences to form the summary
    summary = ' '.join([sent_tokenize(text)[sentence_index] for sentence_index in summary_sentences])
    
    return summary

# Example usage
if __name__ == "__main__":
    text = """
    Your input text goes here. This can be a long article or document that you want to summarize. Make sure to provide enough text for meaningful summarization.
    """
    summary = generate_summary(text, num_sentences=3)
    print("Summary:")
    print(summary)
