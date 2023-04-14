import pandas as pd
import altair as alt
import numpy as np
from altair_saver import save
from pandas.core.indexes import category
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

with open("StarWars.csv", encoding='utf8',errors='ignore') as f:
    df = pd.read_csv(f, header = 1)

# QUESTION 1
# Shorten the column names and clean them up for easier use with pandas.
name_replacements = {"Response":"seen_starwars","Response.1":"fan",'Star Wars: Episode I  The Phantom Menace':'seen_1','Star Wars: Episode II  Attack of the Clones':'seen_2',
'Star Wars: Episode III  Revenge of the Sith':'seen_3','Star Wars: Episode IV  A New Hope':'seen_4','Star Wars: Episode V The Empire Strikes Back':'seen_5',
'Star Wars: Episode VI Return of the Jedi':'seen_6','Star Wars: Episode I  The Phantom Menace.1':'rating_1','Star Wars: Episode II  Attack of the Clones.1':'rating_2',
'Star Wars: Episode III  Revenge of the Sith.1':'rating_3','Star Wars: Episode IV  A New Hope.1':"rating_4",'Star Wars: Episode V The Empire Strikes Back.1':'rating_5',
'Star Wars: Episode VI Return of the Jedi.1':'rating_6', 'Han Solo':'Han_Solo_rating','Luke Skywalker':'Luke_Skywalker_rating', 'Princess Leia Organa':'Princess_Leia_Organa_rating',
'Anakin Skywalker':'Anakin_Skywalker_rating','Obi Wan Kenobi':'Obi_Wan_Kenobi_rating','Emperor Palpatine':'Emperor_Palpatine_rating', 'Darth Vader':'Darth_Vader_rating',
'Lando Calrissian':'Lando_Calrissian_rating', 'Boba Fett':'Boba_Fett_rating', 'C-3P0': 'C-3P0_rating', 'R2 D2':'R2_D2_rating', 'Jar Jar Binks':'Jar_Jar_Binks_rating',
'Padme Amidala':'Padme_Amidala_rating', 'Yoda':'Yoda_rating', 'Response.2':"shot_first", 'Response.3':"keu", 'Response.4':'feu','Response.5':'fst', 
'Response.6':'gender', 'Response.7':'age_range', 'Response.8':'income', 'Response.9':'education','Response.10':'location'}
df.rename(columns=name_replacements,inplace=True)

# QUESTION 2
# Filter the dataset to those that have seen at least one film.

# drops all people who say they have not seen star wars
df = df.drop(df[df.seen_starwars == "No"].index)

# drops all people who say they have not seen any of the star wars films
df = df.loc[~((df['seen_1'] != 'Star Wars: Episode I  The Phantom Menace') & (df['seen_2'] != 'Star Wars: Episode II  Attack of the Clones') 
& (df['seen_3'] != 'Star Wars: Episode III  Revenge of the Sith')  & (df['seen_4'] != 'Star Wars: Episode IV  A New Hope') 
& (df['seen_5'] != 'Star Wars: Episode V The Empire Strikes Back') & (df['seen_6'] != 'Star Wars: Episode VI Return of the Jedi')),:]

seen_data = pd.DataFrame(df)

# QUESTION 3
# Please validate that the data provided on GitHub lines up with the article by recreating 2 of their visuals and calculating 2 summaries that they report in the article.
chart_data = df
#Convert all columns to numbers for ease of use

qualites = 0
for value in chart_data.seen_1.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_1 == value, 'seen_1'] = qualites
for value in chart_data.seen_2.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_2 == value, 'seen_2'] = qualites
for value in chart_data.seen_3.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_3 == value, 'seen_3'] = qualites
for value in chart_data.seen_4.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_4 == value, 'seen_4'] = qualites    
for value in chart_data.seen_5.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_5 == value, 'seen_5'] = qualites
for value in chart_data.seen_6.unique():
    if qualites == 0:
        qualites += 1
    else: 
        qualites -= 1
    chart_data.loc[chart_data.seen_6 == value, 'seen_6'] = qualites
qualites = 0
for value in chart_data.shot_first.unique():
    #print(f"{value}: {qualites}")
    chart_data.loc[chart_data.shot_first == value, 'shot_first'] = qualites
    qualites += 1

#print(chart_data)

#Create the "Which 'Star Wars' Movies have you seen?" chart
chart_1_df = pd.DataFrame({'Movie': ['Star Wars: Episode I','Star Wars: Episode II','Star Wars: Episode III','Star Wars: Episode IV','Star Wars: Episode V','Star Wars: Episode VI'],
"Percent":[round(chart_data.seen_1.sum()/len(chart_data),2),round(chart_data.seen_2.sum()/len(chart_data),2),round(chart_data.seen_3.sum()/len(chart_data),2),round(chart_data.seen_4.sum()/len(chart_data),2),round(chart_data.seen_5.sum()/len(chart_data),2),round(chart_data.seen_6.sum()/len(chart_data),2)]})
chart = alt.Chart(chart_1_df,).mark_bar().encode(
    alt.X('Percent',title='Percent Watched',axis=alt.Axis(format='.0%')),
    y='Movie')
text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
    alt.Text('Percent:Q')
    ).properties(
    title={
      "text": ["Which 'Star Wars' Movies have you seen?"], 
      "subtitle": [f"Of {len(chart_data)} respondents who have seen any film"],
    }
    )
chart += text
#save(chart,'chart 1.png')

#Create the "Who Shot First" chart
counts =chart_data.shot_first.value_counts()
chart_2_df = pd.DataFrame({"Option": ["Han","Greedo","I don't understand this question"],
"Percent":[round(counts[2]/len(chart_data),2),round(counts[1]/len(chart_data),2),round(counts[0]/len(chart_data),2)]})
chart = alt.Chart(chart_2_df,).mark_bar().encode(
    alt.X('Percent',title='Percent Watched',axis=alt.Axis(format='.0%')),
    y='Option')
