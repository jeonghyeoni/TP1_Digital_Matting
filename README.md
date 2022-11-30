# TP1_Digital_Matting
By obtaining the absolute difference between the background and each frame, pixels with a difference less than the threshold are considered as the background, and greater than the threshold as the foreground.
Also, I applied erosion and dilation to all frames of the video.

# How to use?
1. Run the 'background_subtraction.py'
2. Make sure that the Python source file, video, and image are in the same folder.
3. Enter the name of the image you want to use as a new background. (e.g. busan.jpg)
4. Enter the name of the video you want to change the background of.(e.g. video.mp4)

# Result
original frame
<img width="100%" src="https://user-images.githubusercontent.com/119128711/204883940-82e92777-fe7f-45dc-8977-36c26930449f.jpg"/>
result frame
<img width="100%" src="https://user-images.githubusercontent.com/119128711/204883261-9e2d7d2b-64fb-4c53-b4f7-e8785c17c28d.jpg"/>
original frame
<img width="100%" src="https://user-images.githubusercontent.com/119128711/204883957-1fd30e94-cd2d-4d5a-b590-7b2a0a08a3fb.jpg"/>
result frame
<img width="100%" src="https://user-images.githubusercontent.com/119128711/204883278-4ade40eb-a1a5-487d-b468-ee2de6b49362.jpg"/>


