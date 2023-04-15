# pip install -U sentence-transformers


def compute_embeddings_bert():
  from sentence_transformers import SentenceTransformer
  # See https://github.com/UKPLab/sentence-transformers
  model = SentenceTransformer('all-MiniLM-L6-v2')


  sentences = ['This framework generates embeddings for each input sentence',
      'Sentences are passed as a list of string.', 
      'The quick brown fox jumps over the lazy dog.']
  sentence_embeddings = model.encode(sentences)


  for sentence, embedding in zip(sentences, sentence_embeddings):
      print("Sentence:", sentence)
      print("Embedding:", embedding)
      print("")
      
def compute_embeddings_word2vec():
  from gensim.models import Word2Vec
  import gensim.downloader as api
  wv = api.load('word2vec-google-news-300')
  computer_wv = wv['computer']
  # wv only works over one word at a time. 
  # so you need to loop over all words in a sentence
  # and then take the average. 
    
    
