# 📊 Swiggy Financial Regression Analysis

| Category        | Details                                 |
| --------------- | --------------------------------------- |
| Project Type    | Business Analytics                      |
| Industry        | Food Delivery                           |
| Company         | Swiggy                                  |
| Tools Used      | Python, Pandas, Statsmodels, Matplotlib |
| Analysis Type   | Multiple Linear Regression              |
| Target Variable | Total Assets                            |
| Status          | Completed                               |

## Applying statistical modeling to understand the financial drivers of business performance through data-driven analysis.

## Executive Summary

Financial variables within an organization are interconnected and collectively influence business performance.

This project applies Multiple Linear Regression (Ordinary Least Squares) to analyze how key financial indicators contribute to Swiggy's Total Assets.

The analysis demonstrates the application of statistical modeling techniques to business analytics and financial decision-making.

## Business Context

Understanding the factors influencing Total Assets is an essential aspect of financial analysis and strategic planning.

Regression analysis enables analysts to estimate the relative contribution of different financial variables and identify important business drivers.

This project explores these relationships using publicly available financial statement data from Swiggy.

## Objectives

Apply Multiple Linear Regression to financial statement data

Analyze relationships between financial variables and Total Assets

Estimate regression coefficients

Visualize coefficient importance

Demonstrate statistical modeling for business analytics

## Dataset

### Source:

The dataset was compiled using publicly available balance sheet information of Swiggy obtained from Screener.

### Dataset Scope:

The dataset includes financial variables such as:

- Equity Capital
- Reserves
- Borrowings
- Other Liabilities
- Deposits
- CWIP
- Investments
- Other Assets
- Total Assets

### Purpose

The dataset was used to explore statistical relationships between financial indicators and Total Assets through regression analysis.

## Dataset Preview



## Tools & Technologies

| Tool        | Purpose              |
| ----------- | -------------------- |
| Python      | Statistical Analysis |
| Pandas      | Data Processing      |
| Statsmodels | OLS Regression       |
| Matplotlib  | Visualization        |


## Methodology

Step 1

Collected Swiggy financial statement data.

Step 2

Prepared predictor variables and target variable.

Step 3

Applied Ordinary Least Squares (OLS) Regression.

Step 4

Estimated regression coefficients.

Step 5

Visualized coefficient magnitudes.

Step 6

Compared Actual vs Predicted values.

Step 7

Interpreted business implications.

## Core Analysis

```python
model = sm.OLS(y, X).fit()

coef = model.params.drop("const", errors="ignore")

coef = coef.sort_values()

plt.barh(coef.index, coef.values)
```

## Results

### Regression Coefficient Analysis


### Actual vs Predicted Values



## Key Findings

Deposits demonstrated one of the strongest positive coefficients within the regression model, indicating a substantial association with Total Assets.

Investments and Other Assets also exhibited strong positive contributions to the regression equation.

Equity Capital showed a negative coefficient within the observed dataset, highlighting an inverse relationship under the available observations.

The coefficient visualization provides a comparative understanding of how different financial variables contribute to Total Assets.

## Business Relevance

Regression analysis enables organizations to estimate relationships among financial variables and support evidence-based decision-making.

Understanding the relative influence of financial indicators helps analysts identify business drivers and evaluate financial structures more effectively.

This project demonstrates the practical application of statistical modeling techniques in business analytics.

## Learning Outcomes

Through this project, I strengthened my understanding of:

Multiple Linear Regression
Ordinary Least Squares (OLS)
Statistical Modeling
Regression Coefficient Interpretation
Financial Data Analysis
Business Analytics
Python for Quantitative Analysis
Project Limitation

This project is intended as an educational demonstration using a relatively small financial dataset.

The regression model illustrates statistical concepts and analytical workflows rather than providing conclusive predictive evidence. Future analyses with larger datasets would improve model robustness and generalizability.

## Future Scope

Potential extensions include:

Residual Analysis
Significance Testing using p-values
Adjusted R² Interpretation
Financial Forecasting Models
Random Forest Regression
Gradient Boosting Regression
Multi-company Comparative Analysis
Interactive Power BI Dashboards

## Conclusion

This project demonstrates how Multiple Linear Regression can be applied to financial statement data to quantify relationships among business variables.

The analysis highlights the practical role of statistical modeling in business analytics while reinforcing the importance of data quality and sample size in predictive analysis.

## About the Analyst

#### Mridul Krishna Parauha

##### BBA (Digital Marketing & AI)

###### Passionate about Business Analytics, Financial Analysis, Digital Marketing, and Generative AI, with a focus on transforming data into actionable business insights.
