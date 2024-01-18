import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the JSON file
file_path = 'ChatGPT_Eval.Computer_Security.json'

# Read the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Create a DataFrame
df = pd.DataFrame(data)

# Extracting only the first character of ChatGPT's response
df['ChatGPT_Response_Option'] = df["ChatGPT's response"].str.extract(r'([ABCD])')

# Calculate accuracy rate
correct_responses = df['ChatGPT_Response_Option'] == df['Answer']
accuracy_rate = correct_responses.mean()

# Calculate correlation between query duration and correctness
df['Correct'] = correct_responses
correlation = df[['Query_duration', 'Correct']].corr()

# Print the accuracy rate and correlation
print("Accuracy Rate:", accuracy_rate)
print("Correlation:\n", correlation)

# Setting the style for the plot
sns.set(style="whitegrid")

# Creating a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Query_duration', y='Correct', alpha=0.7)

plt.title('Correlation Between Query Duration and Correctness of ChatGPT Responses')
plt.xlabel('Query Duration (seconds)')
plt.ylabel('Correct Response (True/False)')
plt.show()
