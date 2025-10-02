
from transformers import MarianMTModel, MarianTokenizer

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function to translate English to Hindi
def translate_en_to_hi(sentences):
    translated = []
    for sentence in sentences:
        tokens = tokenizer(sentence, return_tensors="pt", padding=True)
        translation = model.generate(**tokens)
        hindi_text = tokenizer.decode(translation[0], skip_special_tokens=True)
        translated.append(hindi_text)
    return translated

# Example: 30 English sentences
english_sentences = [
    "Hello!", "How are you?", "I love programming.", "Python is great.", 
    "This is a test.", "Good morning!", "Good night!", "See you later.", 
    "I am learning AI.", "I want to travel.", "What is your name?", 
    "My name is Shazia.", "I like music.", "I like dancing.", 
    "Can you help me?", "This is easy.", "I am happy.", "I am sad.", 
    "It is raining.", "It is sunny.", "I am hungry.", "I am tired.", 
    "I like reading.", "I like painting.", "I like coding.", 
    "I have a cat.", "I have a dog.", "Where are you?", "Thank you!", "Bye!"
]

# Translate
hindi_translations = translate_en_to_hi(english_sentences)

# Print results
for en, hi in zip(english_sentences, hindi_translations):
    print(f"{en} → {hi}")
