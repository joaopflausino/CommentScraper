import pandas as pd
import spacy

nlp = spacy.load("pt_core_news_sm")

def process_text(comments_df, post_id):
    reshaped_df = pd.DataFrame(comments_df.values.reshape(-1, 3), columns=['Username', 'Time', 'Comment'])
    reshaped_df["post ID"] = post_id
    reshaped_df['texto_limpo'] = reshaped_df['Comment'].str.lower().str.replace(r'[^\w\s]', '', regex=True)
    return reshaped_df