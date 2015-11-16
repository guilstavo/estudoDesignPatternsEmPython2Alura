class Impressao(object):

	def visita_soma(self, soma):
		print'(',
		# visita expressao esquerda
		print '+',
		# visita expressao direita
		print ')',
		

	def visita_subtracao(self, subtracao):
		print'(',
		# visita expressao esquerda
		print '-',
		# visita expressao direita
		print ')',

	def visita_numero(self, numero):

		print numero.avalia(),