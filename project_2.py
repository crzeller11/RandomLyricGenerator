
def read_corpus(filename):
    with open(filename) as file:
        text = file.read()
    return text # outputs a string of the text from the text file

def clean_word(word):
    g = word.strip('! " # $ % & ( ) * + = . / : ; < = > ? @ [ \ \ ] ^ , _ ` { | } ~ ')
    w = g.replace(" ", "")
    m = w.replace("-", "")
    return m.lower() # this outputs a word (a string) that is "cleaned"

def prepare_corpus(text): # the text that goes into this function, should be the output from read_corpus
    my_nested_list = []
    for line in text.strip().splitlines():
        line_list = []
        for word in line.split(" "):
            word = clean_word(word)
            line_list.append(word)
        my_nested_list.append(line_list)
    return my_nested_list


def build_bigrams(lines): # the input for this function should be the nested list from prepare_corpus
    outer_dict = {}
    for line in lines:
        old_word = '::END::'
        line.append('::END::')
        for word in line:
            first_word = old_word
            first_key = (first_word,)
            second_word = word
            old_word = second_word
            if first_key not in outer_dict:
                outer_dict[first_key] = {}
            if second_word in outer_dict[first_key]:
                outer_dict[first_key][second_word] += 1
            if second_word not in outer_dict[first_key]:
                outer_dict[first_key][second_word] = 1
    return outer_dict # This outputs a nested dictionary of tuple keys



from my_random import randint
def weighted_random_draw(weights):
    total = 0
    for list in weights:
        value = list[1]
        term = list[0]
        total += value
    rand_int = randint(1, total)
    # New loop needed to return term at specific value
    # Sum will loop through values in list one by one
    # When the sum is greater than random integer, will return term at that sum
    sum = 0
    for x in weights:
        value = x[1]
        term = x[0]
        sum += value
        if sum >= rand_int:
            return term


# print(weighted_random_draw([['a', 3], ['b', 1]]))
# should return 'a'

# print(weighted_random_draw([['a', 1], ['b', 1]]))
# should return 'a'

# print(weighted_random_draw([['a', 1]]))
# should return 'a'


# The context is exactly what you're looking up in the dictionary, you don't necessarily care about each word in the
# function. What does this mean, you only care about the first word in context tuple?
def find_next_word(ngrams, context):
    for context in ngrams:
        if context not in ngrams:
            return None
        if context in ngrams:
            inner_dicts = ngrams[context]
            list_of_dictionaries = list(inner_dicts.items())
            random_term = weighted_random_draw(list_of_dictionaries)
            return random_term


# Not working when we import one word that we know is in the bigrams
# print(build_bigrams([ ['if', 'you', 'could', 'see', 'that', "i'm", 'the', 'one', 'who', 'understands', 'you'], ['been', 'here', 'all', 'along', 'so', 'why', "can't", 'you', 'see'],['you', 'belong', 'with', 'me'],['you', 'belong', 'with', 'me']]))
#print(find_next_word(x, ('along')))
# print(find_next_word({}, ('hello',)))
# should return None

# print(find_next_word({('hello',): {'world': 1}}, ('hello',)))
# should return 'world'

# print(find_next_word({('hello',): {'from': 1, 'world': 1}}, ('hello',)))
# should return 'world'

# print(find_next_word({('from',): {'the': 1}, ('hello',): {'world': 1, 'from': 1}}, ('hello',)))
# should return 'world'


def generate_sentence(bigrams):
    previous_word = '::END::'   #initialize the sentence
    next_word = ''
    sentence = [previous_word]  #initialize the list
    while next_word != '::END::':
        next_word = find_next_word(bigrams, (previous_word,))
        sentence.append(next_word)
        previous_word = next_word
        x = " ".join(sentence)
    return x.replace('::END::', "")


 pass
'''
initialize the sentence with ::END:: while the next word we pick is not ::END::
get the last we generated in the sentence
get the next word using a weighted random draw add the word to our sentence
'''
x = (build_bigrams([ ['if', 'you', 'could', 'see', 'that', "i'm", 'the', 'one', 'who', 'understands', 'you'], ['been', 'here', 'all', 'along', 'so', 'why', "can't", 'you', 'see'],['you', 'belong', 'with', 'me'],['you', 'belong', 'with', 'me']]))
print(generate_sentence(x))
