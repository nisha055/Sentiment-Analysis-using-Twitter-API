# Sentiment-Analysis-using-Twitter-API

Sentiment Analysis using Twitter API (tweepy)

- Aim is to extract the features of tweets and classify them into positive or negative sentiment.
- The dataset is collected from twitter and is splitted into two sets, 
    - N_train = Training Set
    - N_test = Test Set
- And further fitted into the Classifier for training and testing purpose
    - Classifier = Classification_Model(N_train , N_test)


- Data is collected using Tweepy (python library ) from twitter.
- While accessing the user timeline , the user with privacy setting were skipped and next users data was taken
- The data collected in the result set then dumped  into a JSON file.
- For further processing, the text attribute is taken from the JSON file and stored into a TSV file with one column as the tweet and then next as mood with 
    - 0 - negative mood 
    - 1 -  positive mood


- Using Spyder IDE for python, steps taken for data cleaning are :
    - Remove all the extra spaces , symbols , numbers  etc. 
    - Next we use NLTK corpus to remove stopwords words such as “is”, “the”, etc.
    - Then we use NLTK PorterStemmer to perform stemming  i.e removing different variations of words with the same meaning such as "loved", "love", etc


- For this part we have used the bag of words Model , it constructs a word presence feature set from all the words of an instance. The steps involved in this are :
    - Collect Data 
    - Design Vocabulary : list of all the words
    - Create Document Vectors : with values as 1 (present) and 0 (absent)


- To predict the mood, different classification models used in this project are :  
    - Naive Bayes
    - Decision Tree
    - Random Forest
    - Support-Vector Machines(SVM)
