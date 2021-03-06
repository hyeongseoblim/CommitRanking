import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class draw_chart(object):
	def __init__(self, file_path):
		self.file_path = file_path

	def bar_chart(self):
		data = pd.read_csv(self.file_path)
		#Set data to list()
		UserName = data.UserName.tolist()
		CommitCount = data.CommitCount.tolist()

		fig = plt.figure(figsize=(12, 8))
		ax = fig.add_subplot(111)
		
		ypos = np.arange(len(UserName))
		rects = plt.barh(ypos, CommitCount, align='center', height=0.5)
		plt.yticks(ypos, UserName)
		plt.xlabel(data.columns[0])
		plt.show()
