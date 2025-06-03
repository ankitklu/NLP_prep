import pandas as pd

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.file_path = file_path
        self.posts = self.load_posts()

    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            posts = json.load(f)
            df= pd.json_normalize(posts)
            df["length"] - df["line_count"].apply(self.categorize_length)
            df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))
            
    
    def categorize_length(self, line_count):
        if line_count <10:
            return "Short"
        elif 5<= line_count<=10:
            return "Medium"
        else:
            return "Long"

if __name__ == "__main__":
    fs = FewShotPosts("")
    pass

