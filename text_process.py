
import re, string, unicodedata
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words


  def remove_punct(self,text):
        """
        take string input and clean string without punctuations.
        use regex to remove the punctuations.
        """
    return ''.join(c for c in text if c not in punctuation)   


def remove_Tags(self,text):
        """
        take string input and clean string without tags.
        use regex to remove the html tags.
        """
        cleaned_text = re.sub('<[^<]+?>', '', text)
    return cleaned_text


  def spelling_correction(self, word1):
        global corrected_word_dict 
        corrected_word_dict=dict()
        global corrected_word_list 
        corrected_word_list=[]
        global processed_word_list 
        processed_word_list=[]
        #for each chat/record/observation as passed, check individual tokens if present in 'word_list_mispell'
        #if present, follow below process
        corrected_word = word1
        if word1 not in processed_word_list:
            if word1 not in corrected_word_list:
                if word1 in word_list_mispell:
                    final_score_word_list = []
                    dict_key_list = []
                    threshold = 0.98
                    for word2 in word_list_correct:   
                        score = float(jellyfish.jaro_winkler(word1,word2))
                        if not score==1.0:
                            if (score>=threshold):
                                my_dict = dict()
                                word_combo = list()
                                word_combo.append(word1)
                                word_combo.append(word2)
                                my_dict[score] = word_combo
                                if not len(my_dict)==0:
                                    final_score_word_list.append(my_dict)

                    if not len(final_score_word_list)==0:
                        for dict_in_list in final_score_word_list:
                            for key in dict_in_list:
                                dict_key_list.append(key)
                        if not len(dict_key_list)==0:
                            dict_key_list = sorted(dict_key_list, reverse=True)
                            #for the highest score, use the correct word from it and change the given misspelled word
                            for dict_item in dict_key_list:
                                for list_dict in final_score_word_list:
                                    if not len(list_dict)==0:
                                        for key in list_dict:
                                            if key==dict_item:
                                                if list_dict[key][0]==word1:
                                                    corrected_word = list_dict[key][1]
                                                    corrected_word_dict[word1] = corrected_word
                                                    corrected_word_list.append(word1)
            else:
                for key in corrected_word_dict:
                    if word1 == key:
                        corrected_word = corrected_word_dict[word1]
            
            processed_word_list.append(word1)
        return corrected_word




def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        # print(word)
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas




def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    words = stem_words(words)
    words = lemmatize_verbs(words)
    words = spelling_correction(words)
    words = remove_Tags(words)


    return words


#words = str("jabscjbjb ")

words = nltk.word_tokenize(words)



words = normalize(words)
print(words)
words = ' '.join(map(str, words))
print(words)