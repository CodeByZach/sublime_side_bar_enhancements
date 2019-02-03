import sublime
import sublime_plugin
import os


class SideBarEnhancementsEditSettings(sublime_plugin.WindowCommand):
	def run(self, **kwargs):
		STP = sublime.packages_path()
		STPA = os.path.join(STP, "User", "SideBarEnhancements")
		if not os.path.exists(STPA):
			os.makedirs(STPA)

		self.window.run_command("edit_settings", kwargs)


class SideBarEnhancementsOpenwithEditSettings(sublime_plugin.WindowCommand):
	def run(self, **kwargs):
		STP = sublime.packages_path()
		STPA = os.path.join(STP, "User", "SideBarEnhancements", "Open With")
		if not os.path.exists(STPA):
			os.makedirs(STPA)

		self.window.run_command("edit_settings", kwargs)
