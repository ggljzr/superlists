from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Zdislava chce vyzkouset novou stranku, zada adresu
		self.browser.get(self.live_server_url)

		#podiva se, jesli stranka dela to co ceka (to-do lists)
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#je naznacino ze hned muze zadavat veci do seznamu
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item',
		)

		#napise 'koupit marmeladu'

		inputbox.send_keys('koupit marmeladu')

		#zmackne enter a stranka se aktualizuje
		#ted ukazuje '1: koupit marmeladu'

		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: koupit marmeladu')

		#je tam furt textbox na pridani dalsiho predmetu
		#napise 'udelat palacinky'

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('koupit vino')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: koupit marmeladu')
		self.check_for_row_in_list_table('2: koupit vino')
		
		self.fail("dodelat testy!!")

		#stranka se aktualizuje a ted ukazuje voba predmety seznamu

		#Zdislava si vsimne, ze stranka ji vygenerovala unikatni url

		#zkusi ho navstivit a je tam jeji seznam

		#vypne prohlizec

