"""Audio to text transcription | Transcrição de audio para texto"""
import speech_recognition as sr
from pydub import AudioSegment
import moviepy.editor as mp
import logging as log

log.basicConfig(level=log.DEBUG)

# type bool for verification with different entries.
def audioToText(title:str, origin:str) -> bool:
    """
        :param - title: repository + name da transcrição
        :param - origin: file mp4 que será transcrito
        :return - True caso ocorreu tudo bem.
    """
    temp_mp3 = "temp/temp.mp3"
    temp_wav = "temp/temp.wav"

    clip = mp.VideoFileClip(origin).subclip()
    clip.audio.write_audiofile(temp_mp3)

    sound = AudioSegment.from_mp3(temp_mp3)
    sound.export(out_f=temp_wav, format="wav")

    with (sr.AudioFile(temp_wav) as source, 
      open(title, 'w') as file):
    
        r = sr.Recognizer()
        process = r.record(source)
        text = r.recognize_google(process, language='pt-BR')
        file.write(text)
        log.info("Transcrição realizado com Sucesso!")


if __name__ == "__main__":
    title = "files/transcricao.txt"
    origin = "src/exemplo.mp4"
    audioToText(title, origin)