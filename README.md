# Group Members

- **Sofía Isaareth Flores Suárez**
- **Paula Inés Llanos López**

## Operating System Version

- **Windows 11**

## Programming Language Used

- **Python**

## Implementation Tools

- **Visual Studio Code**

## Instructions

1. Download the `.zip` file and extract its contents.
2. Inside the folder, you will find the `main.py` file, which contains the proposed implementation code.
3. The `input.txt` file includes the words to be processed.
4. The output will check if each word is accepted. If a word is accepted, `yes` will be displayed; if not, `no` will be displayed.

## Proposed CNF Grammar

The context-free grammar is defined as follows:

**G = ({S, A, I, D}, {(, )}, P, S)**

where P is the set of productions:

- **S → ID | IA | SS**
- **A → SD**
- **I → (**
- **D → )**

### Accepted Strings by the Grammar

- `()`
- `(()`
- `((()))`

### Rejected Strings by the Grammar

- `()((`
- `(()))`
- `)(`
