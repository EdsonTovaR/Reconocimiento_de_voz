import pytube 
import whisper

youtubeVideoId="https://www.youtube.com/shorts/VGfTpi2Vmzo?feature=share"
model=whisper.load_model('small')

youbeVideo=pytube.YouTube(youtubeVideoId)
audio=youbeVideo.streams.get_audio_only()
audio.download(filename='tmp.mp4')

result = model.transcribe('tmp.mp4')

print(result["text"])