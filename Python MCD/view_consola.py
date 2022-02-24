class ViewConsola():
	
	def __init__(self, controller):
		self.controller = controller
		
	def mostrarMensaje(self, msg):
		print(msg)

	def pedirNumero(self):
		num=input()
		num=int(num)
		return num
	