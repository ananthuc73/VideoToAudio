#make sure to install the moviepy library

import moviepy as mp
import moviepy.editor

#import the videofile using its path
videofile = mp.editor.VideoFileClip("C://path/mp4")

#Converting video to audio
videofile.audio.write_audiofile('audiofile.mp3')
