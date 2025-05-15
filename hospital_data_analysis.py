
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Health_dataset.csv')

# Check if the file exists before proceeding
if os.path.exists(file_path):
    # Load data from CSV
    health_data = pd.read_csv(file_path)

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(health_data.head())

    # Count the number of patients (records)
    total_records = health_data.shape[0]

    # Print the total number of patients
    print(f"Total Patients: {total_records}")
else:
    print("Error: File not found. Please check the file path.")


# How is the patient population distributed by gender?
gender_count = health_data['Gender'].value_counts()

print("\nPatient Population Distribution by Gender:")
for gender, count in gender_count.items():
    print(f"{gender}: {count} patients")
    

# How is the patient population distributed by gender?
gender_count = health_data['Gender'].value_counts()

# Set the style for the plot
sns.set_style("whitegrid")

# Define custom colors
custom_colors = ["skyblue", "lightgreen"]

# Create a bar plot
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=gender_count.index, y=gender_count.values, palette=custom_colors)

# Add labels and title
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Patient Population Distribution by Gender")
plt.xticks(rotation=0)  # Keep labels horizontal

# Annotate bars with the total number of patients
for i, count in enumerate(gender_count.values):
    ax.text(i, count + 5, str(count), ha='center', color='black', fontsize=12)

# Save the plot as an image
plt.savefig("images/gender_distribution.png", dpi=300, bbox_inches='tight')

plt.show()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%', 
        colors=["skyblue", "lightgreen"], startangle=90)
plt.title("Patient Population Distribution by Gender")

# Save the pie chart as an image
plt.savefig("images/gender_distribution_pie.png", dpi=300, bbox_inches='tight')

plt.show()



# Convert columns to datetime
health_data['Admission Date'] = pd.to_datetime(health_data['Admission Date'])
health_data['Date of Birth'] = pd.to_datetime(health_data['Date of Birth'])

# Calculate Age
health_data['Age'] = (health_data['Admission Date'] - health_data['Date of Birth']).dt.days // 365

# Define Age Bins and Labels
age_bins = [0, 20, 40, 60, 80, 100, 200]  # Extended upper limit to 200
age_labels = ["0-20", "21-40", "41-60", "61-80", "81-100", "100+"]

# Categorize patients into Age Groups
health_data['Age Group'] = pd.cut(health_data['Age'], bins=age_bins, labels=age_labels, 
                                  right=True, include_lowest=True)

# Check if all patients are categorized
missing_age_group = health_data['Age Group'].isna().sum()
print(f"Patients without an Age Group: {missing_age_group}")

# Display count of patients in each age group
age_group_counts = health_data['Age Group'].value_counts()
print(age_group_counts)


# Load data
health_data = pd.read_csv(r"C:\Users\user\Downloads\Python Project\Health Dataset Python\Health Dataset Python\Health_dataset.csv")

# Convert columns to datetime
health_data['Admission Date'] = pd.to_datetime(health_data['Admission Date'])
health_data['Date of Birth'] = pd.to_datetime(health_data['Date of Birth'])

# Calculate Age at Admission
health_data['Age'] = (health_data['Admission Date'] - health_data['Date of Birth']).dt.days // 365

# Define Age Bins and Labels (Upper limit set to 200)
age_bins = [0, 20, 40, 60, 80, 100, 200]
age_labels = ["0-20", "21-40", "41-60", "61-80", "81-100", "100+"]

# Categorize patients into Age Groups
health_data['Age Group'] = pd.cut(health_data['Age'], bins=age_bins, labels=age_labels, 
                                  right=True, include_lowest=True)

# Count number of patients in each age group
age_group_counts = health_data['Age Group'].value_counts().sort_index()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, 
            palette=['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink', 'lightyellow'])

