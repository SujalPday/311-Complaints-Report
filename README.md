# 📊 NYC 311 Complaints

This report presents a comprehensive analysis of New York City's 311 service request data for the year 2025.
The dataset encompasses complaints filed across all five boroughs 
— Brooklyn, Queens, Bronx, Manhattan, and Staten Island — spanning residential, infrastructure, and quality-of-life concerns.

## 🪛 Technologies

- `Python`
- `Pandas`
- `Matplotlib-Pyplot`
- `Seaborn`
- `PyCharm`
- `Sublime Text`

## 👩🏽‍🍳 The Process

- I created a list for all the months in 2025 and imported the data with reference to the months from the "cityofnewyork.us" website with the help of ChatGPT.
- Merged all the data into a big file and imported the raw data into the local directory.
- Cleaned the data by fixing the dates, standardising text columns, sorting invalid values, ensuring the right length of the zipcodes, dropped unusable rows, farmatted date/time in right format, dropped negative resolution values, and saved the cleaned file.
- Performed data analysis using "Pyplot" and "Seaborn".
- Generated and saved all the charts.
- Analysed the charts and prepared a report using "MS Word".

## 📋 Key Findings

- **Monthly Complaint Volume Trend:** Volume of complaints throughout the year were measured showing high-volume usage of the 311 service with limited seasonal sensitivity.
- **Borough-Level Distribution:** Total number of complaints were divided for 5 major areas of the NYC where •	Brooklyn accounted for the largest share of complaints, reflecting both its population size and density.
- **Top Complaint Types:** •	Illegal Parking was the top complaint by a significant margin, suggesting persistent parking enforcement gaps, followed by noise, heat/hot water, and encampment related complaints.

## 📚 What I Learned

During this project, I learned about how to import big data and how to take advantage of AI tools for such operations.

## ✏️ Note Taking

While making this project, I made notes on every step. Every line of code I wrote, what it did, what was the outcome of the specific command, everything was journaled and I use these notes later for referencing in my next projects.

## 📈 Overall Growth

This project taught me how important it is to get all your work organised as it has 2 million+ rows of data to work with and a lot of files that had to me sorted and managed throughout the project. On top of that, I can now download any of public data, no matter the size using pyhton. Reporting was one more factor that I would say got better during this project.

## ⚙️ Running the Project

To run the project in your local environment:

1. Download the [311](https://github.com/SujalPday/311-Complaints-Report/blob/main/311.py "Go to 311.py file") file and the [Excel](https://drive.google.com/file/d/1Vy8GZci3jPBS1nfQBVY86i_bqmr9kTvh/view?usp=drive_link "Link to the Excel file") file into your system.
2. Download the "Pandas", "Matplotlib", "Seaborn" modules for python.
3. Copy the location of the directory where you saved the database file.
4. Open the "311.py" file.
5. Paste the location of the file in the "df" variable. (replace, "[Paste location here]" with file location)
6. Run the program and all the charts will be generated and saved in the same directory where your project files are saved.

#### Fun Fact:
I had to upgrade my RAM by 8gb in order to work with this big of data. In this market. <img width="25" height="24" alt="thisisfine" src="https://github.com/user-attachments/assets/9b8dd11b-ac00-4087-bb5f-d0006a99abc4" />
