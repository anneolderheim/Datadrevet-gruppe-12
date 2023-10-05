import numpy as np
import pandas as pd
from ast import If
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

education_mapping = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

# Importing the dataset
dataset = pd.read_csv('graduation_dataset.csv')

# Translate Mother's qualification column using the education_mapping
dataset["Mother's qualification"] = dataset["Mother's qualification"].map(education_mapping)


print(dataset.head(5))

print(dataset.describe())

sns.scatterplot(x="Mother's qualification", y="Age at enrollment", data=dataset, hue=dataset["Target"])
plt.show()

# Removing the last column
# dataset = dataset.iloc[:, :-1]

# f = plt.figure(figsize=(15, 15))
# sns.heatmap(dataset.corr(),annot=False, cmap='RdBu',vmax=.3, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5})
# plt.show()