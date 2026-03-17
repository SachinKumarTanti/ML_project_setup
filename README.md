# Student Performance Prediction

A machine learning web application that predicts student math scores based on various demographic and academic factors using advanced ML models.

## 🚀 Features

- **Predictive Analytics**: Predict math scores using factors like gender, race/ethnicity, parental education, lunch type, test preparation, and reading/writing scores.
- **Multiple ML Models**: Utilizes CatBoost, Random Forest, Gradient Boosting, and other algorithms for accurate predictions.
- **Web Interface**: User-friendly Flask-based web application with responsive design.
- **Data Preprocessing**: Automated preprocessing with one-hot encoding, standard scaling, and imputation.
- **Real-time Predictions**: Instant results through an intuitive form interface.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, CatBoost, XGBoost
- **Data Processing**: pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Local Flask server

## � Documentation

- **[Technical Documentation](docs/TECHNICAL_DOCUMENTATION.md)**: Detailed technical specifications, architecture, and API reference
- **[User Documentation](docs/USER_DOCUMENTATION.md)**: Complete user guide with installation, usage, and troubleshooting

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ML/Project_setup
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**:
   ```bash
   python src/components/data_ingestion.py
   ```
   This will process the data, train the models, and save the best model and preprocessor.

## 🚀 Usage

1. **Run the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to `http://127.0.0.1:5000/`

3. **Navigate the app**:
   - **Home**: Landing page with project overview
   - **Predict**: Fill out the prediction form with student details
   - Submit to get the predicted math score

## 📁 Project Structure

```
ML_Project_setup/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── test.py                         # Test file
│
├── artifacts/                      # Trained models and data
│   ├── model.pkl                   # Best trained model
│   ├── preprocessor.pkl            # Data preprocessor
│   ├── train.csv                   # Training data
│   ├── test.csv                    # Test data
│   └── data.csv                    # Raw data
│
├── src/                            # Source code
│   ├── __init__.py
│   ├── execption.py                # Custom exceptions
│   ├── logger.py                   # Logging utilities
│   ├── utils.py                    # Utility functions
│   │
│   ├── components/                 # ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py       # Data loading and splitting
│   │   ├── data_transformation.py  # Data preprocessing
│   │   └── model_trainer.py        # Model training and evaluation
│   │
│   └── pipelines/                  # Prediction pipelines
│       ├── __init__.py
│       ├── predict_pipeline.py     # Prediction logic
│       └── train_pipeline.py       # Training pipeline
│
├── templates/                      # HTML templates
│   ├── index.html                  # Landing page
│   └── home.html                   # Prediction form
│
├── notebook/                       # Jupyter notebooks
│   └── process.ipynb               # Data exploration notebook
│
├── logs/                           # Application logs
├── catboost_info/                  # CatBoost training info
└── ml_project.egg-info/            # Package info
```

## 🎯 How It Works

1. **Data Ingestion**: Loads student performance data from CSV
2. **Data Transformation**: Preprocesses features using ColumnTransformer with scaling and encoding
3. **Model Training**: Trains multiple ML models and selects the best performing one
4. **Prediction**: Takes user input, preprocesses it, and predicts math score using the trained model

## 📊 Model Performance

The application evaluates multiple models and selects the best one based on R² score (>0.6 threshold). Supported models include:
- CatBoost Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- Linear Regression
- And more...

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

**Note**: This project is for educational purposes demonstrating ML model deployment with Flask.