
import argparse
import os
from pytube import YouTube
import whisper
from googletrans import Translator

def list_of_strings(arg):
	 return arg.split(',')

parser = argparse.ArgumentParser()

parser.add_argument(
	"--workerTaskId",
	type=int,
	default=0,
	help="Worker Task Id"
)

parser.add_argument(
	"--youtube_url",
	type=str,
	default="",
	help="Youtube Url",
)

parser.add_argument(
	"--target_lang",
	type=str,
	default="",
	help="Target_Language",
)

parser.add_argument(
	"--model_name",
	type=str,
	default="",
	help="Model Name",
)

parser.add_argument(
	"--audio_file_name",
	type=str,
	default="",
	help="Audio_File_Name",
)

parser.add_argument(
	"--output",
	type=str,
	default="",
	help="Output Folder",
)

ap = parser.parse_args()

info_text = f"Script Version : 1.1 \
				Arguments : \
				--workerTaskId: {ap.workerTaskId} \
				--youtube_url: {ap.youtube_url} \
				--target_lang: {ap.target_lang} \
				--model_name: {ap.model_name} \
				--output:{ap.output} \
				--audio_file_name: {ap.audio_file_name}"

print(info_text)

os.makedirs(ap.output, exist_ok=True)

path_1 = f""+ap.output+"/"+'audio'+".mp4"

def translation(text):

	translator = Translator()

	result = translator.translate(text,dest=ap.target_lang)

	return (result.text)

if ap.youtube_url != "":

	video_url = ap.youtube_url

	audio_file = YouTube(video_url).streams.filter(only_audio=True).first().download(filename= path_1)

else:

	audio_file = ap.audio_file_name


whisper_model = whisper.load_model(ap.model_name)

transcription = whisper_model.transcribe(audio_file)

path = f""+ap.output+"/"+'transcription'+".txt"

with open(path, 'w') as f:

	if ap.target_lang != "":

		f.write(translation(transcription['text']))

	else:

		f.write(transcription['text'])



