import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    data = pd.read_csv("ds_salaries.csv")
    return data

# Load data
data = load_data()

# Top 10 Film berdasarkan IMDb Rating
# Sorting data by IMDb rating in descending order and selecting top 10
top_10_movies = data.sort_values(by='IMDb Rating', ascending=False).head(10)

# Setting up Streamlit app
st.header('Top 10 Film dengan IMDb Rating Tertinggi')

# Defining custom colors for the bar chart
custom_colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2C7873', '#1287A5', '#5DADE2', '#85C1E9', '#D7BDE2', '#F4D03F']

# Displaying bar chart using Streamlit with custom colors
st.bar_chart(top_10_movies.set_index('Title')['IMDb Rating'], color=custom_colors)
st.write("Grafik ini menampilkan 10 film dengan rating IMDb tertinggi dalam data. Film-film ini memiliki rating yang sangat tinggi, menunjukkan bahwa mereka sangat dihargai oleh penonton dan kritikus.")

# Top 5 positions with highest salaries
st.subheader("5 Posisi dengan Gaji Terbesar")
top_5_positions = data.groupby('job_title')['salary_in_usd'].mean().nlargest(5)
st.bar_chart(top_5_positions)



# Scatter plot of salary against experience level
st.subheader("Korelasi antara Gaji dan Tingkat Pengalaman")
scatter_plot = sns.scatterplot(data=data, x='experience_level', y='salary_in_usd', alpha=0.5)
scatter_plot.set_title('Korelasi antara Gaji dan Tingkat Pengalaman')
scatter_plot.set_xlabel('Tingkat Pengalaman')
scatter_plot.set_ylabel('Gaji (USD)')
st.pyplot(plt.gcf())


# Distribution of job positions
st.subheader("10 Posisi Pekerjaan Teratas")
position_distribution = data['job_title'].value_counts().head(10)
st.write(position_distribution)

# Distribution of job positions (as pie chart)
st.subheader("Distribusi Posisi Pekerjaan")
fig, ax = plt.subplots()
position_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
ax.axis('equal')  
st.pyplot(fig)
