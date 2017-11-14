"""A text content analyzer to find statistics on essays and articles."""
from collections import Counter
import sys
import re


def _extractor(file_path):
    """Extract and lowercase text."""
    with open(file_path) as file:
        raw_text = file.read()
    return raw_text.lower()


def _word_counts(text):
    """Return a counter object of the text."""
    split_text = re.split(r'[\s,.!?:;\(\)/]', text)
    split_text_cleaned = [word for word in split_text if word != '']
    word_counts = Counter(split_text_cleaned)
    return len(split_text_cleaned), len(word_counts)


def _sentence_counts(text):
    """Return a counter object of sentences in the text."""
    sentence_split = re.split(r'[.!?]', text)
    sentences = [sentence for sentence in sentence_split if sentence != '']
    return sentences


def main(file_path):
    """Main implementation of the text analyzer."""
    raw_text = _extractor(file_path)
    total_word_count, total_unique_words = _word_counts(raw_text)
    total_sen = _sentence_counts(raw_text)
    avg_sen_len = total_word_count / len(total_sen)

    return total_word_count, total_unique_words, len(total_sen), avg_sen_len


if __name__ == '__main__':
    wc, uc, ts, asl = main(sys.argv[1])
    print(
'''
Total word count: {}
Unique words: {}
Sentences: {}
Average Sentence Length: {}
'''.format(wc, uc, ts, asl))
