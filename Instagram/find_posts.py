import instaloader
import pandas as pd
from Creds import FIND_USER

def find_post():
    
    loader = instaloader.Instaloader()
    df = pd.DataFrame(columns=["Post_URLs"])

    username = FIND_USER

    try:

        profile = instaloader.Profile.from_username(loader.context, username)
    
        for post in profile.get_posts():
            print(f"Post: {post.shortcode}")
            new_row = pd.DataFrame({"Post_URLs": [post.shortcode]})
            df = pd.concat([df, new_row], ignore_index=True)
        
        print("##############")
        print(df)

        print(f"All posts from @{username} downloaded successfully.")
        df.to_csv(f"{username}_posts.csv")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile @{username} does not exist.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    find_post()
