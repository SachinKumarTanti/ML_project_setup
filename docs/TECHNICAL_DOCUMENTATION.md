# Technical Documentation

## Architecture Overview

The Student Performance Prediction system is a Flask-based web application that implements a machine learning pipeline for predicting student math scores. The architecture follows a modular design with clear separation of concerns.

### System Components

#### 1. Web Layer (Flask Application)
- **app.py**: Main application entry point
- **Routes**:
  - `GET /`: Landing page (index.html)
  - `GET/POST /predict_data`: Prediction form and result page (home.html)

#### 2. Machine Learning Pipeline
Located in `src/` directory with the following components:

##### Data Ingestion (`data_ingestion.py`)
- **Purpose**: Load and split raw data into train/test sets
- **Input**: CSV file from `notebook/data/student.csv`
- **Output**: Train and test CSV files in `artifacts/`
- **Key Functions**:
  - `initiate_data_ingestion()`: Main data loading method

##### Data Transformation (`data_transformation.py`)
- **Purpose**: Preprocess and transform data for ML models
- **Components**:
  - Numerical Pipeline: SimpleImputer (median) + StandardScaler
  - Categorical Pipeline: SimpleImputer (most_frequent) + OneHotEncoder + StandardScaler
- **ColumnTransformer**: Combines numerical and categorical pipelines
- **Key Functions**:
  - `get_data_transformer_object()`: Creates preprocessing pipeline
  - `initiate_data_transformation()`: Applies transformation and saves fitted preprocessor

##### Model Training (`model_trainer.py`)
- **Purpose**: Train and evaluate multiple ML models, select best performer
- **Supported Models**:
  - CatBoostRegressor
  - RandomForestRegressor
  - GradientBoostingRegressor
  - AdaBoostRegressor
  - ExtraTreesRegressor
  - HistGradientBoostingRegressor
  - LinearRegression
  - Ridge, Lasso, ElasticNet
  - DecisionTreeRegressor
  - XGBRegressor
- **Evaluation**: R² score with 0.6 threshold
- **Key Functions**:
  - `evaluate_models()`: Cross-validation and scoring
  - `initiate_model_trainer()`: Model training and selection

##### Prediction Pipeline (`predict_pipeline.py`)
- **Purpose**: Load trained model and make predictions
- **Components**:
  - `PredictPipeline`: Main prediction class
  - `CustomData`: Data validation and DataFrame creation
- **Key Functions**:
  - `predict()`: Load model/preprocessor, transform input, predict

#### 3. Utilities and Support
- **logger.py**: Logging configuration
- **exception.py**: Custom exception handling
- **utils.py**: Helper functions (load_object, save_object, evaluate_models)

## Data Flow

### Training Phase
1. **Data Ingestion**: Load CSV → Split into train/test → Save to artifacts/
2. **Data Transformation**: Fit preprocessor on training data → Transform train/test → Save fitted preprocessor
3. **Model Training**: Train multiple models → Evaluate → Select best → Save model

### Prediction Phase
1. **Input Validation**: Collect form data → Create CustomData object → Convert to DataFrame
2. **Preprocessing**: Load fitted preprocessor → Transform input data
3. **Prediction**: Load trained model → Predict → Return result

## API Reference

### Flask Routes

#### GET /
- **Description**: Landing page
- **Response**: Renders index.html
- **Status**: 200 OK

#### GET /predict_data
- **Description**: Prediction form
- **Response**: Renders home.html
- **Status**: 200 OK

#### POST /predict_data
- **Description**: Process prediction request
- **Request Body**: Form data with student information
- **Required Fields**:
  - gender (str)
  - race_ethnicity (str)
  - parental_level_of_education (str)
  - lunch (str)
  - test_preparation_course (str)
  - reading_score (int, 0-100)
  - writing_score (int, 0-100)
- **Response**: Renders home.html with prediction result
- **Status**: 200 OK on success, 500 on error

## Data Schema

### Input Features
| Feature | Type | Description | Possible Values |
|---------|------|-------------|-----------------|
| gender | string | Student gender | "male", "female" |
| race_ethnicity | string | Racial/ethnic group | "group A", "group B", "group C", "group D", "group E" |
| parental_level_of_education | string | Parent's education level | "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree" |
| lunch | string | Lunch type | "standard", "free/reduced" |
| test_preparation_course | string | Test prep completion | "none", "completed" |
| reading_score | int | Reading test score | 0-100 |
| writing_score | int | Writing test score | 0-100 |

### Output
- **math_score**: Predicted mathematics test score (float)

## Dependencies

### Core Dependencies
- **flask**: Web framework
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: ML algorithms and preprocessing
- **catboost**: Gradient boosting library
- **xgboost**: Extreme gradient boosting

### Development Dependencies
- **python-dotenv**: Environment variables (if used)

## Configuration

### File Paths
- **Model Path**: `artifacts/model.pkl`
- **Preprocessor Path**: `artifacts/preprocessor.pkl`
- **Data Paths**: `artifacts/train.csv`, `artifacts/test.csv`

### Model Parameters
Defined in `model_trainer.py` under `params` dictionary for each model type.

## Error Handling

### Custom Exceptions
- **CustomException**: Wraps all exceptions with file, line, and error message
- Logged using the custom logger
- Returns user-friendly error pages

### Validation
- Form validation on frontend (required fields, number ranges)
- Data validation in CustomData class
- Model validation (R² > 0.6 threshold)

## Performance Considerations

### Model Selection
- Cross-validation with 3 folds
- R² score evaluation
- Automatic best model selection

### Preprocessing
- Handles missing values appropriately
- Scales numerical features
- Encodes categorical features

### Prediction Speed
- Pre-trained models loaded from disk
- Efficient preprocessing pipeline
- Fast inference for real-time predictions

## Security Considerations

### Input Validation
- Server-side validation of all inputs
- Type checking and range validation
- Sanitization of user inputs

### File Security
- Model files stored securely
- No direct file access from web
- Safe loading of pickled objects

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
- Use WSGI server (gunicorn)
- Set debug=False
- Configure proper logging
- Use environment variables for sensitive data

## Testing

### Unit Tests
- Located in `test.py`
- Test individual components
- Mock external dependencies

### Integration Tests
- Test full pipeline
- Validate end-to-end functionality

## Monitoring and Logging

### Logging
- Custom logger in `logger.py`
- Logs to `logs/` directory
- Different log levels (INFO, ERROR, DEBUG)

### Performance Monitoring
- Model performance metrics
- Prediction latency tracking
- Error rate monitoring

## Future Enhancements

### Potential Improvements
- API versioning
- Authentication and authorization
- Batch prediction endpoints
- Model retraining pipeline
- Advanced feature engineering
- Model explainability (SHAP values)
- Containerization (Docker)
- CI/CD pipeline