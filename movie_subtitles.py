import cv2
import pandas as pd
from moviepy.editor import VideoFileClip

def pipeline(frame):
    try:
        cv2.putText(frame, str(next(dfi)[1].sentence), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA, True)
    except StopIteration:
        pass
    # additional frame manipulation
    return frame

dfi = pd.read_csv('/Users/danielshaked/Downloads/Peaky.Blinders.S06E01.720p.HDTV.x264-ORGANiC.srt-1.csv').iterrows()
video = VideoFileClip("/Users/danielshaked/Downloads/Peaky.Blinders.S06E01.720p.HDTV.x264-ORGANiC.srt-1.csv")
out_video = video.fl_image(pipeline)
out_video.write_videofile("vidout.mp4", audio=True)