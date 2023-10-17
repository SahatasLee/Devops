# Vim Editor

## Mode

1. Normal Mode
2. Edit Mode or Insert Mode
3. Visual Mode

[More Detail](https://www.freecodecamp.org/news/vim-editor-modes-explained/)

## Command

- Press `0` move to the begin of word.
- Press `$` move to the end of word.

### Copy All

To copy all text in Vim, you can use the following command:

1. Press `Esc` to make sure you are in normal mode.
2. `gg` move to top of the file.
3. `v` enter visual mode
4. `G` move to bottom of the file.
5. `y` (yark) copy all words.

### Delete All

To delete all text in Vim, you can use the following command:

1. Open Vim by typing `vim` in your terminal.
2. Press `Esc` to make sure you are in normal mode.
3. Type `:%d` and then press `Enter`.

This command means:
- `:` enters the command-line mode.
- `%` selects all lines.
- `d` deletes the selected lines.

### Search

1. In Normal mode, typing `/` following by your search in your terminal.
2. Press `Enter`
3. Press `n` to find next match, `b` to find a previous word.