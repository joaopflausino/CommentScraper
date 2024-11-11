import pandas as pd
from browser_setup import setup_driver
from scraper import scrape_comments
from text_processing import process_text
from sentiment_analysis import analyze_sentiment
from Login import instagram_login  
from Creds import USERNAME, PASSWORD, CSV_PATH,INSTAGRAM_POST_PATH,FINAL_FILE


def get_post_urls(csv_path):
    
    urls_df = pd.read_csv(csv_path)
    
    return [f"{INSTAGRAM_POST_PATH}{post_id}/" for post_id in urls_df['Post_URLs']]

def main():
    csv_path = CSV_PATH  
    post_urls = get_post_urls(csv_path)
    
    max_urls = 5

    all_comments_df = []
    
    
    driver = setup_driver()
    instagram_login(driver, USERNAME, PASSWORD)

    #this loop is for normal mode
    #for url in post_urls:

    #just for test
    for i, url in enumerate(post_urls):
        if i >= max_urls: 
            break
        
        comments, post_id = scrape_comments(driver, url)
        comments_df = pd.DataFrame(comments, columns=["Comments"])
        if len(comments_df) == 1 and comments_df.iloc[0]["Comments"] == "Inicie a conversa.":
            continue
        reshaped_df = process_text(comments_df, post_id)
        all_comments_df.append(reshaped_df)

    driver.quit()

    final_comments_df = pd.concat(all_comments_df, ignore_index=True)

    final_comments_df = analyze_sentiment(final_comments_df)
    

    print("###########################")
    print(final_comments_df)
    print("###########################")

    final_comments_df.to_csv(FINAL_FILE)

if __name__ == "__main__":
    main()
