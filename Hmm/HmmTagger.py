import io
from nltk.tag import hmm
from xml.etree import cElementTree as ET
from random import shuffle
import HmmTagger_lan
import dill
from nltk.metrics.scores import precision,recall,f_measure, accuracy
import collections

root = ET.fromstring(io.open('Hi-En_data.xml',encoding='utf-8').read())
count = 0
data = []
for page in list(root):
    l = []
    text = page.find('text').text.decode('utf8')
    language = page.find('language').text.decode('utf8')
    pos = page.find('pos_tags').text.decode('utf8')
    splitText = text.split(" ")[1:-1]
    posText = pos.split(" ")[1:-1]
    for i in range(len(splitText)):
        l.append((splitText[i], posText[i]))
    data.append(l)
    count = count + 1
shuffle(data)
train_data_new = []
for i in range(len(data)):
    if len(data[i]) != 0:
        train_data_new.append(data[i])
data = train_data_new
# print len(data)        



def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }
def features1(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }
# Divide data into train and test sets
eightyPercent = count*0.9
training_set = data[0:int(eightyPercent)]
test_set = data[int(eightyPercent):]

# print len(training_set)
# print len(test_set)

# Train
trainer = hmm.HiddenMarkovModelTrainer()
train_data = training_set

tagger = trainer.train_supervised(training_set)


with open('my_tagger.dill', 'wb') as f:
    dill.dump(tagger, f)




test_data_new = []
test_data_tags = []
for i in range(len(test_set)):
    if len(test_set[i]) != 0 :
        for j in range(len(test_set[i])):
            test_data_new.append(test_set[i][j][0])
            test_data_tags.append(test_set[i][j][1])
gold_sentences = test_data_new

# print ct.evaluate(gold_sentences)

pred_tags = []
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

pred = tagger.tag(gold_sentences)
for i in range(len(pred)):
    pred_tags.append(pred[i][1])

for i in range(len(test_data_tags)):
    refsets[test_data_tags[i]].add(i)
    testsets[pred_tags[i]].add(i)

print "Hmm POS model"
print 'Accuracy:', accuracy(pred_tags,test_data_tags)
print "\n"
print 'Precision of G_N:',precision(refsets['G_N'], testsets['G_N'])
print 'Precision of G_V:',precision(refsets['G_V'], testsets['G_V'])
print 'Precision of CC:',precision(refsets['CC'], testsets['CC'])
print 'Precision of PSP:',precision(refsets['PSP'], testsets['PSP'])
print 'Precision of G_PRP:',precision(refsets['G_PRP'], testsets['G_PRP'])
print 'Precision of G_PRT:',precision(refsets['G_PRT'], testsets['G_PRT'])
print 'Precision of DT:',precision(refsets['DT'], testsets['DT'])
print 'Precision of G_J:',precision(refsets['G_J'], testsets['G_J'])
print "\n"
 
print 'Recall of G_N:',recall(refsets['G_N'], testsets['G_N'])
print 'Recall of G_V:',recall(refsets['G_V'], testsets['G_V'])
print 'Recall of CC:',recall(refsets['CC'], testsets['CC'])
print 'Recall of PSP:',recall(refsets['PSP'], testsets['PSP'])
print 'Recall of G_PRP:',recall(refsets['G_PRP'], testsets['G_PRP'])
print 'Recall of G_PRT:',recall(refsets['G_PRT'], testsets['G_PRT'])
print 'Recall of DT:',recall(refsets['DT'], testsets['DT'])
print 'Recall of G_J:',recall(refsets['G_J'], testsets['G_J'])
print "\n"

print 'f_measure of G_N:',f_measure(refsets['G_N'], testsets['G_N'])
print 'f_measure of G_V:',f_measure(refsets['G_V'], testsets['G_V'])
print 'f_measure of CC:',f_measure(refsets['CC'], testsets['CC'])
print 'f_measure of PSP:',f_measure(refsets['PSP'], testsets['PSP'])
print 'f_measure of G_PRP:',f_measure(refsets['G_PRP'], testsets['G_PRP'])
print 'f_measure of G_PRT:',f_measure(refsets['G_PRT'], testsets['G_PRT'])
print 'f_measure of DT:',f_measure(refsets['DT'], testsets['DT'])
print 'f_measure of G_J:',f_measure(refsets['G_J'], testsets['G_J'])
print "\n"