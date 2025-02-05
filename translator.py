pip install googletrans==4.0.0-rc1
from googletrans import Translator
def translate_text(text, target_language):
translator = Translator()
translation = translator.translate(text, dest=target_language)
 return translation.text
 # Example usage
 text_to_translate  = input( "Enter the text to translate : ")
 target_language = input("Enter the target language code (e.g. , 'en' for English, 'fr' for French ) : " )
translated_text = translate_text (text_to_translate, target_language)
print(f" Translated Text : {translated_text}")
except Exception as e:
 print( f "Error : {e} ")



