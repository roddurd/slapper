import cv2
import numpy as np
import os

class Vidsplitter:
	def __init__(self, filename, frameskip = 4):
		self.video = cv2.VideoCapture(filename)
		self.factor = frameskip
	def split():
		try:
			if not os.path.exists('data'):
				os.makedirs('data')
		except OSError:
			print('Error creating directory of data')

		currentFrame = 0
		while (True):
			ret, frame = self.video.read()
			name = './data/frame' + str(currentFrame) + '.jpg'
			print('Creating...' + name)
			if currentFrame % self.factor == 0:
				cv2.imwrite(name, frame)
			currentFrame += 1
		self.video.release()
		cv2.destroyAllWindows()
