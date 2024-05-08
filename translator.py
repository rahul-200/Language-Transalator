from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    print("Welcome to the Language Translator!")
    print("Enter text to translate or type 'quit' to exit.")

    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            target_language = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish, etc.): ")
            translated_text = translate_text(user_input, target_language)
            print("Translated text:", translated_text)

if __name__ == "__main__":
    main()
