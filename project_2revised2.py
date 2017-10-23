
EMPTY = '::END::'

from my_random import randint

# This function takes a text file, reads it, and returns a string of all the text in the file
def read_corpus(filename):
    with open(filename) as file:
        text = file.read()
    return text




# This function takes a single string and cleans it of unnecessary punctuation and spaces
def clean_word(word):
    g = word.strip('! " # $ % & ( ) * + = . / : ; < = > ? @ [ \ \ ] ^ , - _ ` { | } ~ ')
    w = g.replace(" ", "")
    m = w.replace("-", "")
    return m.lower()




# This function takes a string of text and returns a nested list of lists of the words in each line
def prepare_corpus(text):
    my_nested_list = []
    for line in text.strip().splitlines():
        line_list = []
        for word in line.split(" "):
            word = clean_word(word)
            line_list.append(word)
        my_nested_list.append(line_list)
    return my_nested_list



# This function takes a nested list and returns a bigram dictionary where there are words as keys and small inner
# dictionaries as values.
def build_bigrams(lines):
    outer_dict = {}
    for line in lines:
        old_word = '::END::'
        line.append('::END::')
        for word in line:
            first_word = old_word
            second_word = word
            old_word = second_word
            if (first_word,) not in outer_dict:
                outer_dict[(first_word,)] = {}
            if second_word in outer_dict[(first_word,)]:
                outer_dict[(first_word,)][second_word] += 1
            if second_word not in outer_dict[(first_word,)]:
                outer_dict[(first_word,)][second_word] = 1
    return outer_dict




def build_trigrams(lines):
    tri_dict = {}
    for line in lines:
        old_word = '::END::'
        line.append('::END::')
        for word in line:
            first_word = old_word
            second_word = first_word
            third_word = word
            old_word = third_word
            if first_word not in tri_dict:
                tri_dict[first_word] = {}
            if second_word in tri_dict[first_word]:
                tri_dict[first_word][second_word] += 1
            if second_word not in tri_dict[first_word]:
                tri_dict[first_word][second_word] = 1
            if third_word in tri_dict[second_word]:
                tri_dict[second_word][third_word] += 1
            if third_word not in tri_dict[second_word]:
                tri_dict[second_word][third_word] += 1
    return tri_dict


# This function takes a nested list of words and corresponding values and returns a random term based on the total of
# the values.
def weighted_random_draw(weights):
    total = 0
    for list in weights:
        value = list[1]
        term = list[0]
        total += value
    rand_int = randint(1, total)
    sum = 0
    for x in sorted(weights):
        value = x[1]
        term = x[0]
        sum += value
        if sum >= rand_int:
            return term

# This function takes a bigram dictionary and a word (context) and returns a random term.
def find_next_word(ngrams, context):
    if context not in ngrams:
        return None
    if context in ngrams:
        inner_dicts = ngrams[context]
        b = list(inner_dicts.items())
        random_term = weighted_random_draw(b)
    return random_term





# This function takes a bigram dictionary and returns a sentence (a string).
def generate_sentence(bigrams):
    previous_word = '::END::'   #initialize the sentence
    next_word = ''
    sentence = [previous_word]  #initialize the list
    while next_word != '::END::':
        next_word = find_next_word(bigrams, (previous_word,))
        sentence.append(next_word)
        previous_word = next_word
        x = " ".join(sentence)
        m = x.replace('::END::', "")
    return m.strip()




def main():
    n = 'lyrics.txt'
    string_of_text = read_corpus(n)
    prep_corpus = prepare_corpus(string_of_text)
    bigrams = build_bigrams(prep_corpus)
    sentence = generate_sentence(bigrams)
    return print(sentence)

if __name__ == '__main__':
    main()