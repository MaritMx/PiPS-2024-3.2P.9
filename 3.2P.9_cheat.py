# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:00:52 2024

@author: Marit
"""

def cheat (question):
    if question == 1:
        print("data = np.random.uniform(low=-10, high=10, size=100)")
    
        print("plt.figure(figsize=(10, 6))")
        print("plt.boxplot(data)")
        print("plt.xlabel('Values')")
        print("plt.show()")
    
        print("plt.figure(figsize=(10, 6))")
        print("sns.violinplot(data, inner=None, color='lightgray')")
        print("sns.stripplot(data, jitter=True, color='black', size=4)")
        print("plt.title('Violinplot with Jittered Data Points')")
        print("plt.xlabel('Values')")
        print("plt.show()")

    elif question == 2: 
        print("titanic_data = pd.read_csv('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv')")

        print("plt.figure(figsize=(12, 8))") 
        print("plt.hist([titanic_data[titanic_data['Survived'] == 0]['Age'].dropna(), titanic_data[titanic_data['Survived'] == 1]['Age'].dropna()],bins=50, label=['Not Survived', 'Survived'], stacked = True)")
        print("plt.title('Distribution of Age by Survival Status on Titanic')")
        print("plt.xlabel('Age')")
        print("plt.ylabel('Count')")
        print("plt.legend()")
        print("plt.show()")