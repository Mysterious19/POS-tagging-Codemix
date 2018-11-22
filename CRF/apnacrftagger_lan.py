import nltk
import io
from nltk.tag.util import untag
from sklearn_crfsuite import CRF
from sklearn_crfsuite import metrics
from xml.etree import cElementTree as ET

#tagged_sentences = nltk.corpus.treebank.tagged_sents()
root = ET.fromstring(io.open('Hi-En_data.xml',encoding='utf-8').read())
count = 0
data = []
for page in list(root):
    l = []
    text = page.find('text').text.decode('utf8')
    language = page.find('language').text.decode('utf8')
    pos = page.find('pos_tags').text.decode('utf8')
    splitText = text.split(" ")[1:-1]
    posText = language.split(" ")[1:-1]
    for i in range(len(splitText)):
        l.append((splitText[i], posText[i]))
    data.append(l)
    count = count + 1

tagged_sentences = data
# print(tagged_sentences[0])

# print("Tagged sentences: ", len(tagged_sentences))
# print("Tagged words:", len(nltk.corpus.treebank.tagged_words()))

def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }

# # Split the dataset for training and testing
cutoff = int(.75 * len(tagged_sentences))
training_sentences = tagged_sentences[:cutoff]
test_sentences = tagged_sentences[cutoff:]

def transform_to_dataset(tagged_sentences):
    X, y = [], []
 
    for tagged in tagged_sentences:
        X.append([features(untag(tagged), index) for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])
 
    return X, y
 
X_train, y_train = transform_to_dataset(training_sentences)
X_test, y_test = transform_to_dataset(test_sentences)
 
# print(len(X_train))     
# print(len(X_test))         
# print(X_train[0])
# print(y_train[0])

model = CRF()
model.fit(X_train, y_train)

sentence = ['Aaj', 'humara', 'project','evaluation','tha']
 
def pos_tag(sentence):
    sentence_features = [features(sentence, index) for index in range(len(sentence))]
    return list(zip(sentence, model.predict([sentence_features])[0]))
 
half_ans = pos_tag(sentence) 

print(half_ans)



 
# y_pred = model.predict(X_test)
# print(metrics.flat_accuracy_score(y_test, y_pred))




