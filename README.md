## Application_Rating_Analysis

#### Project Description:
In this project, I utilized Python to perform an analysis of application ratings.

I began by loading the data from the "applications.csv" file into a Pandas DataFrame and conducted data cleaning tasks, which included eliminating duplicate applicant_id entries, filling missing values in the 'External Rating' field with zeros, and addressing missing values in the 'Education level' field by assigning them the label "Secondary."

To enrich the DataFrame, I incorporated data from the "industries.csv" file, specifically industry rankings.

The project's core task involved calculating application ratings based on the following criteria: The rating must range from 0 to 100 and is determined by the summation of evaluations across six criteria. The rating remains null if the 'Amount' or 'External Rating' fields are missing or null.

The rating components encompass:
1. Adding 20 points if the applicant's age falls between 35 and 55.
2. Adding 20 points if the application was not submitted on a weekend.
3. Adding 20 points if the applicant is married.
4. Adding 10 points if the applicant is located in Kyiv or the surrounding region.
5. Including the 'Score' value from the "industries.csv" table, ranging from 0 to 20 points.
6. Adding 20 points if 'External Rating' is greater than or equal to 7.
7. Deducting 20 points if 'External Rating' is less than or equal to 2.

The resulting table includes only applications with ratings greater than zero, signifying acceptance.

I grouped the data by the application submission week and generated a plot illustrating the average rating of accepted applications for each week.

#### Skills:
Python, NumPy, Pandas, Matplotlib, Jupyter Notebook
