import spacy
import numpy as np
from typing import List, Tuple

def load_categories(filename: str) -> List[str]:
    """Load categories from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def load_sentences(filename: str) -> List[str]:
    """Load sentences from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_vector_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors."""
    if vec1 is None or vec2 is None:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def find_top_categories(sentence: str, 
                       categories: List[str], 
                       nlp, 
                       num_categories: int = 5) -> List[Tuple[str, float]]:
    """Find the top N categories most similar to the sentence."""
    # Get sentence vector
    sentence_doc = nlp(sentence)
    sentence_vector = sentence_doc.vector

    # Calculate similarities with all categories
    similarities = []
    for category in categories:
        category_doc = nlp(category)
        similarity = get_vector_similarity(sentence_vector, category_doc.vector)
        similarities.append((category, similarity))

    # Sort by similarity score and return top N
    return sorted(similarities, key=lambda x: x[1], reverse=True)[:num_categories]

def main():
    # Load spaCy model (using the larger model for better accuracy)
    print("Loading Spacy model...")
    nlp = spacy.load('en_core_web_lg')

    # Load categories and sentences
    print("Loading categories and sentences...")
    categories = load_categories('final_simplified_subjects_exact_3500_complete.txt')
    sentences = load_sentences('random_sentences.txt')

    # Process each sentence and write results
    print("Processing sentences...")
    with open('classified_sentences.txt', 'w', encoding='utf-8') as f:
        total_sentences = len(sentences)
        for idx, sentence in enumerate(sentences, 1):
            # Get top 5 categories
            top_categories = find_top_categories(sentence, categories, nlp)
            
            # Format output line
            category_names = [cat[0] for cat in top_categories]
            output_line = f"{sentence}, {', '.join(category_names)}\n"
            
            # Write to file
            f.write(output_line)
            
            # Progress update
            if idx % 10 == 0:
                print(f"Processed {idx}/{total_sentences} sentences...")

    print("Classification complete! Results written to classified_sentences.txt")

if __name__ == "__main__":
    main()
