def clean_transcript (txtFile, gov, lem=True, rev_format=True):
    # The two required arguments are the txt file and the name of the governor giving the speech
    # Make sure you put both arguments in quotation marks: "____"
    # The `lem` parameter indicates whether you want the words to be lemmatized
    # The `rem_format` paramater indicates if the transcript is from the Rev website
    
    # This opens the text file and stores it as a string
    transcript = open(txtFile)
    transcript_str = transcript.read()
    
#**************************************************************************

    # Specifically for transcripts from Rev.com
    # This removes all unnecesary text in between the actual speech
    if rev_format:
        gov_str = str(gov)+": "
        transcript_str = transcript_str.replace(gov_str, "")
        transcript_str = transcript_str.replace("\n", " ")
        time1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        time2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        time3 = ["0", "1", "2", "3", "4", "5", "6"]
        time4 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for a in time1:
            for b in time2:
                for c in time3:
                    for d in time4:
                        var = "("+a+b+":"+c+d+")"
                        transcript_str = transcript_str.replace(var, "")
                        
#**************************************************************************
   
    # This part tolkenizes and cleans the transcripts string
    
    # Make sure you download nltk
    import nltk
    # Also download the stop words through: nltk.download('stopwords')
    from nltk.tokenize import word_tokenize
    transcript_tokens = word_tokenize(transcript_str)
    # convert to lower case (w stands for words)
    transcript_tokens = [w.lower() for w in transcript_tokens]
    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    transcript_stripped = [w.translate(table) for w in transcript_tokens]
    # remove remaining tokens that are not alphabetic
    transcript_stripped = [word for word in transcript_stripped if word.isalpha()]
    # filter out stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    transcript_clean = [w for w in transcript_stripped if not w in stop_words]
    
#**************************************************************************
    
    # This part lemmatizes the transcript; each word is converted to its normalized form
    
    # Download wordnet, a database that helps the script detemine the base word: nltk.download('wordnet')
    # Download averaged_perceptron_tagger, a resource that determines the context of a word in a sentence: nltk.download('averaged_perceptron_tagger')
    if lem:
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
        
#**************************************************************************
    
    return transcript_clean
