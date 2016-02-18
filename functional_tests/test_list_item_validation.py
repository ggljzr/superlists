from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		#Zdislava jde na stranku a omylem zada prazdnej predmet
	
		#homepage se refreshne a ukazuje chybovou hlasku ze predmet nemuze bejt
		#prazdnej

		#Zdislava to zkusi znova s nakym predmetem, coz funguje

		#Ted zkusi znova prazdnej predmet

		#Podobny varovani, ale na strance s jejim seznamem

		#opravi to zadanim nejakyho textu
		self.fail('write me!!!')


