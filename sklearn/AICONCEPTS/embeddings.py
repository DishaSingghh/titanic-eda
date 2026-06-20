# embeddings and cosine simialrity 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # small, fast, good quality

sentences = [
    "I love pizza",
    "I enjoy pasta",
    "Food is my favourite thing",
    "The stock market crashed today",
    "Sensex fell 500 points",
    "Razorpay processes payments",
    "PhonePe is a payment app",
    "Dogs are great pets",
    "I adopted a puppy last week",
    "Machine learning is fascinating"
]

embeddings = model.encode(sentences)

print(f"Number of sentences: {len(embeddings)}")
print(f"Embedding dimension: {len(embeddings[0])}")
print(f"First embedding (first 5 values): {embeddings[0][:5]}")

#cosine simlarity by hand
# import numpy as np

# def cosine_similarity(vec_a, vec_b):
#     dot_product = np.dot(vec_a, vec_b)          # A · B
#     magnitude_a = np.sqrt(np.sum(vec_a ** 2))   # ||A||
#     magnitude_b = np.sqrt(np.sum(vec_b ** 2))   # ||B||
#     return dot_product / (magnitude_a * magnitude_b)


# # compare all pairs against sentence 0 ("I love pizza")
# anchor = embeddings[0]

# print(f"Anchor: '{sentences[0]}'\n")
# for i, (sentence, embedding) in enumerate(zip(sentences[1:], embeddings[1:]), 1):
#     score = cosine_similarity(anchor, embedding)
#     print(f"vs '{sentence}' → {score:.4f}")


# #full matrix
# print("\n--- Full Similarity Matrix ---")
# print(f"{'':45}", end="")
# for s in sentences:
#     print(f"{s[:10]:12}", end="")
# print()

# for i, s1 in enumerate(sentences):
#     print(f"{s1[:45]:45}", end="")
#     for j, s2 in enumerate(sentences):
#         score = cosine_similarity(embeddings[i], embeddings[j])
#         print(f"{score:.2f}        ", end="")
#     print()