class CalculoDivisores():

	def __init__(self, controller):
		self.controller = controller

	
	def calcularMCD(self, num1, num2):
		divisores1=[]
		divisores2=[]
		mcd=0
		for i in range(1, num1+1):
			if num1%i==0:
				divisores1.append(i)

		for i in range(1, num2+1):
			if num2%i==0:
				divisores2.append(i)

		if(len(divisores1)>len(divisores2)):
			for div in divisores2:
				if div in divisores1 and div>mcd:
					mcd=div
		else:
			for div in divisores1:
				if div in divisores2 and div>mcd:
					mcd=div

		return mcd


