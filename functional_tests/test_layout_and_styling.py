from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		#zdislava jde na domovskou stranku
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,768)

		#vsimne si, ze textbox je pekne zarovnanej
		inputbox = self.get_item_input_box() 

		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)

		#zance zadavat novej seznam a vidi ze i tady je pekne vycentrovanej textbox
		inputbox.send_keys('testing\n')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)
	

