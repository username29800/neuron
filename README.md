# neuron
a line editor which helps you think

# Text Editor Manual

## Introduction
This text editor provides a simple command-line interface for basic text editing tasks. Below is a manual explaining the available commands and their functionalities.

## Editor Commands

- **a**: Append to the current line.
- **l**: Print the current line.
- **p**: Set the pointer.
- **x**: Delete characters before the cursor.
- **d**: Delete the current line.
- **o**: Insert a new line after the current line.
- **lo**: Append a new line at the end of the document.
- **y**: Yank (copy) the current line.
- **n**: Set the current line.
- **pi**: Paste the copied line into the current line.
- **l.**: Print all lines with index numbers.
- **lm**: Print lines within a specified range with index numbers.
- **ml**: Print lines within a specified range without index numbers.
- **.l**: Print all lines without index numbers.
- **quit**: Quit the editor.
- **of**: Open a file for editing.
- **wf**: Write the current document to a file.
- **ecl**: Clear all editor lines.
- **fn**: Forward search with count.
- **bn**: Backward search with count.
- **pl**: Move the pointer to the end of the line.
- **pp**: Set a relative cursor position.
- **m**: Copy the current line to a specified line.
- **i**: Insert the current line into a specified line.
- **ll**: Print the last line number.
- **h** or **;**: Display help.

## Additional Commands

- **ol**: Append input to the document.
- **ii**: Set auto indentation.
- **j**: Join lines within a specified range.
- **jl**: Join lines specified in a list.
- **s**: Split a joined line into individual lines.
- **ss**: Split the line at the specified position.
- **v**: Move a line to a specified position.
- **c**: Copy and paste a line to a specified position.
- **e**: Empty the current line.
- **b**: Backup lines after a specified line.
- **bb**: Restore backed-up lines.
- **jn**: Join lines within a specified range without a newline.
- **jnn**: Join lines specified in a list without a newline.
- **f**: Search and replace within a given count.
- **g**: Search and replace all occurrences.

**Note:** Replace `ed('command')` with the actual command to execute.

## Example Usage
- To append text to the current line: `ed('a')`.
- To print the current line: `ed('l')`.
- To set the pointer: `ed('p')`.
- To delete characters before the cursor: `ed('x')`.
- To delete the current line: `ed('d')`.
- To insert a new line after the current line: `ed('o')`.
- To quit the editor: `ed('quit')`.

Refer to the commands above for additional functionalities and examples.
