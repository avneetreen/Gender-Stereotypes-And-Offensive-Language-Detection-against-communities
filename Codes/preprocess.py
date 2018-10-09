"""
 @Avneet Kaur

 Prepocess tweets - remove extra spaces, new lines, and stopwrods, also removes @user tags, hash tags and hyperlinks to other pages

"""
import csv 
import re
import nltk
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
def readFile(filename):
    content = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            content.append([row[0],row[1],row[2],row[3]])
    newContent = []
    for x in content:  
        cleanTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x[2]).split())  
        tokens = nltk.word_tokenize(cleanTweet)
        cleanTokens = [word for word in tokens if word not in stop_words]  
        finalTweet = ' '.join(cleanTokens)    
        newContent.append([x[0],x[1],finalTweet,x[3]])
    #print newContent
    return newContent

def writeTofile(newContent,filename):
    with open(filename, 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for x in newContent:
            print(x)
            wr.writerow([newContent[0]] + [newContent[1]] + [newContent[2]] + [newContent[3]])

if __name__ == "__main__":
    filename1=""
    filename2=""
    newContent = readFile(filename1)
    writeTofile(newContent,filename2)
