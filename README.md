# neuron
- a line-oriented editor,
- a sticky note for simple tasks,
- a typewriter for writing,
- a text editor for programming,
- and a simple calculator.
- **An editor which helps you *think*.**

## Introduction
This text editor provides a simple command-line interface for basic text editing tasks. Below is a manual explaining the available commands and their functionalities.
* neuron is provided WITHOUT any warranty.
* IMPORTANT: do NOT press Control-C, otherwise it will forcibly stop the editor.

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
- **nn**: insert a newline at the cursor
- **aa**: add numbers in the specified range of lines.
- **xx**: subtract.
- **tt**: multiply.
- **dd**: divide.
- **cx**: Convert the current line to an integer.
- **q**: Add keywords. Keywords are divided by space.
- **z**: Erase a specific keyword.
- **zz**: Erase all keywords.
- **w**: Print keywords.
- **r**: Select and order keywords by their index numbers.
- **rr**: Swap keyword lists.
- **ww**: Move keywords to the cursor in the current line.
- `add <a> <b>`: Add two numbers.
- `sub <a> <b>`: Subtract one number from another.
- `tx <a> <b>`: Multiply two numbers.
- `dd <a> <b>`: Divide one number by another.
- `dr <a> <b>`: Divide one number by another, returning the remainder.
- `xx <a> <b>`: Raise a number to the power of another. (xt in neuron)
- `str <a> <b>`: Concatenate two strings.
- `cut <string> <start> <end>`: Cut a substring from a string.
- `ssc <string1> <string2>`: Concatenate two strings with a space.
- 'ed \<encoding\>': change file encoding. utf-8 by default.
- 'sb': save current buffer.
- 'bs': load the specified buffer. req: buffer index number
- 'b.': print the specified buffer. req: same as the above.
- 'ab': append the specified buffer after current buffer.
- 'bb': Delete a buffer.
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

## Example Usage
- To append text to the current line: a [content]
- To print the current line: l
- To set the pointer: p [column]
- To delete characters before the cursor: x [number of chars to erase]
- To delete the specified line: d [line number]
- To insert a new line after the specified line: o [line number]
- To quit the editor: quit

Refer to the commands above for additional functionalities and examples.

# Fission Scripting Language Manual

## Introduction
The Fission Scripting Language is a simple language designed for scripting within the text editor. It allows users to define and execute custom commands not included in neuron. Below is a beginner's manual explaining the syntax and usage of the Fission Scripting Language.

## Basic syntax
- line 1: prep (argument; condition, repeat count, constant, etc)
- line 2: command

### example:
- prep 10
- prep 20
- add
- o

- output: 30.0

### example 2:
- prep Hello
- prep  world
- comb
- o

- output: Hello world

### example 3: square of 20
- bs
- prep 20
- o
- be
- prep 20
- rr
- sum
- o

- Remember to run fs (starting index) (ending index) in neuron after you complete the code.

## Commands

### `bs` and `be` - Block Start and Block End
- `bs`: Marks the beginning of a block.
- `be`: Marks the end of a block.

### `if` - Conditional Statement
- Syntax: `if`
- Executes the block if the specified condition is true.

### `rr` - Repeat Block
- Syntax: `rr`
- Repeats the block specified number of times.

### `rp` - Reset Parameters
- Resets the parameters, clearing any existing values.

### `e` - Eliminate Elements
- Syntax: `e`
- Removes elements at the specified indices from the argument list.

### `o` - Output Result
- Returns the current argument list as the output.

### `comb` - Concatenate Strings
- Syntax: `comb`
- Concatenates the first two elements as strings.

### `add` - Add Numbers
- Syntax: `add`
- Adds the first two elements as numbers.

### `sub` - Subtract Numbers
- Syntax: `sub`
- Subtracts the first element from the second element.

### `cut` - Cut String
- Syntax: `cut`
- Extracts a substring from the third element based on the specified start and end indices.

### `sum` - Sum Numbers
- Syntax: `sum`
- Sums all the numbers in the argument list.

### `prep` - Prepare Element
- Syntax: `prep value`
- Prepares the specified value to add to the argument stack.

## Note
- The Fission Scripting Language operates on a list of particles, and each particle represents a command or value.
- Commands `bs` and `be` define blocks of code.
- Use `if` for conditional statements and `rr` for repeating blocks.
- Various commands manipulate the argument list (`arg`), such as `e` for eliminating elements, `comb` for concatenating strings, and others for numerical operations.

Experiment with these commands to create custom scripts tailored to your needs within the text editor.

# Reactor (Pre-Fission Processor) Manual

## Introduction
The Reactor is a pre-fission processor designed to simplify the usage of the Fission Scripting Language. It provides functions for common mathematical operations and encapsulates the complexities of interacting with the Fission language. Below is a manual explaining the functions available in the Reactor.

