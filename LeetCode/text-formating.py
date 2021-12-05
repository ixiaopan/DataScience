"""
Format a text file using the following rules:

* Only a single space between words (remove excessive spaces);
* No spaces before punctuation marks;
* One space after each punctuation mark in front of a letter;
* Use only lowercase letters, except for the beginning of the sentence (after a dot);
* Remove repeated punctuation marks.

A punctuation mark is a character other than a space, a letter or a digit.

Example
  Input: "when a father gives to his son,,, Both laugh; When a son gives to his father, , , Both cry...shakespeare"
  Output: "When a father gives to his son, both laugh; when a son gives to his father, both cry. Shakespeare"
"""
import re

def text_format(sent):
  # lowercase
  sent = sent.lower()

  # remove spaces
  sent = re.compile(r'\s+').sub(' ', sent)
  print('remove spaces:    ', sent)

  # no space before pun
  punc_pattern = re.compile(r'\s*([^\s\da-zA-Z]+)\s*')
  sent = punc_pattern.sub(lambda m: m.group().strip(), sent)
  print('no space before pun:    ', sent)

  # repeated puncs
  # one space between punc and a letter
  def rep_deal(m):
    punc, l = m.groups()
    
    if l is None:
      return punc[0]
  
    return punc[0] + ' ' + l

  sent = re.compile(r'([^\s\da-zA-Z]+)([a-zA-z\d])?').sub(rep_deal, sent)
  print('remove repeated puncs:    ', sent)


  # uppercase
  ret = '. '.join([ s[0].upper() + s[1:] for s in sent.split('. ') ])
  print('final result:    ', ret)
  return ret


text_format('helo   ...world   one, two ,,,,  three.')
text_format('when a father gives to his son,,, Both laugh; When a son gives to his father, , , Both cry...shakespeare')