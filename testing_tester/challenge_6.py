def longest(sentence):
  new_sentence=max(sentence.split(),key=len)
  return new_sentence
  
  
 
longest('home is best')