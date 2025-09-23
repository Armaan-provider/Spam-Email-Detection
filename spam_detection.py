import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('spam_data.csv')

df['Category'] = df['Category'].replace(['spam', 'ham'],['Spam', 'Not Spam'])

mess = df['Message']
cat = df['Category']

# Splitting the data into train set and test set
(m_train, m_test, c_train, c_test) = train_test_split(mess, cat, test_size=0.2)

# Using countVectorizer to convert the alphabetical data to numerical data
count_vec = CountVectorizer()

message = count_vec.fit_transform(m_train)

# Now let's train the MultinomialNB model on our data
model = MultinomialNB()
model.fit(message, c_train)

# Let's test the model now

message_test = count_vec.transform(m_test)
score = model.score(message_test, c_test)

# Let's make a final funciton that will take message(input) from the user and tell whether it is spam or not

def predict(input_message):
    message = count_vec.transform([input_message]).toarray()
    Result = model.predict(message)
    return Result