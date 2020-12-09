# python-challenge
* There are two Python Challenges with 2 names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder we have the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files used. The script has the correct path to the CSV file.
  * An "analysis" folder that contains the text file that has the results from the analysis.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* This challenge is for creating a Python script for analyzing the financial records of your company. You will given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* The task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, we are tasked with helping a small, rural town modernize its vote counting process.

* we will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.


