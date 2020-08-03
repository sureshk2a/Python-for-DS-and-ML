import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
#nltk.download_shell()
messages = pd.read_csv("..//..//Files//SMSSpamCollection",sep="\t",names=["label","message"])
#messages = [line.strip() for line in open("..//..//Files//SMSSpamCollection")]
#print(messages[0])
# for message_no,message in enumerate(messages[:10]):
#     print(message_no,message)
#     print("\n")
messages["length"] = messages["message"].apply(len)
#print(messages.head())
#messages["length"].plot.hist(bins=150)
#print(messages[messages["length"] == 910]["message"].iloc[0])
# mess = "Sample message! Notice: it has punctuation."
# npunc = [c for c in mess if c not in string.punctuation]
# nopunc = "".join(npunc)
# clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words("english")]
# print(clean_mess)
def text_process(mess):
    #remove punc,join,remove stopwords,return
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = "".join(nopunc)
    return [c for c in nopunc.split() if c.lower() not in stopwords.words("english")]
processed = messages["message"].apply(text_process)
print(processed)
bow_transformer = CountVectorizer(analyzer=text_process).fit(messages["message"])
#print(len(bow_transformer.vocabulary_))
mess4 = messages["message"][3]
print(mess4)
bow4 = bow_transformer.transform([mess4])
print(bow4)
print(bow_transformer.get_feature_names()[9554])
plt.show()