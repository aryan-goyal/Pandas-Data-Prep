<p float="left">
   <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=pythonlogoColor=white"/>
   <img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

# Snapcommerce-F2021

Snapcommerce Case Study: Data Engineer Intern - Fall 2021 Term

The solution was developed in Python using the pandas library.

The [cleanedData](https://github.com/aryan-goyal/Snapcommerce-F2021/blob/main/cleanedData) file contains the data after the transformations have been applied.

## 1. FlightCodes column

1. Null values are replaced with correct values.
2. Column type changed to int.

## 2. To_From column

1. Columns are split by underscore and added to DataFrame.
2. Columns are converted to capital case.
3. Orignal To_From column is dropped.

## 3. Airline Code column

1. Regex expression used removed everything but letters and space.
2. Leading and Trailing space trimmed.

## 4. Mock SQL Query

`SELECT * FROM cleanedData WHERE From='WATERLOO';`
