import threading, time

def play_audio(audio_e, video_e):
    print("PLAY AUDIO")
    audio_e.set()  # Say "I'm ready" to play_video()
    video_e.wait()  # Wait for play_video() to say "I'm ready"
    #audio_e.set()  # Say "I'm ready" to play_video()
    print("PLAYING AUDIO")
    time.sleep(10)

def play_video(audio_e, video_e):
    print("PLAY VIDEO")
    #audio_e.wait()  # Wait for play_audio() to say "I'm ready"
    video_e.set()  # Say "I'm ready" to play_audio()
    audio_e.wait()  # Wait for play_audio() to say "I'm ready"
    print("PLAYING VIDEO")
    time.sleep(10)

def view():
    audio_e = threading.Event()
    video_e = threading.Event()

    audiothread = threading.Thread(target=play_audio,
                                   args=(audio_e, video_e))
    audiothread.start()
    time.sleep(5)
    play_video(audio_e, video_e)


view()