def trascript_cleaner(txtFile):
    transcript = open(txtFile)
    transcript_str = transcript.read()
#*************************************************************************************
    # seperates the string a list of words
    import nltk
    from nltk.tokenize import word_tokenize
    transcript_tokens = word_tokenize(transcript_str)
    # convert to lower case (w stands for words)
    transcript_tokens = [w.lower() for w in transcript_tokens]
#*************************************************************************************
    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    transcript_stripped = [w.translate(table) for w in transcript_tokens]
    # remove remaining tokens that are not alphabetic
    transcript_stripped = [word for word in transcript_stripped if word.isalpha()]
#*************************************************************************************
    # filters out stop words ==> ntlk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    transcript_clean = [w for w in transcript_stripped if not w in stop_words]
#*************************************************************************************
    # lemmatizes the transcript; each word is converted to its normalized form
    # ==> nltk.download('wordnet'), nltk.download('averaged_perceptron_tagger')
    from nltk.tag import pos_tag
    from nltk.stem.wordnet import WordNetLemmatizer
    def lemmatize_sentence(tokens):
        lemmatizer = WordNetLemmatizer()
        lemmatized_sentence = []
        for word, tag in pos_tag(tokens):
            if tag.startswith('NN'):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
        return lemmatized_sentence
    transcript_clean = lemmatize_sentence(transcript_clean)
#*************************************************************************************
    return transcript_clean


def output_csv(transcript_clean, new_file):
    # This imports a list to a csv file
    import csv
    with open(new_file, "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for word in transcript_clean:
            wr.writerow([word])
    return 0
    
    
def main():
    
    file = "transcripts"
    txt_file = file+".txt"
    new_file = file+"_cleaned.csv"
    
    transcript_clean = trascript_cleaner(txt_file)
    
    output_csv(transcript_clean, new_file)


if __name__ == "__main__":
    main()
