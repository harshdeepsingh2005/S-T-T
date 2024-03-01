# import speech_recognition as sr
# import pyttsx3

# h='ur-IN'
# # te-In >> telugu............... hi-In >> hindi ..............  ur-IN >> Urdu .............. bn-In >> Bengali ............ en-In >> indian englist

# if __name__=="__main__":
    

#     s=sr.Recognizer()

#     with sr.Microphone() as source2:
#         print(" SILENCE Please")
        
#         s.adjust_for_ambient_noise(source2, duration = 2)
        
#         print(" speak now please.....  ")
        
#         audio2=s.listen(source2)
#         print("Hearing")
#         try:
#             textt= s.recognize_google(audio2, language=h)
#             textt= textt.lower()
#             h=textt
#             print(" Did you say :- "+textt)
      
#         except Exception as e:
            
#             print("error :"+str(e))
            
            
from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()

    # Get audio file from the request
    audio_file = request.files['audio_data']

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text

    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."

    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

if _name_ == '_main_':
    app.run(debug=True)
    