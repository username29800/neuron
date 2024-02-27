# neuron
a line editor which helps you think

## Introduction
This text editor provides a simple command-line interface for basic text editing tasks. Below is a manual explaining the available commands and their functionalities.
* neuron will provide a simple calculator soon.

## Editor Commands

- **a**: Append to the current line.
- **l**: Print the current line with the cursor mark.
- **p**: Set the pointer(cursor).
- **x**: Delete characters before the cursor.
- **d**: Delete the specified line.
- **o**: Insert a new line after the specified line.
- **lo**: Append a new line at the end of the document.
- **y**: Yank (copy) the specified line.
- **n**: Set the current line.
- **pi**: Paste the copied line into the current line(after the cursor).
- **l.**: Print all lines with line numbers.
- **lm**: Print lines within a specified range with line numbers.
- **ml**: Print lines within a specified range without line numbers.
- **.l**: Print all lines without line numbers.
- **quit**: Quit the editor(note: save the file before you leave).
- **of**: Open a file for editing.
- **wf**: Write the current document to a file(note: this could overwrite an existing file).
- **ecl**: Clear all editor lines(irreversible).
- **fn**: Forward search with count.
- **bn**: Backward search with count.
- **pl**: Move the pointer to the end of the line.
- **pp**: Set a relative cursor position.
- **m**: Copy the current line to a specified line. The original line is pushed downwards.
- **i**: Insert the current line into a specified line. Replaces the original line.
- **ll**: Print the last line number.
- **h** or **;**: Display help.(incomplete)
- **n**: insert a newline at the cursor

## Additional Commands

- **ol**: Append input to the document.
- **ii**: Set auto indentation.
- **j**: Join lines within a specified range.
- **jl**: Join lines specified in a list.
- **s**: Split a joined line into individual lines. Lines are appended at the end of the document.
- **ss**: Split the line while keeping its position.
- **v**: Move a line to a specified position. Replaces the original line.
- **c**: Copy and paste a line to a specified position. Replaces the original line.
- **e**: Empty the current line.(irreversible)
- **b**: Backup lines after a specified line. Useful for appending from the middle of the document.
- **bb**: Restore backed-up lines.
- **jn**: Join lines within a specified range without a newline.
- **jnn**: Join lines specified in a list without a newline.
- **f**: Search and replace within a given count.
- **g**: Search and replace all occurrences.

**Note:** Replace `ed('command')` with the actual 'command' to execute.

## Example Usage
- To append text to the current line: `ed('a')`.
- To print the current line: `ed('l')`.
- To set the pointer: `ed('p')`.
- To delete characters before the cursor: `ed('x')`.
- To delete the current line: `ed('d')`.
- To insert a new line after the current line: `ed('o')`.
- To quit the editor: `ed('quit')`.

Refer to the commands above for additional functionalities and examples.
