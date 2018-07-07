import os 

def load_data(path):
    fp = os.path.join(path)
    with open(fp, 'r') as f:
        data = f.read()
        
        return data

def punctuation_lookup():
    
    """
    Generate a dict to turn punctuation into a token.
    :return: Tokenize dictionary where the key is the punctuation and the value is the token
    """
    punctuation = {'.':'||Period||',
                  ',':'||Comma||',
                  '"':'||QuotationMark||',
                  '!':'||ExclamationMark||',
                  ';':'||Semicolon||',
                  '?':'||QuestionMark||',
                  '(':'||LeftParentheses||',
                  ')':'||RightParentheses||',
                  '--':'||Dash||',
                  '\n':'||Return||'}   
    return punctuation

def create_lookup_table(vocabulary):
    
    int2vocab = {idx:vocab for idx,vocab in enumerate(vocabulary)}
    vocab2int = {vocab:idx for idx, vocab in int2vocab.items()}
    return int2vocab, vocab2int
    

    
def preprocess_data(text):
    
    '''
    ARGUMENT 
    text : text data to be tokenized 
    
    <return> tokenized data, int2vocab, vocab2int 
    '''
    text = text.lower()
    punctuation = punctuation_lookup()
    for key, item in punctuation.items():
        text = text.replace(key, ' {} '.format(item)) # tokenize punctuation and add space between them 
                      
    data = text.split() #split data into list of words
    vocabulary = sorted(set(data))
    int2vocab, vocab2int = create_lookup_table(vocabulary)
    int_data = [vocab2int[word] for word in data] # turns words into numbers 
    
    return int_data, int2vocab, vocab2int 
    
