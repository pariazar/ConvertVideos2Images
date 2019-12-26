# ConvertVideos2Images
CV2I (Convert Videos to Images) is command line tool that you can easily convert your videos in one directory to multiple images
it used for creating dataset and training them and making model in CNN

simple definition: CV2I is dataset creator with videos

<h2>features</h2>

collect image data from video resize them after saving files automatically
set quality of the images

<h2>Requirements</h2>


install Anaconda distribution Python 3.7 version from here

install libs with using the command below in Anaconda prompt


    pip install numpy matplotlib opencv-contrib-python PIL
    
    
<p>Usage 1- download tool with using the command below</p>
    

    git clone https://github.com/hamedpa/ConvertVideos2Images
    
<p>2- execute program with using the command below</p>

    python cv2iDatasets.py 


<p>4- Enter inputs with using the command below</p>

SAMPLE OF INPUTS

    format of your video (Example: mp4) : mkv
    format of your images (Example: jpg) : jpg
    please enter a path that your videos exist there : G:/videos
    please enter frame Rate : 10
    Please enter seconds for the video to start : 10
    do you need to resize images (n/y) : n


<p>5- All images will save in images directory</p>

you can use this data in deep learning
