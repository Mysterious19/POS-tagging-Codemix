import dill



with open('hmm_taggerlan.dill', 'rb') as f:
    hmm_tagger_lan = dill.load(f)


with open('my_tagger.dill', 'rb') as f:
    hmm_tagger = dill.load(f)



print "Give a sentence..."
# Test
test_sent = raw_input()
test_sent = test_sent.encode('utf-8').decode('utf-8').split(' ')
# print test_sent
# half_ans = tagger.tag('OUT nahi KARDO ISSE BAHUT HOGAYA aaj Salman'.encode('utf-8').decode('utf-8').split())
print hmm_tagger_lan.tag(test_sent)

print hmm_tagger.tag(test_sent)