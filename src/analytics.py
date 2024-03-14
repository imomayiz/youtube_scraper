import os

# modify if necessary
TRANSCRIPTS_DIR = os.path.join(os.getcwd(), "transcripts")

# open each txt file in TRANSCRIPTS_DIR and count the number of words
word_count = {}
for file in os.listdir(TRANSCRIPTS_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(TRANSCRIPTS_DIR, file), "r", encoding="utf-8") as f:
            word_count[file] = len(f.read().split())
            
print(word_count)
print(f"Total number of words: {sum(word_count.values())}")
