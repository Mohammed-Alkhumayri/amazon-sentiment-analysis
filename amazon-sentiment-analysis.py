import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

#task1: Write a Python function called sentimentAnalyzer(text). This function takes a text (i.e review) and returns the sentiment 

def sentimentAnalyzer(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:
        return 'Negative'
    elif -0.2 <= polarity <= 0.2:
        return 'Neutral'
    else:
        return 'Positive'



texts = ["This product is bad", "This product is good", "This product is neither good nor bad."]
print("---------------------Task 1--------------------------------")
sentiments = [sentimentAnalyzer(text) for text in texts]
print(sentiments)


#task2: Verify that the function does classify the sentiment correctly by passing the  words from the table

print("-----------------Task 2--------------------------")
test_texts = [
    "happy",     #Positive
    "exciting",   #Positive
    "good",     #Positive
    "rich",      #Positive
    "smile",      #Positive
    "sad",    #Negative
    "disappointed",  #Negative
    "bad",     #Negative
    "poor",    #Negative
    "anger", #Negative
    "food",  #Neutral
    "animel"   #Neutral
]


test_results = {text: sentimentAnalyzer(text) for text in test_texts}
print(test_results)



# Task 3:  Import the provided dataset into a Pandas DataFrame
file_path = "data.xlsx"
df = pd.read_excel(file_path)

df_final = df.drop(columns=['Unnamed: 5'])
df_final.columns = ['Product Name', 'Brand', 'Price', 'Rating', 'Review']


# Task 4: Apply the function sentimentAnalyzer(text)to the text column in your dataframe.
# This should create a new column in the dataframe called (Sentiment) which includes the sentiment for each review. 

df_final['Sentiment'] = df_final['Review'].apply(sentimentAnalyzer)
output_file_path = "data1.xlsx"  
df_final.to_excel(output_file_path, index=False)




# Task 5: Visualization

# 1 Sentiment Distribution
sentiment_counts = df_final['Sentiment'].value_counts()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.title('Sentiment Distribution')
plt.ylabel('Number of Reviews')
plt.xlabel('Sentiment')
plt.show()

# 2 customers rating based on thier sentiment
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.countplot(x='Rating', data=df_final, hue='Sentiment', palette='viridis', saturation=0.75)
ax.set_title('Count of Ratings by Sentiment Category', fontsize=16)
ax.set_xlabel('Ratings', fontsize=14)
ax.set_ylabel('Number of Reviews', fontsize=14)
plt.legend(title='Sentiment', title_fontsize='13', fontsize='12', loc='upper left')
plt.show()


# 3 Average of sentiments
sentiment_percentages = df_final['Sentiment'].value_counts(normalize=True) * 100
average_ratings = df_final.groupby('Sentiment')['Rating'].mean()
print(f"\nAverage Ratings by Sentiment:\n", average_ratings)


# 4 examples of reviwes thats have rating that opposet of the sentiment 
positive_sentiment_low_rating = df_final[(df_final['Sentiment'] == 'Positive') & (df_final['Rating'] < 3)]
negative_sentiment_high_rating = df_final[(df_final['Sentiment'] == 'Negative') & (df_final['Rating'] > 3)]

mismatched_positive = positive_sentiment_low_rating[['Review', 'Rating', 'Sentiment']].head(5)
mismatched_negative = negative_sentiment_high_rating[['Review', 'Rating', 'Sentiment']].head(5)


print("Reviews with Positive Sentiment but Low Ratings:")
print(mismatched_positive)
print("\nReviews with Negative Sentiment but High Ratings:")
print(mismatched_negative)

# Task 6: Save the DataFrame to a CSV file
output_file_path = "data2.csv" 
df_final.to_csv(output_file_path, index=False)