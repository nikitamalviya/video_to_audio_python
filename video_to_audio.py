import os
import sys

'''
Description :
    This code converts video to audio file.
    The FFMPEG exe can be downloaded from : https://www.filehorse.com/download-ffmpeg/download/'''

def convert_video_to_audio(video_path, audio_path):
    '''
    @param video_path : in .mp4 format
    @param audio_path : in .wav format
    @param status : if the process of video to audio conversion is successfull or not. 
    '''
    try:
        # ffmpeg -i IA0128647-1591811959-video.mp4 -vn test_audio.wav
        os.system(f"""ffmpeg -i {video_path} -vn {audio_path}""")
        status = True
    except Exception as e:
        status = False
        print(f"Exception Raised -- video to audio conversion,  {e}")
    return status

if __name__ == "__main__":
    if len(sys.argv) == 3:
        video_path, audio_path = sys.argv[1], sys.argv[2] 
        convert_video_to_audio(video_path, audio_path)
    else:
        print("Expects two arguments : video_path and audio_path")    