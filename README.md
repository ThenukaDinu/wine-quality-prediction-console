# Wine Quality Prediction

This is a console application for predicting the quality of wine using machine learning. The application uses a Kaggle provided dataset and machine learning model that was submitted for a Kaggle competition.

## Prerequisites

- Python 3.7 or higher
- pip
- virtualenv

## Installation

1. Create a virtual environment using the following command:

   ```
   python -m venv env
   ```

2. Activate the virtual environment using the following command:

   ```
   env\Scripts\activate
   ```

3. Install the required libraries using the following command:

   ```
   python -m pip install pandas numpy tqdm scipy matplotlib seaborn plotly scikit-learn lightgbm xgboost[scikit-learn] xgboost sklearn Jinja2 catboost tabulate
   ```

## Usage

To run the application, use the following command:

```
 python app.py
```

The application provides two options:

1. Enter features
2. Import from CSV

### Option 1: Enter features

This option allows users to input all features that are needed to predict wine quality one by one and then display the prediction.

### Option 2: Import from CSV

This option allows users to provide a path to an input CSV file. The application will create a new file in the same location as the input file with the name `inputfilename-predictions.csv`. The new file will have all the columns that the input CSV had and an additional `predictions` column.

## Libraries

The following libraries are required to run the application:

- pandas
- numpy
- tqdm
- scipy
- matplotlib
- seaborn
- plotly
- scikit-learn
- lightgbm
- xgboost[scikit-learn]
- xgboost
- sklearn
- Jinja2
- catboost
- tabulate

## Acknowledgments

- Kaggle for providing the dataset and hosting the competition.
- The scikit-learn team for providing the machine learning library.
