import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as file:
            text_string = file.read()

        return (text_string)


class WordList:
    def __init__(self, text_string):
        self.list = [ ]
        self.text = text_string
        self.word_count = {}

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        self.text = self.text.lower().strip().split()
        transformed_words = []
        for word in self.text:
            if word not in STOP_WORDS:
                transformed_words.append(word.strip(string.punctuation))
        self.list = transformed_words

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        raise NotImplementedError("WordList.remove_stop_words")

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        word_count = {}
        for words in self.list:
            if words in word_count:
                word_count[words] += 1
            else:
                word_count[words] = 1

        return word_count

class FreqPrinter:
    """Handles a dictonary of word frequencies"""
    def __init__(self, freqs):
        self.freqs = freqs #this is a dictionary
    

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """



        

        working_words = sorted(self.freqs.items(), key=lambda seq: seq[1], reverse = True)
        for words, count in working_words:
            print(f"{words:>20} | {(count)} {(count * '*'):<20}")

        
        # sorted_words = sorted(self.freqs.items(), key= use_count_as_key, reverse=True)
        # for word, count in sorted_words:
        #     print(
        #         f"{word.rjust(longest_word_length +1)}",
        #         "|",
        #         str(count).ljust(4),
        #         ('*'*count),
        #     )


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list= WordList(reader.read_contents())
        word_list.extract_words()
        # print(word_list.list)
        # print(word_list.get_freqs())
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
