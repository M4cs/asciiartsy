# asciiartsy
ASCII VT100 Animation Player | Preloaded with 88 VT100 Files from http://artscene.textfiles.com/vt100/

### What is asciiartsy?

Asciiartsy is a small little script I wrote to run VT100 animations in the background on a terminal. Below you can see a GIF of it in action. You can add your own custom VT100 animations.

<p align="center">
  <img src="https://mbcdn.sfo2.digitaloceanspaces.com/ezgif-4-c3d28f793eab.gif" />
</p>

### Requirements

- macOS or Linux (`pv` must be installed on macOS)

- python3.5+

### Installation

If you would like to set the speed of the animations set an `AA_SPEED` Environment Variable in your shell config file.

Example:

```
# Bash
echo "export AA_SPEED=2000" >> ~/.bash_rc

# Zsh
echo "export AA_SPEED=2000" >> ~/.bash_rc
```

Start the script by running:

```
python3 start.py
```

Simple as that!
