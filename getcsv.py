import imageio

video_path = 'G:/database/statistics/database/'
VideoNameFile = 'Testlist.txt'
videofile = open(VideoNameFile, 'r')
allline = videofile.readlines()

with open('./'+"dataset_test.txt","a") as f:
	f.write('ID,Video,Frames,type\n')

i = 0
for line in allline:
	lindex = line.index('\t')
	VideoIndex = int(line[:lindex])
	VideoName = line[lindex + 1:-1]
	cur_video = imageio.get_reader(video_path + VideoName + '/' + VideoName + '.mp4', 'ffmpeg').get_meta_data()
	print(cur_video)
	sum_frames = cur_video['nframes']
	types = 'training'
	with open('./'+"dataset_test.txt","a") as f:
		f.write('%d,%s,%d,%s\n'%(int(i+1),VideoName,int(sum_frames),types))
	i = i + 1
print('finish')
