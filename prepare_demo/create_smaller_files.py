#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:56:01 2017

@author: ajaver
"""
import glob
import os
import subprocess as sp
from MWTracker.helper.misc import FFMPEG_CMD


main_dir = '/Volumes/behavgenom_archive$/Avelino/Worm_Rig_Tests/short_movies_new/RawVideos'
video_files = glob.glob(os.path.join(main_dir, '**', '*.mjpg'))
short_files = [x.replace('short_movies_new', 'demo') for x in video_files]
for f_old, f_new in zip(video_files, short_files):
    dname = os.path.dirname(f_new)
    if not os.path.exists(dname):
        os.makedirs(dname)
    
    
    command = [FFMPEG_CMD, '-i', f_old, '-t', '60', '-c', 'copy', f_new]
    print(command)
    proc = sp.call(command)

#command = [ fileName, '-']
#proc = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)