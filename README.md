# README for Audio/Video to Text Conversion Web Application

## Introduction

This project is focused on creating a web application that facilitates the conversion of audio and video files into text format, leveraging speech recognition and synthesis technologies. This tool is particularly beneficial for individuals with learning disabilities, basic literacy levels, or visual impairments, and reduces dependency on traditional input devices.

## Features

1. **Convert Audio**: Users can upload audio files in WAV format and select the language for transcription. The audio is then converted into text and displayed in a text box.
2. **Convert Video**: Users can upload video files in MP4 format, choose the desired language, and convert the video's audio track into text.
3. **About Us**: Provides information about the application and its developers.

## Usage

- **Convert Audio Page**: Upload an audio file, select the language, and click the "Transcribe" button to convert the audio into text.
- **Convert Video Page**: Upload a video file, select the language, and click the "Transcribe" button to extract and convert the audio into text.
- **About Us Page**: Learn more about the purpose and development of the application.

## Speech Recognition Process

1. **Analog to Digital Conversion**: Vibrations in the air (speech) are converted into digital signals. The software may enhance the recording by eliminating noise and adjusting volume levels.
2. **Analysis of Digital Signal**: The digital signals are segmented and matched with phonemes of the target language, representing the sounds of human speech.
3. **Conversion to Text**: The software compares the phonemes against a large database and outputs the final text on the screen.

## Hardware and Software Requirements

- **IDE**: PyCharm 2021.1 for system layout design.
- **Web Browser**: Google Chrome for accessing the system.
- **Backend**: Python with Flask for building lightweight web applications.
- **Operating System**: Compatible with Windows 10 and other major operating systems.

## Installation and Setup

1. Clone the repository to your local machine.
2. Ensure Python and Flask are installed. If not, install them using:
   ```bash
   pip install Flask
   ```
3. Open the project in PyCharm or your preferred IDE.
4. Start the Flask server:
   ```bash
   flask run
   ```
5. Access the web application through Google Chrome at `http://localhost:5000`.
