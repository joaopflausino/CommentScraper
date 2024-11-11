from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(reshaped_df):
    reshaped_df['sentimento'] = reshaped_df['Comment'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
    return reshaped_df
