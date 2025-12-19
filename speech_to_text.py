import sounddevice as sd
import queue
import vosk
import json
import speak


q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def spech_to_text():
    try:
        model = vosk.Model("vosk-model-small-en-us-0.15")
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, 16000)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    voice_data = result.get("text", "")
                    if voice_data:
                        return voice_data
                    else:
                        speak.speak("sorry")
    except:
        speak.speak("sorry")
     
