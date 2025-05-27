import pandas as pd
import re
import json
from tqdm import tqdm

df = pd.read_csv("tripadvisor_hotel_reviews.csv")

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^A-Za-z0-9 .,?!]', '', text)
    return text.strip()

df['cleaned_review'] = df['Review'].apply(clean_text)

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

chunks = []
for idx, row in tqdm(df.iterrows(), total=len(df)):
    for chunk in chunk_text(row['cleaned_review']):
        chunks.append({
            'text': chunk,
            'metadata': {
                'source': 'TripAdvisor',
                'rating': row['Rating']
            }
        })

with open("processed_chunks.json", "w") as f:
    json.dump(chunks, f)