OpenTerminal
============

A SublimeText plugin to add a **Open in Terminal** menu option...

### How to install

- Add Repository：`Preference` → `Packages Control` → Select `Add Repository`, Input: `https://github.com/fffilo/OpenTerminal`, Enter.
- Install Package：`Preference` → `Packages Control` → Select `Install Package`, Input: `OpenTerminal`, Enter.

### How to use

![OpenTerminal Context](screenshot-1.png)

![OpenTerminal Side Bar](screenshot-2.png)

![OpenTerminal Command](screenshot-3.png)

### Settings

You can change your terminal application in your settings (`Preferences → Package Settings → Open Terminal → Settings - User`).

The `command` may be either a direct string:

###### Windows
```JSON
"command": "cd \"{0}\" && start \"Terminal\" cmd"
```

###### Linux

```JSON
"command": "gnome-terminal --working-directory=\"{0}\""
```

###### OSX

```JSON
"command": "open -a Terminal \"{0}\""
```

or it may be a dictionary keyed off what `sublime.platform()` returns, so it may be customized on a per-platform basis:

```JSON
{
	"command": {
		"linux": "gnome-terminal --working-directory=\"{0}\"",
		"osx": "open -a Terminal \"{0}\"",
		"windows": "cd \"{0}\" && start \"Terminal\" cmd"
	}
}
```
