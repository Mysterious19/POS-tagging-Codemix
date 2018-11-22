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
hiData = []
enData = []
uniData = []
for page in list(root):
    l = []
    text = page.find('text').text.decode('utf8')
    language = page.find('language').text.decode('utf8')
    pos = page.find('pos_tags').text.decode('utf8')
    splitText = text.split(" ")[1:-1]
    lanText = language.split(" ")[1:-1]
    posText = pos.split(" ")[1:-1]
    for i in range(len(splitText)):
        l.append((splitText[i],lanText[i],posText[i]))
    data.append(l)
    count = count + 1


for li in data:
    en = []
    hi = []
    uni = []
    for i in range(len(li)):
        if str(li[i][1]) == "en":
            en.append(li[i])
        elif str(li[i][1]) == "hi":
            hi.append(li[i])
        else:
            uni.append(li[i])

    enData.append(en)
    hiData.append(hi)
    uniData.append(uni)        

if len(en) != 0:        
    enData.append(en)
if len(hi) != 0:    
    hiData.append(hi)
if len(uni) != 0:    
    uniData.append(uni) 


# tagged_sentences = data
tagged_sentences_En = enData
tagged_sentences_Hn = hiData
tagged_sentences_Un = uniData

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
cutoff = int(.75 * len(tagged_sentences_En))
training_sentences_En = tagged_sentences_En[:cutoff]
test_sentences_En = tagged_sentences_En[cutoff:]

cutoff = int(.75 * len(tagged_sentences_Hn))
training_sentences_Hn = tagged_sentences_Hn[:cutoff]
test_sentences_Hn = tagged_sentences_Hn[cutoff:]

cutoff = int(.75 * len(tagged_sentences_Un))
training_sentences_Un = tagged_sentences_Un[:cutoff]
test_sentences_Un = tagged_sentences_Un[cutoff:]

def transform_to_dataset(tagged_sentences):
    X, y = [], []
    # new_tagged_sentences = []
    for tagged in tagged_sentences:
        new_tagged=[]
        for i in range(len(tagged)):
            new_tagged.append((tagged[i][0],tagged[i][2]))
        tagged=new_tagged
        for idx  in range(len(tagged)):
            cX,cy =[], []
            cX.append(features(untag(tagged),idx))
            cy.append(tagged[idx][1])
            X.append(cX)
            y.append(cy) 
    return X, y
 
X_train_En, y_train_En = transform_to_dataset(training_sentences_En)
X_test_En, y_test_En = transform_to_dataset(test_sentences_En)
 
X_train_Hn, y_train_Hn = transform_to_dataset(training_sentences_Hn)
X_test_Hn, y_test_Hn = transform_to_dataset(test_sentences_Hn)

X_train_Un, y_train_Un = transform_to_dataset(training_sentences_Un)
X_test_Un, y_test_Un = transform_to_dataset(test_sentences_Un)



# print(len(X_train))     
# print(len(X_test))         
# print(X_train[0])
# print(y_train[0])

model_En = CRF()
model_En.fit(X_train_En, y_train_En)

model_Hn = CRF()
model_Hn.fit(X_train_Hn,y_train_Hn)

model_Un = CRF()
model_Un.fit(X_train_Un,y_train_Un)

sentence = [('Aaj', 'hi'), ('humara', 'hi'), ('project', 'en'), ('evaluation', 'en'), ('tha', 'hi')]

def pos_tag(sentence):
    sentence_features_En=[]
    sentence_features_Hn = []
    sentence_features_Un = []
    for word in range(len(sentence)):
        if sentence[word][1]=="en":
            sentence_features_En.append(features(untag(sentence),word))
        elif sentence[word][1]=="hi":
            sentence_features_Hn.append(features(untag(sentence),word))
        else:
            sentence_features_Un.append(features(untag(sentence),word))

    # print sentence_features_En
    # print sentence_features_Hn
    # print sentence_features_Un   




    finallist=[]
    finallist_En = []   
    finallist_Hn = []
    finallist_Un = []
    finallist_En.append(model_En.predict([sentence_features_En])[0])
    finallist_Hn.append(model_Hn.predict([sentence_features_Hn])[0])
    finallist_Un.append(model_Un.predict([sentence_features_Un])[0])
    # print finallist_Un
    # print finallist_En
    # print finallist_Hn
    print len(finallist_En)
    for tagged in sentence:
        print tagged
        
        if tagged[1]=='en':
            finallist.append((tagged[0],finallist_En[0].pop(0)))
        elif tagged[1]=='hi':
            finallist.append((tagged[0],finallist_Hn[0].pop(0)))
        else:
            finallist.append((tagged[0],finallist_Un[0].pop(0)))

    # finallist.append(list(zip(sentence, model_En.predict([sentence_features_En])[0])))
    # finallist.append(list(zip(sentence, model_Hn.predict([sentence_features_Hn])[0])))
    # finallist.append(list(zip(sentence, model_Un.predict([sentence_features_Un])[0])))
    return finallist
 
print pos_tag(sentence)


 
y_pred_En = model_En.predict(X_test_En)
print(metrics.flat_accuracy_score(y_test_En, y_pred_En))


y_pred_Hn = model_Hn.predict(X_test_Hn)
print(metrics.flat_accuracy_score(y_test_Hn, y_pred_Hn))


y_pred_Un = model_Un.predict(X_test_Un)
print(metrics.flat_accuracy_score(y_test_Un, y_pred_Un))