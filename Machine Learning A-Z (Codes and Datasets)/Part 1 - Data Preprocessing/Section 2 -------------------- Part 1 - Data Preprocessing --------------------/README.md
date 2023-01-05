## Import Libraries
## Import the data
## Missing Values
### Imputation

e.g. **Univariate feature imputation**:
 
    sklearn.impute.SimpleImputer
    1. mean
    2. median
    3. most_frequent
    4. constant

e.g. **Multivariate feature imputation**:

    sklearn.experimental.enable_iterative_imputer
    sklearn.impute.IterativeImputater
    
    A more sophisticated approach is to use the IterativeImputer class, which models each feature with missing values as a function of other features, and uses that estimate for imputation. It does so in an iterated round-robin fashion: at each step, a feature column is designated as output y and the other feature columns are treated as inputs X. A regressor is fit on (X, y) for known y. Then, the regressor is used to predict the missing values of y. This is done for each feature in an iterative fashion, and then is repeated for max_iter imputation rounds. The results of the final imputation round are returned.

## Categorical variable:

**Solution**: Create dummies:

    e.g. sklearn.compose.ColumTransformer
         
        sklearn.preprocessing.OneHotEncoder

        ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')

        
        from sklearn.preprocessing import LabelEncoder

## Split the test set and training set

We split the test set and training set before feature scaling to prevent the data leackage or additional information that we can obtain from the test set, which was supposed to be missing in real life applications.     


        e.g. sklearn.model_selection.train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)



## Feature Scaling

### Normalization 

```math
    X' = \frac{X - X_{min}}{X_{max} - X_{min}}
```

### Standardization:

```math
    X' = \frac{X - \mu}{\sigma}
```