# Adding chart labels and title
plt.title('Patient Distribution by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)

# Display total count of patients in each age group on top of bars
for i, v in enumerate(age_group_counts.values):
    plt.text(i, v + 50, str(v), ha='center', fontsize=12)

# Show the plot
plt.show()


# Which diseases are most commonly diagnosed among patients (Top 3)?

# Check the top 3 most diagnosed diseases
top_3_diseases = health_data['Disease'].value_counts().head(3)

# Display the result
print("Top 3 Diseases Diagnosed:")
print(top_3_diseases)


# Identify the top 3 most diagnosed diseases
top_3_diseases = health_data['Disease'].value_counts().head(3)

# Plotting the bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=top_3_diseases.index, y=top_3_diseases.values, palette='muted')

# Adding chart labels and title
plt.title('Top 3 Most Diagnosed Diseases', fontsize=16)
plt.xlabel('Disease', fontsize=14)
plt.ylabel('Number of Patients Diagnosed', fontsize=14)

# Display total count of patients on top of bars
for i, v in enumerate(top_3_diseases.values):
    plt.text(i, v + 50, str(v), ha='center', fontsize=12)

# Show the plot
plt.show()


# Identify the top 3 most diagnosed diseases
top_3_diseases = health_data['Disease'].value_counts().head(3)

# Calculate the total number of patients diagnosed with the top 3 diseases
total_top_3 = top_3_diseases.sum()

# Calculate the percentage relative to the top 3 total
top_3_percentages_relative = np.round((top_3_diseases / total_top_3) * 100).astype(int)

# Adjust for rounding to ensure the total is exactly 100%
difference = 100 - top_3_percentages_relative.sum()
top_3_percentages_relative.iloc[0] += difference  # Adjust the largest category

# Combine count and percentage
top_3_summary_relative = pd.DataFrame({'Count': top_3_diseases, 'Percentage': top_3_percentages_relative.astype(str) + "%"})

# Display the total number of patients diagnosed with the top 3 diseases
print(f"Total number of patients diagnosed with the top 3 diseases: {total_top_3:,}")

# Display the formatted summary table
print("\nTop 3 Diseases with Counts and Percentages (Relative to Top 3 Total):")
print(top_3_summary_relative)

# Plotting the bar chart for top 3 diseases
plt.figure(figsize=(8, 5))
sns.barplot(x=top_3_diseases.index, y=top_3_diseases.values, palette='muted')

# Adding chart labels and title
plt.title('Top 3 Most Diagnosed Diseases (Relative %)', fontsize=16)
plt.xlabel('Disease', fontsize=14)
plt.ylabel('Number of Patients Diagnosed', fontsize=14)

# Display total count and percentage on top of bars
for i, (count, percentage) in enumerate(zip(top_3_diseases.values, top_3_percentages_relative.values)):
    plt.text(i, count + 50, f"{count:,} ({percentage}%)", ha='center', fontsize=12)

# Show the plot
plt.show()



# Define the number of top diseases to extract
top_n = 5  # Change this value to get top N diseases (e.g., top 10, top 15, etc.)

# Filter dataset by gender
male_diseases = health_data[health_data['Gender'] == 'Male']['Disease'].value_counts().head(top_n)
female_diseases = health_data[health_data['Gender'] == 'Female']['Disease'].value_counts().head(top_n)

# Display top diseases for each gender
print(f"Top {top_n} Diseases Among Males:\n{male_diseases}\n")
print(f"Top {top_n} Diseases Among Females:\n{female_diseases}\n")

# Plot the bar chart
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Male Diseases Chart
sns.barplot(x=male_diseases.values, y=male_diseases.index, palette='Blues_r', ax=axes[0])
axes[0].set_title(f"Top {top_n} Diseases Among Males", fontsize=14)
axes[0].set_xlabel("Number of Patients", fontsize=12)
axes[0].set_ylabel("Disease", fontsize=12)

# Female Diseases Chart
sns.barplot(x=female_diseases.values, y=female_diseases.index, palette='Reds_r', ax=axes[1])
axes[1].set_title(f"Top {top_n} Diseases Among Females", fontsize=14)
axes[1].set_xlabel("Number of Patients", fontsize=12)
axes[1].set_ylabel("Disease", fontsize=12)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()


# Convert columns to datetime format
health_data['Admission Date'] = pd.to_datetime(health_data['Admission Date'], errors='coerce')
health_data['Discharge Date'] = pd.to_datetime(health_data['Discharge Date'], errors='coerce')

# Calculate Length of Stay (LOS) in days
health_data['Length of Stay'] = (health_data['Discharge Date'] - health_data['Admission Date']).dt.days

# Define stay duration categories
bins = [-1, 0, 3, 7, 14, 21, float('inf')]
labels = ['Same Day', '1-3 Days', '4-7 Days', '8-14 Days', '15-21 Days', 'Above 21 Days']

# Categorize patients based on length of stay
health_data['Stay Category'] = pd.cut(health_data['Length of Stay'], bins=bins, labels=labels, right=True)

# Count patients in each stay category
stay_distribution = health_data['Stay Category'].value_counts().sort_index()

# Display results
print("Patient Stay Distribution:\n")
print(stay_distribution)

# Create a bar chart
plt.figure(figsize=(10, 5))
sns.barplot(x=stay_distribution.index, y=stay_distribution.values, palette="coolwarm")

# Add labels and title
plt.xlabel("Length of Stay Category", fontsize=12)
plt.ylabel("Number of Patients", fontsize=12)
plt.title("Patient Stay Duration Distribution", fontsize=14)

# Display the values on the bars
for index, value in enumerate(stay_distribution.values):
    plt.text(index, value + 50, f"{value:,}", ha='center', fontsize=10, fontweight='bold')

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Remove blank (NaN) values in "Cause of Death" column
health_data = health_data.dropna(subset=['Cause of Death'])

# Function to get the top N causes of death
def top_causes_of_death(n=5):
    # Count occurrences of each cause of death
    death_counts = health_data['Cause of Death'].value_counts().head(n)

    # Display results
    print(f"\nTop {n} Causes of Death:\n")
    print(death_counts.to_string())

    # Create a bar chart
    plt.figure(figsize=(10, 5))
    sns.barplot(x=death_counts.index, y=death_counts.values, palette="Reds_r")

    # Add labels and title
    plt.xlabel("Cause of Death", fontsize=12)
    plt.ylabel("Number of Patients", fontsize=12)
    plt.title(f"Top {n} Most Common Causes of Death", fontsize=14)

    # Display values on the bars
    for index, value in enumerate(death_counts.values):
        plt.text(index, value + 5, f"{value:,}", ha='center', fontsize=10, fontweight='bold')

    # Show the plot
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Call the function (Change the number as needed)
top_causes_of_death(n=5)  # Change "5" to any number (e.g., 10, 15, etc.)


# Count occurrences of each Treatment Status
treatment_counts = health_data['Treatment Status'].value_counts()

# Total number of patients
total_patients = treatment_counts.sum()

# Calculate percentage for each category
treatment_percentages = (treatment_counts / total_patients) * 100

# Round percentages and add "%" symbol
treatment_summary = pd.DataFrame({
    'Count': treatment_counts,
    'Percentage': treatment_percentages.round(2).astype(str) + "%"
})

# Display the results
print("\nTreatment Status Distribution:")
print(treatment_summary.to_string())


# Count occurrences of each Treatment Status
treatment_counts = health_data['Treatment Status'].value_counts()

# Total number of patients
total_patients = treatment_counts.sum()

# Calculate percentage for each category
treatment_percentages = (treatment_counts / total_patients) * 100

# Create a Doughnut chart
plt.figure(figsize=(8, 8))

# Plot a pie chart
plt.pie(treatment_percentages, labels=treatment_percentages.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ff6666'])

# Draw a circle at the center to make it a doughnut chart
centre_circle = plt.Circle((0, 0), 0.50, color='white', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.title('Treatment Status Distribution', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()


# Convert Admission Date and Discharge Date to datetime format
health_data['Admission Date'] = pd.to_datetime(health_data['Admission Date'], errors='coerce')
health_data['Discharge Date'] = pd.to_datetime(health_data['Discharge Date'], errors='coerce')

# Extract Admission Day of the Week and Month
health_data['Admission Day'] = health_data['Admission Date'].dt.day_name()
health_data['Admission Month'] = health_data['Admission Date'].dt.month_name()

# Create a pivot table for the heatmap
pivot_table = health_data.pivot_table(index='Admission Day', columns='Admission Month', aggfunc='size', fill_value=0)

# Sort days of the week in order
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_table = pivot_table.reindex(day_order)

# Sort months in calendar order from January to December
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
pivot_table = pivot_table[month_order]

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', linewidths=0.5, linecolor='gray', fmt='d')
plt.title('Heatmap of Admissions by Day of the Week and Month', fontsize=14)
plt.xlabel('Admission Month')
plt.ylabel('Admission Day')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


# Gender Distribution
def gender_distribution():
    plt.figure(figsize=(6,4))
    sns.countplot(x='Gender', data=df, palette='Set2')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# Age Distribution
def age_distribution():
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Recovery Rate by Age Group
def recovery_rate_by_age_group():
    age_bins = [0, 18, 30, 45, 60, 75, 100]
    df['Age_Group'] = pd.cut(df['Age'], bins=age_bins)
    recovery_counts = df[df['Treatment_Status'] == 'Recovered'].groupby('Age_Group').size()
    total_counts = df.groupby('Age_Group').size()
    recovery_rate = (recovery_counts / total_counts * 100).fillna(0)

    plt.figure(figsize=(10,6))
    recovery_rate.plot(kind='bar', color='green')
    plt.title('Recovery Rate by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Recovery Rate (%)')
    plt.tight_layout()
    plt.show()

# Top Causes of Death
def top_causes_of_death(top_n=10):
    death_causes = df[df['Treatment_Status'] == 'Deceased']['Diagnosis'].value_counts().head(top_n)

    plt.figure(figsize=(10,6))
    death_causes.plot(kind='bar', color='crimson')
    plt.title(f'Top {top_n} Causes of Death')
    plt.xlabel('Cause of Death')
    plt.ylabel('Number of Patients')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Treatment Status Summary Table
def treatment_status_summary():
    status_counts = df['Treatment_Status'].value_counts()
    total = status_counts.sum()
    summary = pd.DataFrame({
        'Count': status_counts,
        'Percentage': (status_counts / total * 100).round(2)
    })
    print("Treatment Status Summary:")
    print(summary)

# Doughnut Chart for Treatment Status
def treatment_status_doughnut():
    treatment_counts = df['Treatment_Status'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(treatment_counts, labels=treatment_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops={'width':0.5})
    plt.title('Treatment Status Distribution')
    plt.tight_layout()
    plt.show()

# Heatmap of Admissions by Day and Month
def admission_heatmap():
    df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
    df['Month'] = df['Admission_Date'].dt.month_name()
    df['Day'] = df['Admission_Date'].dt.day_name()
    heatmap_data = df.groupby(['Day', 'Month']).size().unstack(fill_value=0)

    plt.figure(figsize=(12,6))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Admissions by Day and Month')
    plt.xlabel('Month')
    plt.ylabel('Day')
    plt.tight_layout()
    plt.show()


