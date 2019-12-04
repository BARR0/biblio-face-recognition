import face_recognition
import cv2 as cv
import numpy as np
import glob
import re

def load_faces(dir = 'face/'):
    fnames = glob.glob(dir + '*.jpg', recursive=True)
    return [
        re.sub(r'\.jpg$', '', f.split('/')[-1])
        for f in fnames
    ], [
        face_recognition.face_encodings(
            face_recognition.load_image_file(f)
        )[0]
        for f in fnames
    ], [
        cv.imread(f)
        for f in fnames
    ], max([
        int(s.group(1)) + 1 if s is not None else 0
        for s in [
            re.search(r'Person ([0-9]*)\.jpg', f)
            for f in fnames
        ]
    ] + [0])
