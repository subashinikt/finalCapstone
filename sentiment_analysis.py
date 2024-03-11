import nltk
import pandas as pd
import spacy
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from textblob import TextBlob

# step: 1 Implement a sentiment analysis model using spaCy
nlp = spacy.load("en_core_web_sm")

# download all the data
nltk.download('all')

# Load the amazon review dataset
df = pd.read_csv('amazon_product_review.csv', low_memory=False)

# remove all missing values
clean_data = df.dropna(subset=['reviews.text'])


def remove_stop_words(sentence: str):
    """
    method to remove stop words
    :param sentence: review text as sentence:
    :return: filtered tokens as a string
    """
    # parse the sentence
    doc = nlp(sentence)
    # use a list comprehension to remove the stop words. To remove stop words used is_stop attribute from spaCy.
    filtered_tokens = [token for token in doc if not token.is_stop]

    return ' '.join([token.text for token in filtered_tokens])


# step:2
def preprocess_text(text):
    """
    Used to preprocess the text.
    :param text:
    :return: processed text
    """
    stop_words_removed_sent = remove_stop_words(text)
    # Tokenize the text
    filtered_tokens = word_tokenize(stop_words_removed_sent.strip().lower())

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text


# create new data frame only with review and its sentiment
df_with_sentiments = pd.DataFrame()
df_with_sentiments['reviewText'] = clean_data['reviews.text'].apply(preprocess_text)


# step:3 create get_sentiment function
def get_sentiment(text):
    """
    It is used to find the sentiment of the reviews.
    :param text: review
    :return: sentiment which is string, possible return values are positive/negative/neutral
    """
    # Analyze sentiment with TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment


# step:3 apply get_sentiment function
df_with_sentiments['sentiment'] = df_with_sentiments['reviewText'].apply(get_sentiment)

# step:4 sample review taken from TrustPilot, expected sentiment is positive
review_text = ("Delivery was better than Prime :) Standard delivery time was mentioned as 10 days but I placed an "
               "order on one Sunday night got it delivered on Monday morning :) Was pleasantly surprised")
print("REVIEW --> " + get_sentiment(review_text))

# random reviews taken from dataframe to compare
review_1 = df_with_sentiments['reviewText'][1]
review_2 = df_with_sentiments['reviewText'][2]

print("Comparing " + review_1 + " with " + review_2)
review_1 = nlp(review_1)
review_2 = nlp(review_2)
print("SIMILARITY: " + str(review_1.similarity(review_2)))
