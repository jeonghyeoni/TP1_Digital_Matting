import cv2
import numpy as np

name = input('video: ')
video = cv2.VideoCapture(name)

fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

recorder = cv2.VideoWriter("output.mp4",
                            cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


name = input('background image: ')
im =  cv2.imread(name)
im = cv2.resize(im,(width, height))

_, background = video.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
background = cv2.GaussianBlur(background, (0, 0), 2)


while True:
    ret, frame = video.read()
    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    current_frame = cv2.GaussianBlur(current_frame, (0, 0), 2)

    difference = cv2.absdiff(background, current_frame)

    final_difference = []

    '''erosion'''
    mask = np.ones((3, 3), dtype='uint8')
    out = cv2.erode(difference, mask)
    final_difference.append(out)
    temporal_difference = np.array(final_difference)

    out = cv2.erode(temporal_difference[-1], mask)
    final_difference.append(out)
    temporal_difference = np.array(final_difference)

    mask = np.ones((5, 5), dtype='uint8')
    out = cv2.erode(temporal_difference[-1], mask)
    final_difference.append(out)
    temporal_difference = np.array(final_difference)


    '''dilation'''
    masklist = [np.ones((k, k), dtype='uint8') for k in range(3, 13)]
    for mask in masklist:
        out = cv2.dilate(temporal_difference[-1], mask)
        final_difference.append(out)
        temporal_difference = np.array(final_difference)

    mask = np.ones((7, 7), dtype='uint8')
    for i in range(3):
        out = cv2.dilate(temporal_difference[-1], mask)
        final_difference.append(out)
        temporal_difference = np.array(final_difference)
    

    '''erosion'''
    masklist = [np.ones((k, k), dtype='uint8') for k in range(10, 3, -3)]
    for mask in masklist:
        for i in range(3):
            out = cv2.erode(temporal_difference[-1], mask)
            final_difference.append(out)
            temporal_difference = np.array(final_difference)

    mask = np.ones((5, 5), dtype='uint8')
    for i in range(7):
        out = cv2.erode(temporal_difference[-1], mask)
        final_difference.append(out)
        temporal_difference = np.array(final_difference)

    final_difference = np.array(final_difference)

    '''threshold'''
    lower10 = final_difference[-1]<=15
    
    frame2 = frame.copy()
    frame2[lower10] = im[lower10]

    cv2.imshow('result', frame2)
    cv2.imshow('difference', final_difference[-1])

    recorder.write(frame2)

    key = cv2.waitKey(20)
    if key == 27:
        break

recorder.release()
video.release()
cv2.destroyAllWindows()