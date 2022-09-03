### INTRODUCTION
This data analytics project is a visual exploration of prosper loan dataset. The exploration goes through three stages, namely: univariate, bivariate, multivariate exploration to uncover insights relating to how a few other features in the dataset influence Borrower Annual Percentage Rate (BorrowerAPR) feature. It also includes little data wrangling and feature engineering activities.

### DATASET

Prosper loan dataset contains 113,937 records (rows) of loans taken and 81 features (columns). Among the columns, is the LoanKey column, which uniquely identifies every loan in the dataset. Other columns include BorrowerAPR, LenderYield, BorrowerState and many more. The prosper loan dataset can be downloaded online [here](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv%26amp;sa%3DD%26amp;ust%3D1581581520570000&sa=D&source=editors&ust=1661879111388315&usg=AOvVaw05Qfnz_qFXWz5S81-e5Y41). The data describtion file with information about each column in the dataset can be found online [here](https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/edit#gid=0)

Preliminary data wrangling involved exploring the quality of the data using functions like .head(), .shape(), .info(), .describe() etc and perform data cleaning by: dropping duplicated records based on the LoanKey column; dropping not needed columns; replacing entries such as 'Not available' with NAN in EmploymentStatus column; change feature data type and lastly drop rows with NANs for completeness.

After preliminary data wrangling, the dataset used for visual explorations had 103,623 rows and 13 columns.


### SUMMARY OF FINDINGS
This exploration goes through the following stages of exploration to come up with findings:
1. Univariate: Explored individual features, looking at their distributions and found that - most borrowers; had 36 month terms, had verifiable income, where employed, had income in the range \\$25,499 to \$74,999 and never had a prosper loan.

2. Bivariate: Explored interaction between two features leading to the findings that: type of borrower Term, if borrower had a home or not, borrower credit rating, income range of borrower, if borrower income is verifiable or not, and the number of prosper loan already taken, had effect on the BorrowerAPR.

3. Mulitvariate: Explored the interaction between multiple features and finding include; borrowers having a mid credit score rating, without previous prosper loan might not have their home owning status or income range influence thier BorrowerAPR. Home owners who got lower BorrowerAPR than their counterparts and none home owners in other regions, where in the West region.


### INSIGHTS IN PRESENTATION
The file `slide_deck.ipynb`, is a presentation from this project that goes through stages of exploration mentioned above, looking at the distribution of features such as BorrowerAPR, BorrowerState, BorrowerRegion, IsBorrowerHomeowner, IncomeRange, and others. It also conveys reson for feature engineering done in the exploration and the difference made in visualising the source features.

Further more it goes on to show the interaction between BorrowerAPR, and features of interests - some already mentioned. These interactions inlude bivariate interactions and multivariate interactins in regards to how BorrowerAPR is influenced by these features.

### PROJECT ENVIRONMENT
Project was carried out in Anaconda environment using the following python packages:
 - JuPyter notebook
 - Pandas
 - Numpy
 - Matplotlib
 - seaborn