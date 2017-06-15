import  cv2

import csv

import os

import sys



filepath = "/home/ubuntu/Sample0101"


# extract gestureID, startFrame, endFrame from labels.csv  @ 04/06/2017 21:28:09

label = []

with open(filepath+'/Sample0101_labels.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        label.append(row)

length = len(label)

gestureID = []
startFrame = []
endFrame = []

for i in range(0, length):
    gestureID.append(label[i][0])
    startFrame.append(label[i][1])
    endFrame.append(label[i][2])




# extract videoinformation from data.csv
videoInfo = []
with open(filepath+'/Sample0101_data.csv', 'rb') as df:
    s_reader = csv.reader(df, delimiter=',', quotechar='|')
    for row in s_reader:
        videoInfo.append(row)
num_Frames = videoInfo[0][0]
fps = videoInfo[0][1]
Max_depth = videoInfo[0][2]






# capture the frame from the video and classify it by gestureID 
# save it in Color 

frameCounter = 0

succ = True


newPath = 0

destFile = '/home/ubuntu/Color'

videoCapture = cv2.VideoCapture(filepath+'/Sample0101_color.mp4')

while (succ):
    # frameCounter += 1

    succ, frame = videoCapture.read()
    os.chdir(destFile)
    file_name = "gesture_"+"_"+ str(gestureID[newPath])
    if(os.path.exists(file_name) == False):
        os.mkdir(file_name)
        os.chdir(file_name)
    if(frameCounter >= int(startFrame[newPath])) and (frameCounter <= int(endFrame[newPath])):
        
        cv2.imwrite(file_name + "/alpha%s.png"%frameCounter, frame)
        cv2.waitKey(200)
    
    elif(frameCounter > int(endFrame[newPath])):
        newPath += 1


    frameCounter += 1
    



# videoCapture = cv2.VideoCapture(filepath)

# succ = True

# i = 0
# while(succ):
#     i = i + 1
#     succ , frame = videoCapture.read()
#     cv2.imwrite("Color/alpha%s.png"%i,frame)
#     cv2.waitKey(500)
# # print(succ)
# # print(frame)
# # cv2.imshow(#frame)