text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
    alt.Text('Percent:Q')
    ).properties(
    title={
      "text": ["Who Shot First?"], 
      "subtitle": [f"According to {len(chart_data)} respondents"],
    }
    )
chart += text
save(chart,'chart 2.png')


md = chart_data.query("gender == 'Male'")
rmd = md.query("fan == 'Yes'")
print(f"Male fan percentage: {(round(len(rmd)/len(md),4))*100}%")
fd = chart_data.query("gender == 'Female'")
rfd = fd.query("fan == 'Yes'")
print(f"Female fan percentage: {(round(len(rfd)/len(fd),4))*100}%")


# QUESTION 4
# Clean and format the data so that it can be used in a machine learning model. 
# Please achieve the following requests and provide examples of the table with a short description the changes made in your report.
clean_data = pd.DataFrame(df)
clean_data = clean_data.drop(columns="Unnamed: 0")
    # -Create an additional column that converts the age ranges to a number and drop the age range categorical column.
qualites = 0
for value in clean_data.age_range.unique():
    print(f"{value}: {qualites}")
    clean_data.loc[clean_data.age_range == value, 'age_range_group'] = qualites
    qualites += 1
clean_data = clean_data.drop(columns="age_range")
    # -Create an additional column that converts the school groupings to a number and drop the school categorical column.
qualites = 0
for value in clean_data.education.unique():
    print(f"{value}: {qualites}")
    clean_data.loc[clean_data.education == value, 'education_group'] = qualites
    qualites += 1
clean_data = clean_data.drop(columns="education")
    # -Create an additional column that converts the income ranges to a number and drop the income range categorical column.
qualites = 0
for value in clean_data.income.unique():
    print(f"{value}: {qualites}")
    clean_data.loc[clean_data.income == value, 'income_group'] = qualites
    qualites += 1
clean_data = clean_data.drop(columns="income")
    # -Create your target (also known as label) column based on the new income range column.
clean_data['target'] = 0
clean_data.loc[clean_data['income_group'] > 3, 'target'] = 1
    # -One-hot encode all remaining categorical columns.
Remaining_columns = ['seen_starwars', 'fan', 'seen_1', 'seen_2', 'seen_3',
       'seen_4', 'seen_5', 'seen_6', 'rating_1', 'rating_2', 'rating_3',
       'rating_4', 'rating_5', 'rating_6', 'Han_Solo_rating',
       'Luke_Skywalker_rating', 'Princess_Leia_Organa_rating',
       'Anakin_Skywalker_rating', 'Obi_Wan_Kenobi_rating',
       'Emperor_Palpatine_rating', 'Darth_Vader_rating',
       'Lando_Calrissian_rating', 'Boba_Fett_rating', 'C-3P0_rating',
       'R2_D2_rating', 'Jar_Jar_Binks_rating', 'Padme_Amidala_rating',
       'Yoda_rating', 'shot_first', 'keu', 'feu', 'fst', 'gender', 'location']
for column in Remaining_columns:
    qualites = 0
    for value in clean_data[column].unique():
        print(f"{value}: {qualites}")
        clean_data.loc[clean_data[column] == value, f'{column}'] = qualites
        qualites += 1

clean_data = clean_data.replace(np.nan, 50)



# QUESTION 5
# Build a machine learning model that predicts whether a person makes more than $50k.

def Classify(data,drop):
    #Seperate the data into our input data and our target data
    in_data = pd.DataFrame(data)
    for item in drop:
        in_data = in_data.drop(columns=item)
    #print(in_data)
    target_data = data.target


    #Convert pandas dataframes into numpy arrays
    x = in_data.to_numpy()
    y = target_data.to_numpy()

    #Initialize and implement the random forest classifier
    clf = RandomForestClassifier()
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)
    clf.fit(X_train,Y_train)
    guesses = clf.predict(X_test)
    key = Y_test

    #Interpret results and identify accuracy with various metrics.
    index = 0
    success = 0
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for value in guesses:
        if value == key[index]:
            if value == 0:
                true_positive += 1
            if value == 1:
                true_negative += 1
            success += 1
        else:
            if value == 0:
                false_positive += 1
            if value == 1:
                false_negative += 1
        index += 1

    #Calculate accuracy metrics
    accuracy = round(success/len(guesses)*100,2)
    precision = round((true_positive/(true_positive+false_positive))*100,2)
    recall = round((true_positive / (true_positive + false_negative))*100,2)
    f1 = round((2*precision*recall)/(precision+recall),2)

    return(accuracy,precision,recall,f1,success,len(guesses))

final_results = [0,0,0,0,0,0]
attempts = 0
runs = 1
while runs > 0: 
    results = Classify(clean_data,['target','income_group'])
    final_results[0] += results[0]
    final_results[1] += results[1]
    final_results[2] += results[2]
    final_results[3] += results[3]
    final_results[4] += results[4]
    final_results[5] += results[5]
        
    runs-=1
    attempts += 1

print(f"Accuracy: {round(final_results[0]/attempts,2)}% ({final_results[4]}/{final_results[5]})")
print(f"Recall: {round(final_results[1]/attempts,2)}%")
print(f"Percision: {round(final_results[2]/attempts,2)}%")
print(f"F1 Score: {round(final_results[3]/attempts,2)}%")










#with open("StarWars.csv", encoding='utf8',errors='ignore') as f:
#    test = pd.read_csv(f, header = 1)
#
#percent = len(seen_data)/len(test)
#print(percent)
#percent = len(seen_data.query("gender == 'Male'"))/len(test)
#print(percent)


