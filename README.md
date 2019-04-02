"# MSL-Tokenizer" 

A monosyllabic language is a language in which words predominantly consist of a single syllable. Vietnamese, Chinese and other languages of Southeast Asia are referred to as monosyllabic languages. 
In these languages, it's difficult to define the term "word", the white space between single syllable do not indicate word boundaries. In Vietnamese or Chinese, 85% of words spread over multiple syllables with spaces. The way of tokenizing the "word" will give different meaning of the sentence.
Because the spaces cannot be used to separate the words so this is big issue of monosyllabic language tokenization.

This repository contains a python program which allow the following:
- Tokenize the sentence into multi-syllables
- Build machine learning model for tokenizing the sentence
- Create feature of model with label and syllables by word dictionary, name dictionary and location name dictionary
- Train and fit the model
