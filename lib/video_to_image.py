import cv2
import os

def count_frames(path):
    video = cv2.VideoCapture(path)
    total = 0
    try:
        total = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    except:
        total = count_frames_manual(video)
    video.release()
    return total

def count_frames_manual(video):
    total = 0
    while True:
        (grabbed, frame) = video.read()
        if not grabbed:
          break
        total += 1
    return total

def extract_mid_frame(pathIn, pathOut):
    mid_frame = count_frames(pathIn)//2
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    file_name = pathIn.split('/')[-1][:-4]
    success = True
    while success:
        success,image = vidcap.read()
        # print ('Read a new frame: ', success)
        if count == mid_frame:
            out_file = os.path.join(pathOut, file_name + "_frame%d.jpg" % count)
            cv2.imwrite(out_file, image)     # save frame as JPEG file
        count += 1
    return out_file
