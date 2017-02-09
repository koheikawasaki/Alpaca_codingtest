"""Given a set of two dimensional points P 
(e.g. [(1.1, 2.5), (3.4, 1.9)...]; the size of set can be 100s), 
write a function that calculates simple K-means. 
The expected returned value from the function is 1) 
a set of cluster id that each point belongs to, and 2) 
coordinates of centroids at the end of iteration."""

import numpy as np
import math
class Kmeans:
	index_cluster = []
	X = []
	Y = []
	k =0
	cX = []
	cY = []
	count = 0
	def __init__(self, setP, K):
		datatmp = np.asarray(setP, dtype=np.float)
		self.X = np.asarray(datatmp[:,0])
		self.Y = np.asarray(datatmp[:,1])
		self.k = K
		minx = np.min(self.X)
		maxx = np.max(self.X)
		miny = np.min(self.Y)
		maxy = np.max(self.Y)
		self.cX = minx + (maxx -minx)*np.random.rand(K)
		self.cY = miny + (maxy -miny)*np.random.rand(K)
		self.index_cluster = np.zeros(len(self.X), dtype = np.int16)
		self.findnearest(self.X, self.Y, self.cX, self.cY)
		# x = self.X
		# y = self.Y
		# plt.scatter(x, y, c = 'b')
		# plt.scatter(self.cX, self.cY, c ='r')

	def fit(self):
		previous = self.index_cluster
		self.cluseter_mean(self.X, self.Y, self.cX, self.cY)
		self.findnearest(self.X, self.Y, self.cX, self.cY)
		self.count +=1
		if self.count > 1000 or all(previous == self.index_cluster):
			return self.index_cluster
		else:
			return fit()
	def findnearest(self, X, Y, cX, cY):
		for i in range(len(X)):
			distls = np.zeros(len(cX))
			for j in range(len(cX)):
				distls[j] = self.dist(X[i], Y[i], cX[j], cY[j])
			self.index_cluster[i] = distls.argmin()
	def cluseter_mean(self, X, Y, cX, cY):
		for i in range(self.k):
			self.cX[i] = np.mean(self.X[np.where(self.index_cluster == i)])
			self.cY[i] = np.mean(self.Y[np.where(self.index_cluster == i)])
				
		# self.index_cluster = map(np.argmin, distls)
	def dist(self, x, y, cx, cy):
		return math.sqrt((x-cx)**2+(y-cy)**2)


a= np.random.randint(100, size=(100,2))

kmeans = Kmeans(a, 5)
colorlist=['b', 'g', 'c', 'm', 'y']
cluster_idx = kmeans.fit()
for i in range(5):
    x = a[:,0][np.where(cluster_idx == i)]
    y = a[:,1][np.where(cluster_idx == i)]
    plt.scatter(x, y, c = colorlist[i])

