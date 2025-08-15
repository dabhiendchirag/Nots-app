from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import OneLineListItem

class HomeScreen(MDScreen):
	pass
	
class AddScreen(MDScreen):
	pass
	
class WindowManager(MDScreenManager):
	pass
	
class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style="Light"
		return Builder.load_file("main.kv")
		
	def on_start(self):
		container=self.root.get_screen("home_screen").ids.container
		container.add_widget(
		OneLineListItem(text="hellow friend"
		)
		)
		
	def show_date_picker(self, focus):
	    if  not focus:
	        return
	        
	    date_dialog = MDDatePicker()
	    date_dialog.bind(on_ok=self.on_ok, on_cancel=self.on_cancel)
	    date_dialog.open()
	        
	def on_ok(self, instance, date_value):
	    dt = str(self, date_value)
	    self.root.get_screen("add_screen").ids.created.text = dt
	    instance.dismiss()
	def on_cancel(self, instance, date_value):
	    instance.dismiss()
	    
	    
if __name__ == "__main__":
	MainApp().run()