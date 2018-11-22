# POS-tagging-Codemix

A NLP based project that tags the user given code-mixed sentence into hindi and english and also does the part of speech tagging for the same.
# Setting up the Project

  - Cloning the project Just run the following command on your terminal or CLI. git clone https://github.com/Mysterious19/POS-tagging-Codemix.git
  - To install the required libraries and dependencies run the command in your terminal 'pip install -r requirements.txt'
  - To test the sentence with CRF model run the command on terminal 'python2 crf.py'
  - To test the sentence with Hmm model run the command on terminal 'python2 hmm.py'


The folder also has attached screenshots of precision, recall and accuracy of every model and each individual tags.

# Dependencies

- dill==0.2.8.2
- lxml==4.1.0
- nltk==3.2.4
- numpy==1.13.3
- numpydoc==0.7.0
- pandas==0.20.3
- pytest==3.2.1
- python-crfsuite==0.9.6
- python-dateutil==2.6.1
- scikit-learn==0.20.0
- scipy==0.19.1
- sklearn==0.0
- sklearn-crfsuite==0.3.6

# Graphs
 
![CRF](https://github.com/Mysterious19/POS-tagging-Codemix/blob/master/Graphs/POS%20CRF.jpg)

![Hmm](https://github.com/Mysterious19/POS-tagging-Codemix/blob/master/Graphs/POS%20HMM.jpg)

![precision](https://github.com/Mysterious19/POS-tagging-Codemix/blob/master/Graphs/Precison%20Language.jpg)

![recall](https://github.com/Mysterious19/POS-tagging-Codemix/blob/master/Graphs/Recall%20Language.jpg)

![f_measure](https://github.com/Mysterious19/POS-tagging-Codemix/blob/master/Graphs/F_Measure%20Language.jpg)

# Reference Papers

1) Anupam Jamatia, Björn Gambäck, Amitava Das, Part-of-Speech Tagging for
Code-Mixed English-Hindi Twitter and Facebook Chat Messages.
2) Yogarshi Vyas, Jatin Sharma,Kalika Bali, POS Tagging of English-Hindi Code-Mixed
Social Media Content
3) Utsab Barman, Amitava Das,Joachim Wagner, Jennifer Foster, Code Mixing: A
Challenge for Language Identification in the Language of Social Media
4) Ben King, Steven Abney, Labeling the Languages of Words in Mixed-Language
Documents using Weakly Supervised Methods
5) Souvick Ghosh, Satanu Ghosh, Dipankar Das, “Part-of-speech Tagging of
Code-Mixed Social Media Text
6) Kovida Nelakuditi, Radhika Mamidi, Part-of-Speech Tagging for Code mixed
English-Telugu Social media data

For any further queries contact
- Pulkit Jaroli(8369545335) iit2016081@iiita.ac.in
- Harshit Agarwal(73887576875) iit2016108@iiita.ac.in
- Sominee Gupta(7983129771) ihm2016007@iiita.ac.in
- Nistala Venkata Kameshwar Sharma(8839002133) ism2016005@iiita.ac.in
- Saksham Singh(9161896720) iit2016090@iiita.ac.in
