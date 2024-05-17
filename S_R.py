#语音识别脚本，通过函数和类将语音模型的调用封装好，然后通过web框架开放API访问和调用，

#语音模型的定义和获取后面再加入，先把功能逻辑部分完成。

import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data)
                return {"status": "success", "transcription": text}
            except sr.UnknownValueError:
                return {"status": "error", "message": "Google Speech Recognition could not understand audio"}
            except sr.RequestError as e:
                return {"status": "error", "message": f"Could not request results from Google Speech Recognition service; {e}"}

@app.route('/recognize', methods=['POST'])
def recognize():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"})
    if file:
        speech_recognition = SpeechRecognition()
        response = speech_recognition.recognize_speech(file)
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
