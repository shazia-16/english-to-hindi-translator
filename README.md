# English to Hindi Translator 🇮🇳

This is a simple **English → Hindi language translator** built using a **Hugging Face pretrained model** (`Helsinki-NLP/opus-mt-en-hi`).  
It takes 30 English sentences and translates them into Hindi.

---

## 📌 Features
- Uses Hugging Face `transformers` library
- Translates English text to Hindi
- Beginner-friendly and lightweight

---

## 🛠️ Tech Stack

### Programming Language
- **Python 3.x** - Core programming language used for the entire project

### Libraries and Frameworks

1. **Transformers (Hugging Face)**
   - Purpose: Provides access to pre-trained NLP models
   - Specific model used: `Helsinki-NLP/opus-mt-en-hi`
   - Why: This library simplifies the implementation of state-of-the-art translation models without requiring extensive training

2. **MarianMT Model**
   - A neural machine translation model specifically trained for English to Hindi translation
   - Part of the OPUS-MT project (Open Parallel Corpus - Machine Translation)
   - Advantage: Optimized for translation tasks with high accuracy

3. **MarianTokenizer**
   - Preprocesses input text by converting it into tokens that the model can understand
   - Handles special characters and maintains context

## ⚙️ Installation & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/shazia-16/english-to-hindi-translator.git
   cd english-to-hindi-translator

2. Create virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate      # for Windows

3. Install dependencies:
pip install torch transformers sentencepiece

4. Run the translator:
python translator.py

## 📸 Example Output

Here is a sample screenshot of the translator in action:

![Translator Screenshot](screenshot.png)
