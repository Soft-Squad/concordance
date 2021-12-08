# Concordance - Keyword-Out-Of-Context
Alphabetical list of keywords, contained in a .txt file, with citations of the passages in which they occur. Someone using a concordance is therefore able to look up a 
word of interest to them for that text, and find all the locations (line numbers) where the word is used. 

Developed for SENG265 - Software Development Methods Summer 2021 - UVic

## Installation and Information
To install, simply download all files. 
With respect to punctuation:
  Words with a dash are considered a singular word.
  Words with uppercase and lowercase letters are considered the same word.
  Words that end with 's and 't are considered part of the word.
  Double quotes and parenthesis are NOT considered part of the word.
  Other punctuation such as: commas (“,”), periods (“.”), colons (“:”), semi-
  colons (“;”), exclamation marks (“!”) and question marks (“?”) may appear at 
  the end of a word. These are not to be considered part of the word. 

## Usage
```./official_tester4.py -e <exclusion_file_name.txt> <input_file_name.txt>```
  or 
```./official_tester4.py <input_file_name.txt> -e <exclusion_file_name.txt>```

## Testing
```./official_tester4.py <input_file_name.txt> -e <exclusion_file_name.txt> | diff <output_file_name.txt>```
