class AlgoritmoEuclidiano():

	def __init__(self, controller):
		self.controller = controller

	def calcularMCD(self, num1, num2):
		res=0
		div=0
		while num2!=0:
			res=num1%num2
			div=num1//num2
			num1=num2
			num2=res
		return num1
