import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Tuple
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

class SentenceClassifier:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def preprocess_text(self, text: str) -> str:
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing."""
        # Tokenize and convert to lower case
        tokens = word_tokenize(text.lower())
        
        # Remove punctuation and stopwords
        tokens = [token for token in tokens 
                 if token not in string.punctuation 
                 and token not in self.stop_words]
        
        # Lemmatize tokens
        lemmatized = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        return ' '.join(lemmatized)

    def get_wordnet_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity using WordNet."""
        # Preprocess both texts
        words1 = word_tokenize(self.preprocess_text(text1))
        words2 = word_tokenize(self.preprocess_text(text2))
        
        # Calculate similarities between all word pairs
        max_similarities = []
        
        for word1 in words1:
            word1_synsets = wn.synsets(word1)
            if not word1_synsets:
                continue
                
            word_similarities = []
            for word2 in words2:
                word2_synsets = wn.synsets(word2)
                if not word2_synsets:
                    continue
                
                # Get maximum similarity between any synsets of the two words
                max_similarity = max(
                    (s1.path_similarity(s2) or 0)
                    for s1 in word1_synsets
                    for s2 in word2_synsets
                )
                word_similarities.append(max_similarity)
            
            if word_similarities:
                max_similarities.append(max(word_similarities))
        
        # Return average of maximum similarities
        return np.mean(max_similarities) if max_similarities else 0.0

    def get_tfidf_similarity(self, texts1: List[str], texts2: List[str]) -> np.ndarray:
        """Calculate TF-IDF based cosine similarity between texts."""
        # Combine all texts for vectorization
        all_texts = texts1 + texts2
        
        # Fit and transform the vectorizer
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)
        
        # Calculate cosine similarity
        n_texts1 = len(texts1)
        similarities = cosine_similarity(
            tfidf_matrix[:n_texts1], 
            tfidf_matrix[n_texts1:]
        )
        
        return similarities

    def find_top_categories(self, 
                          sentence: str, 
                          categories: List[str], 
                          num_categories: int = 5) -> List[Tuple[str, float]]:
        """Find the top N categories most similar to the sentence."""
        # Calculate WordNet similarities
        wn_similarities = [
            self.get_wordnet_similarity(sentence, category)
            for category in categories
        ]
        
        # Calculate TF-IDF similarities
        tfidf_similarities = self.get_tfidf_similarity(
            [sentence], 
            categories
        )[0]
        
        # Combine similarities (giving equal weight to both methods)
        combined_similarities = [
            (cat, 0.5 * wn_sim + 0.5 * tfidf_sim)
            for cat, wn_sim, tfidf_sim 
            in zip(categories, wn_similarities, tfidf_similarities)
        ]
        
        # Sort by similarity score and return top N
        return sorted(combined_similarities, 
                     key=lambda x: x[1], 
                     reverse=True)[:num_categories]

def load_files(categories_file: str, sentences_file: str) -> Tuple[List[str], List[str]]:
    """Load categories and sentences from files."""
    with open(categories_file, 'r', encoding='utf-8') as f:
        categories = [line.strip() for line in f if line.strip()]
    
    with open(sentences_file, 'r', encoding='utf-8') as f:
        sentences = [line.strip() for line in f if line.strip()]
    
    return categories, sentences

def main():
    print("Initializing classifier...")
    classifier = SentenceClassifier()
    
    print("Loading categories and sentences...")
    categories, sentences = load_files(
        'final_simplified_subjects_exact_3500_complete.txt',
        'random_sentences.txt'
    )
    
    print("Processing sentences...")
    with open('classified_sentences.txt', 'w', encoding='utf-8') as f:
        total_sentences = len(sentences)
        for idx, sentence in enumerate(sentences, 1):
            # Get top 5 categories
            top_categories = classifier.find_top_categories(sentence, categories)
            
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
