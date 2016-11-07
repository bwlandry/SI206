# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk import word_tokenize,sent_tokenize



#print (nltk.corpus.gutenberg.fileids())   
moby_dick = nltk.corpus.gutenberg.words("melville-moby_dick.txt")   #assign text to variable moby_dick
#print (moby_dick)

#print (moby_dick)
# tokens = nltk.word_tokenize(moby_dick))


tagged = nltk.pos_tag(moby_dick)[0:150]    #tagging each word with a part of speech. Results in tuples (word, POS)
#print (tagged)



tagmap = {"NN":"a noun","PRON":"a pronoun","VB":"a verb","JJ":"an adjective", "ADP": "an adposition (preposition)"}
substitution_probabilities = {"NN":.15,"PRON":.1,"VB":.1,"JJ":.1, "ADP": .1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

original_text = []
for (word, tag) in tagged:
	original_text.append(spaced(word))

final_words = []


for (word, tag) in tagged:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


print ("".join(original_text))
print("\n")
print("\n")
print("\n")
print ("".join(final_words))
print("\n\nEND*******")
