import os
from google.cloud import speech_v1 as speech
client = speech.SpeechClient().from_service_account_file('key.json')

#specifying path of the audio files folder
path = "C:\\Users\\mugir\\Desktop\\Audio files"

os.chdir(path)

#For reading a file
def read_text_file(file_path):
    with open(file_path, 'rb') as f:
        audio_data = f.read()
    return audio_data

#for transcription of audio file
def transcription(config,audio):
    response = client.recognize(config=config,
                                audio=audio)
    print_transcription(response)

#printing the results
def print_transcription(response):
    # print(response)
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}\n")

#audio configuration

config = speech.RecognitionConfig(
            language_code='es-CO',
            encoding="OGG_OPUS",
            sample_rate_hertz=16000,
            enable_spoken_punctuation=True
        )
i=1
#walking through the folder of audio files
for file in os.listdir():

    # Check whether file is in opus format or not
    if file.endswith(".opus"):
        file_path = f"{path}\{file}"
        # call read text file function
        audio_data=read_text_file(file_path)

        audio_file = speech.RecognitionAudio(content=audio_data)
        print(f"File Number: {i} ")
        i+=1
        #calling the function
        transcription(config,audio_file)

