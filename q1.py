import sys
import re

#initializing lists for words, sentences and phrases
word_dict = {}
phrase_dict = {}
sentence_list = []
words_used_with_count = []
phrases_list = []
phrases_used_with_count =[]
most_common_phrases = []

#accepting input from command line
if len(sys.argv) > 1:
	f = open(sys.argv[1], 'r')
	data = f.read()
else:
	print "STDIN: Input text ---> use Ctrl-D to run program"
	f = sys.stdin.read()
	data = f
data = str(data).lower()


#splitting up the text by space for words and periods for sentences
word_list = data.split(" ") 
word_count = len(word_list)
unique_word_list = set(word_list)
unique_word_count = len(unique_word_list)
sentence_periods = data.split('.')

#Finding further sentences in the case of sentences ending in exclamation or question marks
for sent in sentence_periods:

	if '!' in sent:
		exclamation = sent.split('!')
		for sentence in exclamation:
			sentence_list.append(sentence)

	elif '?' in sent:
		question = sent.split('?')
		for sentence in question:
			sentence_list.append(sentence)		
	else:
		sentence_list.append(sent)
#getting rid of any blank strings in sentence_list		
sentence_list = filter(None, sentence_list)
#print sentence_list
sentence_count = len(sentence_list)
sentence_length = float(word_count)/sentence_count

#Creating a dictionary to keep track of words and the count for each word
for word in word_list:
	if word in word_dict:
		word_dict[word] += 1
	else:
		word_dict[word] = 1
#Creating a list of phrases from the word list
for i in range(len(word_list)-2):
	phrases_list.append(word_list[i] + " " + word_list[i+1] + " " + word_list[i+2])

#Creating a dictionary to keep track of 3 word phrases and the count for each phrase
for phrase in phrases_list:
	if phrase in phrase_dict:
		phrase_dict[phrase] += 1
	else:
		phrase_dict[phrase] = 1

#Sorting both dictionaries by the count, starting with highest count (descending order)
phrase_used = sorted(phrase_dict, key=phrase_dict.__getitem__, reverse=True)
words_used = sorted(word_dict, key=word_dict.__getitem__, reverse=True)

#Filling up word and phrase count list using the dictionaries created above
for word in words_used:
	words_used_with_count.append((word, word_dict[word]))

for phrase in phrase_used:
	phrases_used_with_count.append((phrase, phrase_dict[phrase]))

#finding the most common 3 word phrases
for phrases in phrases_used_with_count:
	if phrases[1] > 3:
		most_common_phrases.append(phrases[0])

#printing the output
print "Total word count: %d \nUnique words: %d \nSentences: %d \nAverage sentence length: %f"  % (word_count, unique_word_count, sentence_count, sentence_length)
print "Words Used (Descending Frequency):%s \n" % (words_used_with_count)
#print "Phrases Used (Descending Frequency):%s \n" % (phrases_used_with_count)
print "Most common phrases: %s \n" % (most_common_phrases)
