import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_name = 'main.csv'
crime_data = pd.read_csv(file_name)
crime_data.fillna(0, inplace=True)

#Initial Exploratory Data Analysis
print("\n INITIAL EDA STARTS HERE")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
# First few rows
print("\n First 5 rows of the dataset:")
print(crime_data.head())
# Last few rows
print("\n Last 5 rows of the dataset:")
print(crime_data.tail())
# Shape of the dataset
print(f"\n Shape of the dataset: {crime_data.shape} (Rows, Columns)")
# Data types and non-null info
print("\n️ Dataset Info:")
print(crime_data.info())
# Descriptive statistics
print("\n Statistical Summary:")
print(crime_data.describe(include='all'))
# Checking for missing values
print("\n Missing Values Count:")
print(crime_data.isnull().sum())

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" EDA Completed\n")

# Predefined columns for different categories
violent_types = ['MURDER', 'ATTEMPT TO MURDER', 'RAPE', 'RIOTS', 'HURT/GREVIOUS HURT']

women_related = ['RAPE', 'DOWRY DEATHS', 'CRUELTY BY HUSBAND OR HIS RELATIVES',
                 'ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY',
                 'INSULT TO MODESTY OF WOMEN']

property_related = ['THEFT', 'AUTO THEFT', 'BURGLARY', 'ROBBERY', 'DACOITY']

focused_crimes = ['MURDER', 'ATTEMPT TO MURDER', 'RAPE', 'ROBBERY', 'BURGLARY',
                  'THEFT', 'RIOTS', 'DOWRY DEATHS', 'AUTO THEFT']

def show_menu():
    print("\n What would you like to explore?")
    print("1.  View Predefined Crime Insights")
    print("2.  Create Your own Crime Insight")
    print("3.  Exit")
    return input("Enter your choice (1/2/3): ")

def choose_plot_type():
    print("\n Choose a graph type:")
    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Pie Chart")
    print("4. Scatter Plot")
    return input("Enter graph type number: ")

def pick_analysis_goal():
    print("\n Choose one of the following objectives:")
    print("1. Top 10 Districts with Highest Number of IPC Crimes")
    print("2. Trend of Violent Crimes Over region")
    print("3. Crimes Against Women - Top States")
    print("4. Kidnapping Analysis by Victim Type")
    print("5. Share of Property Crimes")
    print("6. Correlation Heatmap")
    return input("Enter your objective number (1-6): ")

def plot_insights(option):
    #Barplot 
    if option == '1':
        crime_data['Total_Reported'] = crime_data.iloc[:, 3:].sum(axis=1)
        top_states = crime_data.groupby('STATE/UT')['Total_Reported'].sum().nlargest(10)
        print(top_states)
        plt.figure(figsize=(12,6))
        sns.barplot(x=top_states.values, y=top_states.index, palette='Reds_d')
        plt.title('Top 10 States with Highest Number of IPC Crimes')
        plt.xlabel('Total Crimes')
        plt.ylabel('State/UT')
        plt.tight_layout()
        plt.show()
    #Line Plot
    elif option == '2':
        region_violent = crime_data.groupby('Region')[violent_types].sum()
        print(region_violent)
        plt.figure(figsize=(10,6))
        
        for category in violent_types:
            plt.plot(region_violent.index, region_violent[category], label=category)
        plt.title('Trend of Violent Crimes Over Region')
        plt.xlabel('Region')
        plt.ylabel('Number of Cases')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    #Barplot
    elif option == '3':
        statewise_women_crime = crime_data.groupby('STATE/UT')[women_related].sum().sum(axis=1).nlargest(10)
        plt.figure(figsize=(12,6))
        sns.barplot(x=statewise_women_crime.values, y=statewise_women_crime.index, palette='Purples_r')
        plt.title('Top 10 States with Highest Crimes Against Women')
        plt.xlabel('Number of Cases')
        plt.ylabel('State')
        plt.tight_layout()
        plt.show()
    #Grouped Bar 
    elif option == '4':
        kidnapping_stats = crime_data.groupby('STATE/UT')[
            ['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS', 'KIDNAPPING AND ABDUCTION OF OTHERS']
        ].sum().nlargest(10, 'KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS')
        plt.figure(figsize=(12,6))
        kidnapping_stats.plot.bar(stacked=False, colormap='coolwarm')
        plt.title('Kidnapping by Victim Type (Top 10 States)')
        plt.xlabel('State')
        plt.ylabel('Number of Cases')
        plt.tight_layout()
        plt.show()
    #Pie Chart 
    elif option == '5':
        prop_crime_total = crime_data[property_related].sum()
        plt.figure(figsize=(8,8))
        plt.pie(prop_crime_total, labels=prop_crime_total.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
        plt.title('Share of Property Crimes')
        plt.tight_layout()
        plt.show()
    #Heatmap 
    elif option == '6':
        plt.figure(figsize=(12,8))
        sns.heatmap(crime_data[focused_crimes].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Crime Type Correlation Heatmap')
        plt.tight_layout()
        plt.show()
    else:
        print("Invalid choice.")

def explore_custom():
    print("\n Columns available for analysis:\n")
    for idx, column in enumerate(crime_data.columns):
        print(f"{idx+1}. {column}")

    try:
        x_col = input("\nEnter the first column name: ").strip()
        y_col = input("Enter second column name (leave blank if not needed): ").strip()
        chart_type = choose_plot_type()

        plt.figure(figsize=(10,6))

        if chart_type == '1':
            sns.barplot(data=crime_data, x=x_col, y=y_col if y_col else None)
            plt.title(f'Bar Plot: {x_col} vs {y_col}')
        elif chart_type == '2':
            if y_col:
                plt.plot(crime_data[x_col], crime_data[y_col])
            else:
                crime_data[x_col].plot()
            plt.title(f'Line Plot: {x_col} vs {y_col}')
        elif chart_type == '3':
            top_values = crime_data[x_col].value_counts().head(10)
            plt.pie(top_values, labels=top_values.index, autopct='%1.1f%%')
            plt.title(f'Pie Chart of {x_col}')
        elif chart_type == '4':
            sns.scatterplot(data=crime_data, x=x_col, y=y_col, hue='STATE/UT', palette='coolwarm', legend=False)
            plt.title(f'Scatter Plot: {x_col} vs {y_col}')
        else:
            print(" Invalid graph type.")

        plt.tight_layout()
        plt.grid(True)
        plt.show()
    except Exception as error:
        print(" Something went wrong:", error)

# Main interaction loop
while True:
    user_choice = show_menu()
    if user_choice == '1':
        analysis_choice = pick_analysis_goal()
        plot_insights(analysis_choice)
    elif user_choice == '2':
        explore_custom()
    elif user_choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid input. Try again.")
