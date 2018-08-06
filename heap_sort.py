import math

class HeapBuilder:
	def __init__(self):
		self._data = [3,39,61,91,57,22,75,89,9,90,63,78,28,73,20]

	def leftChild(self, i):
		return (2 * i) + 1	
	def rightChild(self, i):
		return (2 * i) + 2

	def makeHeap(self, i):
		maxindex = i
		lchild = self.leftChild(i)

		if lchild < len(self._data) and self._data[lchild] < self._data[maxindex]:
			maxindex = lchild

		rchild = self.rightChild(i)

		if rchild < len(self._data) and self._data[rchild] < self._data[maxindex]:
			maxindex = rchild

		if i != maxindex:
			self._data[maxindex], self._data[i] = self._data[i], self._data[maxindex]
			self.makeHeap(maxindex)

	def loopation(self):
		ulti = len(self._data) - 1
		for x in range(math.ceil(ulti/2) -1, -1, -1):
			self.makeHeap(x)

	def Solver(self):
		self.loopation()
		print(self._data)

if __name__ == '__main__':
	heap_builder = HeapBuilder()
	heap_builder.Solver()