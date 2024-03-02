from googletrans import Translator

def translate_urdu_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='ur', dest='en')
    return translation.text

# Example usage
urdu_text = input("Enter the text in Urdu: ")
english_translation = translate_urdu_to_english(urdu_text)
print("English translation:", english_translation)
