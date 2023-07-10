from gtts import gTTS
message= "yippee"
tts = gTTS(message)
tts.save("yippee.mp3")