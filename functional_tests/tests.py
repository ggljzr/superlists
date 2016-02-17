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

		#zmackne enter a je presmerovana na novy url s jejim seznamem
		#ted ukazuje '1: koupit marmeladu'

		inputbox.send_keys(Keys.ENTER)
		zdislava_list_url = self.browser.current_url

		self.assertRegex(zdislava_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: koupit marmeladu')

		#je tam furt textbox na pridani dalsiho predmetu
		#napise 'koupit vino'

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('koupit vino')
		inputbox.send_keys(Keys.ENTER)

		#stranka se aktualizuje a ted ukazuje voba predmety seznamu
		
		self.check_for_row_in_list_table('2: koupit vino')
		self.check_for_row_in_list_table('1: koupit marmeladu')
	
		#ted prijde novej uzivatel francis

		self.browser.quit()
		self.browser = webdriver.Firefox()

		#francis navstivi home page kde neni zadnej seznam zdislavy
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('koupit marmeladu', page_text)
		self.assertNotIn('koupit vino', page_text)

		#francis zacne novej seznam pridanim novyho predmetu
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('koupit vodku')
		inputbox.send_keys(Keys.ENTER)

		#francis dostane svoje unikatni url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, zdislava_list_url)

		#ani ted nevidi nic ze seznamu zdislavy
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('koupit marmeladu', page_text)
		self.assertNotIn('koupit vino', page_text)


