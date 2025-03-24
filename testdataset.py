import pandas as pd

# Load the dataset
file_path = "dataset/UpdatedResumeDataSet.csv"
df = pd.read_csv(file_path)

# Show some basic info
print("✅ Total resumes loaded:", len(df))
print("\n📄 First 5 resumes:")
print(df.head(5))
