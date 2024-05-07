import streamlit as st
import pandas as pd
import seaborn as sns

# Load data
@st.cache
def load_data():
    data = pd.read_csv("ds_salaries.csv")
    return data

# Load data
data = load_data()

# Top 5 positions with highest salaries
st.subheader("5 Posisi dengan Gaji Terbesar")
top_5_positions = data.groupby('job_title')['salary_in_usd'].mean().nlargest(5)
st.bar_chart(top_5_positions)

# Distribution of job positions
st.subheader("10 Posisi Pekerjaan Teratas")
position_distribution = data['job_title'].value_counts().head(10)
st.write(position_distribution)

# Scatter plot of salary against experience level
st.subheader("Korelasi antara Gaji dan Tingkat Pengalaman")
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='experience_level', y='salary_in_usd', alpha=0.5)
plt.title('Korelasi antara Gaji dan Tingkat Pengalaman')
plt.xlabel('Tingkat Pengalaman')
plt.ylabel('Gaji (USD)')
st.pyplot(plt)
