from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import moviepy.editor as mp
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, language=request.form["menu"])

            return render_template('transcribe.html', transcript=transcript)
    return render_template('index.html', transcript=transcript)


@app.route("/templates/index2.html", methods=["GET", "POST"])
def index2():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:

            file.save(os.path.join("uploads", file.filename))

            path = os.path.join("uploads", file.filename)
            clip = mp.VideoFileClip(path)
            clip.audio.write_audiofile(r"converted.wav")
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile("converted.wav")
            with audioFile as source:
                data = recognizer.record(source, duration=100)

            transcript = recognizer.recognize_google(data, language=request.form["menu"])

            # os.remove(os.path.join(path))
            return render_template('transcribe.html', transcript=transcript)
    return render_template('index2.html', transcript=transcript)


@app.route("/templates/about.html")
def about():
    return (render_template('about.html'))


@app.route("/templates/transcribe.html")
def transcribe():
    return (render_template('transcribe.html'))


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
