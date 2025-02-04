import random

def split_sentences(input_file, train_file, test_file, train_size):
    # Read all sentences
    with open(input_file, 'r', encoding='utf-8') as f:
        sentences = f.read().splitlines()
    
    # Randomly sample train_size sentences for training
    train_sentences = random.sample(sentences, train_size)
    
    # Create a set of training sentences for efficient lookup
    train_set = set(train_sentences)
    
    # Get test sentences (all sentences not in training set)
    test_sentences = [sent for sent in sentences if sent not in train_set]
    
    # Write training sentences
    with open(train_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(train_sentences))
    
    # Write test sentences
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(test_sentences))
    
    # Print summary
    print(f"Total sentences: {len(sentences)}")
    print(f"Training sentences: {len(train_sentences)}")
    print(f"Test sentences: {len(test_sentences)}")

# Run the script
input_file = "sentence_data_v1.txt"
train_file = "sentence_data_training.txt"
test_file = "sentence_data_test.txt"
num_training_sentences = 10000  # Explicitly specify we want 10,000 sentences

split_sentences(input_file, train_file, test_file, num_training_sentences)