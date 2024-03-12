import openai
import pyttsx3
import time
import speech_recognition as sr


def voiceTtext(file):
    rec = sr.Recognizer()
    with sr.AudioFile(file) as source:
        aud = rec.record(source)
    try:
        return rec.recognize_google_cloud(aud)
    except:
        print('An error!')

# API
openai.api_key = ''
def generaterep(text):
    resp = openai.Completion.create(
        engine='text-davinci-003',
        promt=text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,  # randomness
    )
    return resp['Choices'][0]['text']


# tts
eng = pyttsx3.init()
def tts(text):
    eng.say()
    eng.runAndWait()


def main():
    while True:
        # Dang
        print('Say Dang ... to record your question')

        with sr.Microphone() as src:
            recog = sr.Recognizer()
            aud = recog.listen(src)

            try:
                trs = recog.recognize_google_cloud(aud)
                if trs.lower() == 'dang':
                    # record
                    fil = 'in.wav'
                    print('say yr question')

                    with sr.Microphone() as src:
                        recog = sr.Recognizer()
                        aud = recog.listen(src, phrase_time_limit=None, timeout=None)
                        with open(fil, 'wb') as f:
                            f.write(aud.get_wav_data())

                    txt = voiceTtext(fil)
                    if txt:
                        print(txt)

                        # generate response
                        resp = generaterep(txt)
                        tts(resp)
                elif trs.lower() == 'dang bang':
                    print('you said stop! we"re stopping ')
                    return
            except:
                print("ERRRR!")


if __name__ == '__main__':
    main()