## Functions
- usage:
- line 1: reactor function (Fs___)
- line 2: fission language code(example: 'o')
- **Replace lines of fission script with just a few reactor functions.**

### `FsAdd(a, b)`
- Adds two numbers.
- Parameters:
  - `a`: First number.
  - `b`: Second number.
- Returns the result of the addition.

### `FsSub(a, b)`
- Subtracts one number from another.
- Parameters:
  - `a`: The number to be subtracted from.
  - `b`: The number to subtract.
- Returns the result of the subtraction.

### `FsMx(a, b)`
- Multiplies two numbers.
- Parameters:
  - `a`: First number.
  - `b`: Second number.
- Returns the result of the multiplication.

### `FsDv(a, b)`
- Divides one number by another, returning the quotient.
- Parameters:
  - `a`: The dividend.
  - `b`: The divisor.
- Returns the quotient.

### `FsDr(a, b)`
- Divides one number by another, returning the remainder.
- Parameters:
  - `a`: The dividend.
  - `b`: The divisor.
- Returns the remainder.

### `Fexp(a, b)`
- Raises a number to the power of another.
- Parameters:
  - `a`: The base.
  - `b`: The exponent.
- Returns the result of the exponentiation.

## Summary
These functions allow you to perform common mathematical operations using a simplified interface. Use them to interact with the Fission Scripting Language without directly handling the underlying complexities.

# Neutron Text Editor Manual

## Introduction

Neutron combines the power of a simple text editing interface of Neuron with a pre-fissionscript processor called the Reactor, which simplifies the usage of the Fission Scripting Language. The Fission Scripting Language allows users to execute commands and manipulate text using concise and expressive syntax.

## Getting Started

### Basic Commands

- `l`: Print the current line.
- `d`: Delete line(s) specified in the list.
- `k`: Kill lines in the specified range.
- `o`: Insert a line at the specified position.
- `lo`: Append a line at the end.
- `n`: Set the current line to the specified line.
- `l.`: Print all lines with index.
- `lm`: Print lines within a specified range with index.
- `ml`: Print lines within a specified range without index.
- `.l`: Print all lines without index.
- `quit`: Exit the editor.
- `of <filename>`: Open a file and load its content into the editor.
- `wf <filename>`: Write the editor content to a file.
- `ecl`: Clear all editor lines.
- `m <line_number>`: Copy the current line to the specified line.
- `i <line_number>`: Insert content into the specified line.
- `ll`: Print the last line number.
- `ii <indentation>`: Set auto indentation.

### Advanced Commands

- `cx`: Convert the current line to an integer.
- `q <keywords>`: Initialize keywords.
- `z <keyword>`: Erase a keyword.
- `zz`: Erase all keywords.
- `w`: Print current keywords.
- `r <order>`: Order keywords based on the specified order.
- `rr`: Swap keyword lists.
- `ww`: Move keywords to the current line.
- `fs <start> <end>`: Execute Fission Script on specified lines.

### Fission Scripting Language Integration

- `add <a> <b>`: Add two numbers.
- `sub <a> <b>`: Subtract one number from another.
- `tx <a> <b>`: Multiply two numbers.
- `dd <a> <b>`: Divide one number by another.
- `dr <a> <b>`: Divide one number by another, returning the remainder.
- `xx <a> <b>`: Raise a number to the power of another. (xt in neuron)
- `str <a> <b>`: Concatenate two strings.
- `cut <string> <start> <end>`: Cut a substring from a string.
- `ssc <string1> <string2>`: Concatenate two strings with a space.

### Fission Scripting Language Functions

- `FsAdd(a, b)`: Add two numbers.
- `FsSub(a, b)`: Subtract one number from another.
- `FsMx(a, b)`: Multiply two numbers.
- `FsDv(a, b)`: Divide one number by another, returning the quotient.
- `FsDr(a, b)`: Divide one number by another, returning the remainder.
- `Fexp(a, b)`: Raise a number to the power of another.
- `Fstr(a, b)`: Concatenate two strings.
- `Fstc(istr, b, c)`: Cut a substring from a string.
- `Fssr(a, b)`: Concatenate two strings with a space.

## Example Usage

```plaintext
> l
> lo
> n 1
> l
> fs 1 2
> add 5 3
> sub 10 4
> tx 3 5
> dd 20 4
> dr 15 7
> xx 2 3
> str Hello World
> cut World! 7 12
> ssc Hello, World!
> ww
> quit
```

## Notes

- Use `:n` to reference the nth line in the editor.
- Fission Scripting Language functions are available for more complex operations.
- Combine Fission commands with text editor commands for powerful text manipulation.
