from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Zdislava chce vyzkouset novou stranku, zada adresu
		self.browser.get('http://localhost:8000')

		#podiva se, jesli je v titulu to co ceka (to-do lists)
		self.assertIn('To-Do', self.browser.title)
		self.fail("finish!!")

		#hned muze zadavat veci do seznamu

		#napise 'koupit marmeladu'

		#zmackne enter a stranka se aktualizuje
		#ted ukazuje '1: koupit marmeladu'

		#je tam furt textbox na pridani dalsiho predmetu
		#napise 'udelat palacinky'

		#stranka se aktualizuje a ted ukazuje voba predmety seznamu

		#Zdislava si vsimne, ze stranka ji vygenerovala unikatni url

		#zkusi ho navstivit a je tam jeji seznam

		#vypne prohlizec

if __name__ == '__main__':
	unittest.main(warnings='ignore')
