import sys
import re


class Concordance:

    def __init__(self, filename, exceptions):
        self.filename = filename
        self.exception_file = exceptions
        self.number_args = len(sys.argv)
    
    # Finds all the exclusion words
    def __read_exclusion_words(self):
        if self.number_args <=2:
            self.fixed_exclusion_words = []
        else:
            with open(self.exception_file, "r") as exclusion_file:
                exclusion_words = exclusion_file.readlines()
            exclusion_file.close()

            self.fixed_exclusion_words = []
            for element in exclusion_words:
                self.fixed_exclusion_words.append(element.strip())

    # Finds all the input file words
    def __get_input_words(self):        
        # Reads file line by line
        with open(self.filename, "r") as input_file:                     
            self.raw_input_text = input_file.readlines()
        input_file.close()

        # Quits if the file is empty
        if len(self.raw_input_text) < 1:
            exit()

    # Removes all the punctuation from our input text  
    def __remove_punctuation(self):
        self.new_input_text = []
        self.raw_input_text = []
        for lines in self.input_text:
            self.new_input_text.append(re.sub(r"([^\w\s'-]+)", " " , str(lines.strip())))
            self.raw_input_text.append(lines)    
    
    # Removes all the exception words from our input_words
    def __remove_exception_words(self):
        input_words = []
        for element in self.new_input_text:
            input_words.extend(element.split())
        
        self.new_input_words = []
        for word in input_words:                
            if word.lower() not in self.fixed_exclusion_words:
                self.new_input_words.append(word.lower())
            else:
                continue
    
    # Removes duplicate words
    def __remove_duplicate_words(self):
        self.sorted_unique_words = sorted(list(set(self.new_input_words)))

    # Finds the longest word in the string
    def __longest_word(self):
        self.longest_word = len(max(self.sorted_unique_words, key = len))

    def full_text(self):
        # Method to get all exclusion words
        self.__read_exclusion_words()
        # Method to get all input words
        self.__get_input_words()
        # Creates a copy so we can manipulate it and use the raw text in the final answer
        self.input_text = self.raw_input_text.copy()
        # Method that removes punctuation from our input words
        self.__remove_punctuation()
        # Method that removes all the exception words from our input_words
        self.__remove_exception_words()
        # Method to remove duplicate words
        self.__remove_duplicate_words()
        # Finds the longest word in the string
        self.__longest_word()

        # Splits the items of the raw input file into single words
        split_text_in_lines = []
        for element in self.raw_input_text:
            split_text_in_lines.append(re.findall(r'\s?(\s*\S+)', element.rstrip()))

        # Pieces it all together, by adding it to a single list
        whitespaceStr = " "
        more_than_once_in_line = "*"
       
        final_concordance = []
        for wordy in self.sorted_unique_words:
            whitespaceStr = " " * ((self.longest_word - len(wordy)) + 2)
            for index, liney in enumerate(split_text_in_lines, 1):
                line_lower = [re.sub(r"([^\w\s'-]+)", " " , lines).lower().strip() for lines in liney]
                if wordy in line_lower:
                    if line_lower.count(wordy) > 1:
                        liney = ' '.join(map(str, liney))
                        final_concordance.append(wordy.upper() + whitespaceStr + liney + " " + "(" + str(index) + more_than_once_in_line + ")")
                    else:
                        liney = ' '.join(map(str, liney))
                        final_concordance.append(wordy.upper() + whitespaceStr + liney + " " + "(" + str(index) + ")")    
            else:
                continue
                
        return final_concordance