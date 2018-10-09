### Related Work
The problem of identifying gender stereotypes and abusive language against specific communities on online social media is closely 
related detection of abusive language against specific communities based on gender, race, ethnicity, caste, creed, colour, on online 
social media. Recent work has also been done on hate speech detection on online social media.  Hate speech has been defined as an 
“abusive speech targeting specific group characteristics, such as ethnicity, religion, or gender”. Various websites list words 
related to hate, aggression, bullying, LGBTQ slang terms, abusive words etc, which have been widely employed by researchers as tags 
to get data from social media platforms. Other work that is related to our problem is Aggression and Bullying detection on social 
media platforms.

Aggression detection in social media is more like a document classification task which can be either binary class or multi class 
classification. Binary class classification in this case would mean, whether a particular social media phenomena such as whether 
the content of the post is racist or not. It would deal with these classes one at a time whereas in  case of multi-class classification, several anti-social phenomenon are dealt with, all at once, example racism, sexism, hate speech, and bullying. 
For the gender stereotypes aspect, its detection has been explored in various instances such as occupation related data, 
social media platforms, plot and role in movies and books for various types of gender.  

Here, several approaches towards hate speech detection, aggression and bullying against communities have been explored.
**Nemanja Djuric et al. [1]**  put forward a two-step approach for hate speech detection. Firstly, distributed representations of 
words which are specific to hate are learned using continuous BOW model which gives a low dimensional embedding, segregating 
semantically similar comments from non similar ones. Then,these embeddings are further used to train a binary classifier to 
distinguish between hateful and clean comments.

Researchers have previously used bag of words features for hate speech detection.  
In **[2]** BOW representation of user comments have been extracted and Support Vector Machines have been used to detect hate speech. 
In **[3]**, a Naive Bayes classifier has been used to classify racist comments against a particular community, after 
learning the BOW features.

**Segun Taofeek Aroyehun et al. [4]** have addressed the challenge of automatically identifying aggression in social media posts. 
The idea was to develop a baseline model and other neural network models. A  logistic regression classifier for hate speech 
detection was used  and was considered to be a strong baseline.  Two variants, one based on word n-grams and the other based on 
character n-grams were implemented. These were then compared to the neural network models hence developed.
For the deep learning models, the input representations was the embedding layer which encodes the words in the vocabulary. For this 
purpose, pre-trained word vectors such as wordToVec, Glove embeddings, fast Text were used. Experiments were performed with 
several Deep Neural Network Models such as: CNN, LSTM, BiLSTM, CNN-LSTM, LSTM-CNN, CNN-BiLSTM, and BiLSTM-CNN.

Another approach towards this problem is by **Despoina Chatzakou et al. [5]** They focus more on categorizing and determining features 
of people who post aggressive and hate speech against communities, ethnicity, gender etc. They aim at studying the characteristics of 
such people, and how to distinguish them from regular users. This could be a possible extension of the problem. 

**Amir H. Razavi et al**, in their work ‘Offensive Language Detection Using Multi-level Classification’ **[6]** have made a significant 
contribution by compiling an Insulting and Abusive Language Dictionary consisting of words that are in any form abusive and insulting. 
They have gone a step further and categorized the offensive languages into taunts, references to handicaps, ethnic slurs,
squalid language, racism, extremism, sexism and many other such categories. Further they adapted a three level classification 
for offensive language detection. Firstly, a Naive Bayes classifier was used for selecting the most prominent features. 
Next, a multinomial updatable naive bayes classifier was used, which was run on the best feature space extracted from the 
previous classifier. The new aggregated feature space extracted is then used in the third level of classification which is a 
Decision Tree Hybrid classifier, which makes the final binary class classification classifying the tweet as okay, or hate inducing.
Like the Insulting and Abusive Language dictionary, there are many other lists such as List of Slangs used against the LGBTQ community, 
List of abusive words(https://www.noswearing.com/dictionary), list of hurtful words (https://lgbtqia.ucdavis.edu/educated/words), 
and negative connotations against handicapped people that are widely provided by wikipedia. These resources can be utilised as 
a base to find posts on online social media that contain these and can help us identify offensive language being used against 
particular communities. 

Another interesting work related to our problem has been done on Peer-to-Peer Insult Detection in Online Communities **[7]** 
which treats the problem as a binary classification problem and employs several supervised learning algorithms like Support Vector
Machines, Logistic Regression etc. Feature extraction here is done by extracting tokens, using a TF-IDF score, using skip grams.
A chi-square test is performed to test  if a pair of categorical variables on a data is statistically dependent or independent. 
In this case, this pair of variable is: The label of the sentence: “insult or not” and the occurrence or nonoccurrence of a feature”. 
High Scoring features in this test are important features to be considered. For example if the feature “you idiot” and the label 
“insult” are statistically dependent, then this means it is an important feature. After the feature extraction, classification was 
done using SVM and Logistic Regression and the accuracy was evaluated.

Some work related to our problem has also been done on predicting features for hate speech detection like in **[8]** . This work presents a criteria and a category list to identify racist and sexist comments, remarks and slurs. Various features like unigrams, bigrams, trigrams, and fourgrams for each tweet and the user description are collected for this purpose.
Grid search is used to perform feature selection in their model. The results indicate that character n-grams turn out to be significant contributors.
Finally  a deep learning based approach using has been explored in the paper “Detecting Offensive Language in Tweets Using Deep Learning” **[9]**. The problem that the researchers are trying to solve here is to effectively identify the class of a user post on social media - categorizing it into - Racist or Sexist or neither, based on the identity of the user, and the history of postings related to this user. It employs a neural network solution composed of multiple Long-Short2 Term-Memory (LSTM) based classifiers, and appart from n-gram features in tweets, also utilizes the features of user’s behaviour that is the user’s tendency towards tweeting on Racism and Sexism using offensive language.

An interesting way in our problem could be extended is like the above, in classifying a post as consisting of offensive language against a community  according to the characteristics of the posting user and user behaviour on online social media platforms. Another interesting approach would be to identify specific areas where there is gender based stereotypes, and then detect offensive language use against a specific community in those specific areas, which would be a significant step, to attributing, and targeting specific areas of life, where there is use of offensive language, and stereotypes on the basis of gender.

[1] Hate Speech Detection with Comment Embeddings http://www.www2015.it/documents/proceedings/companion/p29.pdf

[2] W. Warner and J. Hirschberg. Detecting hate speech on the World Wide Web. In Workshop on Language in Social Media at ACL

[3]  I. Kwok and Y. Wang. Locate the hate: Detecting tweets against blacks. In AAAI, 2013

[4] Aggression Detection in Social Media: Using Deep Neural Networks, Data Augmentation, and Pseudo Labeling http://aclweb.org/anthology/W18-4411

[5] Mean Birds: Detecting Aggression and Bullying on Twitter https://arxiv.org/pdf/1702.06877.pdf

[6] Offensive Language Detection Using Multi-level Classification http://www.eiti.uottawa.ca/~diana/publications/Flame_Final.pdf

[7] Peer-to-Peer Insult Detection in Online Communities https://cse.iitk.ac.in/users/cs365/2013/submissions/~prigoyal/cs365/project/report.pdf

[8] Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter http://www.aclweb.org/anthology/N16-2013

[9] Detecting Offensive Language in Tweets Using Deep Learning https://www.researchgate.net/publication/322517785  
