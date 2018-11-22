import io
from nltk.tag import CRFTagger
from xml.etree import cElementTree as ET
from random import shuffle
from nltk.metrics.scores import precision,recall,f_measure,accuracy
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
    posText = language.split(" ")[1:-1]
    for i in range(len(splitText)):
        l.append((splitText[i], posText[i]))
    data.append(l)
    count = count + 1
shuffle(data)
# print len(data)


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

# Divide data into train and test sets
eightyPercent = count*0.9
training_set = data[0:int(eightyPercent)]
test_set = data[int(eightyPercent):]
# print training_set

# Train
ct = CRFTagger()
train_data = training_set
train_data_new = []
for i in range(len(train_data)):
    if len(train_data[i]) != 0 :
        train_data_new.append(train_data[i])
ct.train(train_data_new, 'model.crf.tagger')

# Accuracy
test_data_new = []
test_data_tags = []
for i in range(len(test_set)):
    if len(test_set[i]) != 0 :
        for j in range(len(test_set[i])):
            test_data_new.append(test_set[i][j][0])
            test_data_tags.append(test_set[i][j][1])
gold_sentences = test_data_new
# print ct.evaluate(gold_sentences)

# print test_data_new
pred_tags = []
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

pred = ct.tag(gold_sentences)
for i in range(len(pred)):
    pred_tags.append(pred[i][1])

for i in range(len(test_data_tags)):
    refsets[test_data_tags[i]].add(i)
    testsets[pred_tags[i]].add(i)

print "CRF language model"
print 'Accuracy:', accuracy(pred_tags,test_data_tags)
print "\n"
print 'Precision of en:',precision(refsets['en'], testsets['en'])
print 'Precision of hi:',precision(refsets['hi'], testsets['hi'])
print "\n"
print 'Recall of en:', recall(refsets['en'], testsets['en'])
print 'Recall of hi:', recall(refsets['hi'], testsets['hi'])
print "\n"
print 'f_measure of en:', f_measure(refsets['en'], testsets['en'])
print 'f_measure of hi:', f_measure(refsets['hi'], testsets['hi'])
print "\n"
