import speech_recognition as sr
import pyttsx3

h='ur'
# te-In >> telugu............... hi-In >> hindi ..............  ur-IN >> Urdu .............. bn-In >> Bengali ............ en-In >> indian englist

if __name__=="__main__":
    

    s=sr.Recognizer()

    with sr.Microphone() as source2:
        print(" SILENCE Please")
        
        s.adjust_for_ambient_noise(source2, duration = 2)
        
        print(" speak now please.....  ")
        
        audio2=s.listen(source2)
        print("Hearing")
        try:
            textt= s.recognize_google(audio2, language=h)
            textt= textt.lower()
            h=textt
            print(" Did you say :- "+textt)
      
        except Exception as e:
            
            print("error :"+str(e))
            
            
    from googletrans import Translator

    def translate_urdu_to_english(text):
        translator = Translator()
        translation = translator.translate(text, src='bn', dest='en')
        return translation.text

    # Example usage
    
    english_translation = translate_urdu_to_english(h)
    print("English translation:", english_translation)

            
            
