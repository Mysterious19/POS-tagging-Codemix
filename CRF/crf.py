from nltk.tag import CRFTagger

crflan = CRFTagger()
crf = CRFTagger()

crflan.set_model_file('model.crf.tagger')
crf.set_model_file('model1.crf.tagger')

print "Give a sentence..."
# Test
test_sent = raw_input()
test_sent = test_sent.encode('utf-8').decode('utf-8').split(' ')
print test_sent
half_ans= crflan.tag(test_sent)
print half_ans

# print test_sent
print crf.tag(test_sent)