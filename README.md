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

If you wish to change your terminal application (in my example instead of using `gnome-terminal` I will use `terminator`) just change command in your settings (`Preferences → Package Settings → Open Terminal → Settings - User`):

```diff
{
	"command": {
-		"linux": "gnome-terminal --working-directory=\"{0}\"",
+		"linux": "terminator --working-directory=\"{0}\"",
		"osx": "open -a Terminal \"{0}\"",
		"windows": "cd \"{0}\" && start \"Terminal\" cmd"
	}
}
```