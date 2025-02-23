# real_time_translation.py

from transformers import pipeline

# Load translation pipeline
translator = pipeline('translation_en_to_fr')

# Example usage
if __name__ == "__main__":
    text = "Hello, how are you?"
    translated = translator(text)
    print(translated)