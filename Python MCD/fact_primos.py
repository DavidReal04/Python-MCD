class FactoresPrimos():

	def __init__(self, controller):
		self.controller = controller

	def calcularMCD(self, num1, num2):
		bandera=False
		mcd = 1
		div = 2
		while(num1!=1 and num2!=1):
			while(num1%div==0 or num2%div==0):
				if(num1%div==0 and num2%div==0):
					bandera=True

				if(num1%div==0):
					num1 = num1//div

				if(num2%div==0):
					num2 = num2//div

			if(bandera):
				mcd*=div
			div+=1
		
		return mcd;