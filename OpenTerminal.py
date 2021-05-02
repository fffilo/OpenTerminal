import sublime
import sublime_plugin
import os
from subprocess import Popen


class OpenTerminal(sublime_plugin.WindowCommand):

    def _get_paths(self, paths):
        # empty list
        result = []

        # loop paths and add to valid directories
        for path in paths:
            if path == "?filename":
                if not self.window.active_view().file_name() is None:
                    result.append(os.path.dirname(os.path.realpath(self.window.active_view().file_name())))
            elif os.path.isfile(path):
                result.append(os.path.dirname(os.path.realpath(path)))
            elif os.path.isdir(path):
                result.append(os.path.realpath(path))
            else:
                pass

        # remove duplicates
        if len(result) > 0:
            result = list(set(result))

        # finally...
        return result

    def run(self, paths):
        # get command from settings
        settings = sublime.load_settings("OpenTerminal.sublime-settings")
        command  = settings.get("command")
        if isinstance(command , dict):
            command = command.get(sublime.platform())
        paths = self._get_paths(paths)

        # add home directory if list is empty
        if len(paths) == 0:
            paths.append(os.path.expanduser("~"))

        # open each path in terminal
        for path in paths:
            Popen(command.format(path), shell=True)

    def description(self, paths):
        # default caption
        return None

    def is_visible(self, paths):
        # always visible
        return True

    def is_enabled(self, paths):
        return len(self._get_paths(paths)) > 0
