import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, RobustScaler, StandardScaler


# == prepare data
class selectColumnTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer to select columns
    """
    def __init__(self, columns):
        self.columns = columns
    
    def transform(self, X):
        return X[self.columns]
    
    def fit(self, X, y=None):
        return self


class dropAllZeroColumnTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer to drop all-zero columns
    """
    def transform(self, X):
        empty_columns = X.columns[X.isnull().all(axis=0)]
        return X.drop(empty_columns, axis=1)
        
    def fit(self, X, y=None):
        return self

    
class dropUselessColumnsTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer to drop useless columns
    """
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X):
        return X.drop(self.columns, axis=1)
        
    def fit(self, X, y=None):
        return self


class categoryAddFeatureTransformer(BaseEstimator, TransformerMixin):
    """
    generate more features from category variables
    """
    def transform(self, X):
        return X.fillna('unknown')

    def fit(self, X, y=None):
        return self




def build_preparation_pipeline():
  outlier_attribs = ['odometer']
  num_attribs = ['lat', 'long', 'year']
  cat_attribs = [
      'manufacturer', 'condition', 'cylinders', 
      'fuel', 'title_status', 'transmission', 
      'drive', 'type', 'paint_color'  
  ]
  useless_columns = [
      # irrelevant
      'id', 'url', 'region_url', 'image_url', 'posting_date', 'description',
      # too many missing values
      'VIN', 'size',
      # repeative or not much useful
      'region', 'state', 'model'
  ] 

  outlier_pipeline = Pipeline([
      ('imputed', SimpleImputer(strategy='median')),
      ('outlier', RobustScaler())
  ])
  num_pipeline = Pipeline([
      ('imputed', SimpleImputer(strategy='median')),
      ('std_scaler', StandardScaler())
  ])
  cat_pipeline = Pipeline([  
      ('add_feature', categoryAddFeatureTransformer()),
      ('one_hot', OneHotEncoder())
  ])

  # full pipeline
  full_pipeline = make_pipeline(
      dropAllZeroColumnTransformer(),
      dropUselessColumnsTransformer(useless_columns),
      ColumnTransformer([
          ('outlier', outlier_pipeline, outlier_attribs),
          ('num', num_pipeline, num_attribs),
          ('cat', cat_pipeline, cat_attribs)
      ])
  )

  return full_pipeline




# == clean data 
def cutIQR(df, col, q1=0.25, q2=0.75):
    Q1 = df[col].quantile(q1)
    Q3 = df[col].quantile(q2)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    cutted_df = df[(df[col] >= lower) & (df[col] <= upper)]

    return cutted_df

def clean_data(df_vehicles):
    # step1: missing values
    # for others, simply impute with unknown or generated from other features
    cleaned_df = df_vehicles.dropna(subset=['year'])

    # step2: remove extreme outlier
    cleaned_df = cutIQR(cleaned_df, 'price', q2=0.85)
    
    cleaned_df = cleaned_df[cleaned_df['odometer'] <= 10000000]
    cleaned_df = cutIQR(cleaned_df, 'odometer', q2=0.85)

    return cleaned_df
