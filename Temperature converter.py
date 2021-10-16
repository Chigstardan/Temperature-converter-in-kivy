import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Converter(BoxLayout):
	result = ObjectProperty(None)
	def convert(self):
		celsius = self.result.text
		self.result.text = str(9 / 5 * int(celsius) + 32)
	
	
class TemperatureConverterApp(App):
	def build(self):
		return Converter()
		

		
	
if __name__ == "__main__" :	
	TemperatureConverterApp().run()

		