from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		#Zdislava jde na stranku a omylem zada prazdnej predmet
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')
	
		#homepage se refreshne a ukazuje chybovou hlasku ze predmet nemuze bejt
		#prazdnej

		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#Zdislava to zkusi znova s nakym predmetem, coz funguje
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		#Ted zkusi znova prazdnej predmet
		self.get_item_input_box().send_keys('\n')

		#Podobny varovani, ale na strance s jejim seznamem
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#opravi to zadanim nejakyho textu
		self.get_item_input_box().send_keys("Make tea\n")
		self.check_for_row_in_list_table("1: Buy milk")
		self.check_for_row_in_list_table("2: Make tea")

