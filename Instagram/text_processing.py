import pandas as pd
import spacy

nlp = spacy.load("pt_core_news_sm")

def process_text(comments_df, post_id):
    print("##########")
    print(comments_df)
    print("##########")
    noheadercomments_df = comments_df.iloc[3:].iloc[:-1]
    print(noheadercomments_df)
    print("##########")
    reshaped_df = pd.DataFrame(noheadercomments_df.values.reshape(-1, 3), columns=['Username', 'Time', 'Comment'])
    reshaped_df["post ID"] = post_id

    reshaped_df['texto_limpo'] = reshaped_df['Comment'].str.lower().str.replace(r'[^\w\s]', '', regex=True)
    reshaped_df['tokens'] = reshaped_df['texto_limpo'].apply(lambda x: [token.text for token in nlp(x)])
    reshaped_df['tokens_sem_stopwords'] = reshaped_df['tokens'].apply(lambda tokens: [token for token in tokens if not nlp.vocab[token].is_stop])
    reshaped_df['lematizado'] = reshaped_df['texto_limpo'].apply(lambda x: [token.lemma_ for token in nlp(x)])

    return reshaped_df