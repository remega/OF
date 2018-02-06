#-*-coding:utf-8 -*-
import cv2
import os

# domain = ['soccer','parade','mountain_climbing','skate']
read_path = 'G:/database/statistics/database/'
VideoNameFile = 'Testlist.txt'
videofile = open(VideoNameFile, 'r')
allline = videofile.readlines()
save_path = 'G:/LEDVO2017/opticalflow/OF/Deep360Pilot-CVPR17-tf1.2/misc/data/frame_test/'

for line in allline:
	lindex = line.index('\t')
	VideoIndex = int(line[:lindex])
	VideoName = line[lindex + 1:-1]
	vc = cv2.VideoCapture(read_path + VideoName + '/' + VideoName + '.mp4')  # 读入视频文件
	frame_total = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	print(frame_total)
	for c in range(frame_total):
		if vc.isOpened():  # 判断是否正常打开
			rval, frame = vc.read()
		else:
			rval = False

		timeF = 1  # 视频帧计数间隔频率
		if not os.path.exists(save_path+VideoName):
			os.makedirs(save_path+VideoName)
		if rval:  # 循环读取视频帧
			if (c % timeF == 0):  # 每隔timeF帧进行存储操作
				frame = cv2.resize(frame, (480, 240))
				cv2.imwrite(save_path+VideoName+'\\'+'frame'+ '_' + str(c+1) + '.jpg', frame)  # 存储为图像
			cv2.waitKey(1)
	print('finish')
	vc.release()
print('All finish')