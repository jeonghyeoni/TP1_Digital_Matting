# TP1_Digital_Matting
By obtaining the absolute difference between the background and each frame, pixels with a difference less than the threshold are considered as the background, and greater than the threshold as the foreground.
Also, I applied erosion and dilation to all frames of the video.

# How to use?
1. Run the 'background_subtraction.py'
2. Make sure that the Python source file, video, and image are in the same folder.
3. Enter the name of the image you want to use as a new background. (e.g. busan.jpg)
4. Enter the name of the video you want to change the background of.(e.g. video.mp4)

