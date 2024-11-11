from transformers import pipeline
import spacy

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
nlp = spacy.load("pt_core_news_sm")
def analyze_sentiment(reshaped_df):
    reshaped_df['sentimento'] = reshaped_df['Comment'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
    reshaped_df['tokens'] = reshaped_df['texto_limpo'].apply(lambda x: [token.text for token in nlp(x)])
    reshaped_df['tokens_sem_stopwords'] = reshaped_df['tokens'].apply(lambda tokens: [token for token in tokens if not nlp.vocab[token].is_stop])
    reshaped_df['lematizado'] = reshaped_df['texto_limpo'].apply(lambda x: [token.lemma_ for token in nlp(x)])
    return reshaped_df
