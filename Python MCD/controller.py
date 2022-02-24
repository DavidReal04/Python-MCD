from view_consola import ViewConsola
from calc_divisores import CalculoDivisores
from fact_primos import FactoresPrimos
from algoritmo_euclidiano import AlgoritmoEuclidiano

class Controller():

	def __init__(self):
		self.view_consola = ViewConsola(self)
		self.calc_divisores = CalculoDivisores(self)
		self.fact_primos = FactoresPrimos(self)
		self.algoritmo_euclidiano = AlgoritmoEuclidiano(self)
		self.funcionar()

	def funcionar(self):
		self.view_consola.mostrarMensaje("Cálculo del Máximo Común Divisor" +
                "\n1. Cálculo de divisores\n2. Descomposición en factores primos\n3. Algoritmo de Euclides"+
                "\nIngrese el número del método que quiera usar:")
		try:
			opcion=self.view_consola.pedirNumero()
			if(opcion==1):
				try:
					num1=0
					num2=0
					while num1<=1:
						self.view_consola.mostrarMensaje("Ingrese el primer número entero positivo")
						num1=self.view_consola.pedirNumero()

					while num2<=1:
						self.view_consola.mostrarMensaje("Ingrese el segundo número entero positivo")
						num2=self.view_consola.pedirNumero()

					if num1<num2:
					    num1=num1+num2
					    num2=num1-num2
					    num1=num1-num2

					self.view_consola.mostrarMensaje("Cálculo de divisores \nEl máximo común divisor de " + str(num1) + " y " + str(num2) + " es "
					+str(self.calc_divisores.calcularMCD(num1, num2)))
				except ValueError:
					self.view_consola.mostrarMensaje("Ingreso erroneo\nHasta Pronto")
				
			elif(opcion==2):
				num1=0
				num2=0
				while num1<=1:
					self.view_consola.mostrarMensaje("Ingrese el primer número entero positivo")
					num1=self.view_consola.pedirNumero()

				while num2<=1:
					self.view_consola.mostrarMensaje("Ingrese el segundo número entero positivo")
					num2=self.view_consola.pedirNumero()

				if num1<num2:
				    num1=num1+num2
				    num2=num1-num2
				    num1=num1-num2

				self.view_consola.mostrarMensaje("Descomposición en factores primos \nEl máximo común divisor de " + str(num1) + " y " + str(num2) + " es "
					+str(self.fact_primos.calcularMCD(num1, num2)))
			elif(opcion==3):
				num1=0
				num2=0
				while num1<=1:
					self.view_consola.mostrarMensaje("Ingrese el primer número entero positivo")
					num1=self.view_consola.pedirNumero()

				while num2<=1:
					self.view_consola.mostrarMensaje("Ingrese el segundo número entero positivo")
					num2=self.view_consola.pedirNumero()

				if num1<num2:
				    num1=num1+num2
				    num2=num1-num2
				    num1=num1-num2

				self.view_consola.mostrarMensaje("Algoritmo de Euclides \nEl máximo común divisor de " + str(num1) + " y " + str(num2) + " es "
					+str(self.algoritmo_euclidiano.calcularMCD(num1, num2)))
			else:
				self.view_consola.mostrarMensaje("Opción Inválida\nHasta Pronto")	
		except ValueError:
			self.view_consola.mostrarMensaje("Opción Inválida\nHasta Pronto")
