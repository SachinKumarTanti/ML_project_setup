# User Documentation

## Welcome to Student Performance Prediction

This guide will help you understand and use the Student Performance Prediction web application, which predicts student mathematics scores based on various academic and demographic factors.

## What is This Application?

The Student Performance Prediction app uses machine learning to estimate a student's mathematics test score based on:
- Personal information (gender, race/ethnicity)
- Family background (parental education level)
- School factors (lunch type, test preparation)
- Academic performance (reading and writing scores)

## Getting Started

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.8 or higher
- **Web Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **RAM**: At least 4GB recommended
- **Storage**: 500MB free space

### Installation

#### Step 1: Download the Project
```bash
git clone <repository-url>
cd ML/Project_setup
```

#### Step 2: Set Up Python Environment
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Train the Model
```bash
python src/components/data_ingestion.py
```
This step processes the data and trains the machine learning models. It may take a few minutes.

## Using the Application

### Starting the Application
```bash
python app.py
```

Open your web browser and go to: `http://127.0.0.1:5000/`

### Navigation

#### Home Page
- **Welcome Message**: Overview of the application
- **Features**: Key capabilities of the system
- **About**: Detailed information about the project
- **Predict Button**: Navigate to the prediction form

#### Prediction Page
- **Form Fields**: Input student information
- **Submit Button**: Generate prediction
- **Results**: Display predicted math score
- **Back to Home**: Return to the main page

## Making Predictions

### Step-by-Step Guide

1. **Access the Prediction Form**
   - Click "Predict" on the home page or visit `/predict_data`

2. **Fill Out the Form**
   Complete all required fields:

   - **Gender**: Select "Male" or "Female"
   - **Race/Ethnicity**: Choose from Group A through E
   - **Parental Level of Education**:
     - Some High School
     - High School
     - Some College
     - Associate's Degree
     - Bachelor's Degree
     - Master's Degree
   - **Lunch Type**:
     - Standard (paid lunch)
     - Free/Reduced (subsidized lunch)
   - **Test Preparation Course**:
     - None
     - Completed
   - **Reading Score**: Enter score 0-100
   - **Writing Score**: Enter score 0-100

3. **Submit the Form**
   - Click "Predict Math Score"
   - Wait for processing (usually instant)

4. **View Results**
   - Predicted math score appears below the form
   - Score is displayed prominently

### Input Validation

The application validates your inputs:
- All fields are required
- Reading and writing scores must be 0-100
- Invalid selections will prevent submission

### Understanding Results

- **Predicted Score**: Estimated mathematics test score
- **Range**: Typically 0-100 (may vary based on model)
- **Accuracy**: Based on historical data patterns
- **Interpretation**: Higher scores indicate better predicted performance

## Features and Functionality

### Responsive Design
- Works on desktop, tablet, and mobile devices
- Automatically adjusts layout for different screen sizes

### Real-time Processing
- Instant predictions (no waiting)
- Results appear immediately after submission

### Error Handling
- Clear error messages for invalid inputs
- Automatic recovery from common issues
- User-friendly error pages

### Data Privacy
- All processing happens locally
- No data is sent to external servers
- Input data is not stored permanently

## Troubleshooting

### Common Issues

#### Application Won't Start
**Problem**: `python app.py` fails
**Solutions**:
- Ensure Python 3.8+ is installed
- Check virtual environment is activated
- Verify all dependencies are installed
- Check for port conflicts (default port 5000)

#### Model Training Fails
**Problem**: `data_ingestion.py` errors out
**Solutions**:
- Ensure data file exists: `notebook/data/student.csv`
- Check file permissions
- Verify sufficient RAM (4GB+ recommended)
- Check Python dependencies

#### Prediction Errors
**Problem**: Form submission fails or shows errors
**Solutions**:
- Verify all form fields are filled
- Check score ranges (0-100)
- Ensure model files exist in `artifacts/`
- Try refreshing the page

#### Page Loads Slowly
**Problem**: Application is slow
**Solutions**:
- Close other applications to free RAM
- Ensure sufficient free disk space
- Check internet connection (for font loading)
- Restart the application

### Error Messages

#### "This ColumnTransformer instance is not fitted yet"
- **Cause**: Model training incomplete
- **Solution**: Re-run `python src/components/data_ingestion.py`

#### "File not found" errors
- **Cause**: Missing model or data files
- **Solution**: Check `artifacts/` directory contents

#### "Invalid input" messages
- **Cause**: Form validation failed
- **Solution**: Check all fields are properly filled

## Advanced Usage

### Understanding the Model

The application uses multiple machine learning algorithms:
- **CatBoost**: Primary model (gradient boosting)
- **Random Forest**: Ensemble method
- **XGBoost**: Extreme gradient boosting
- **Linear Models**: Ridge, Lasso regression

The system automatically selects the best performing model based on accuracy metrics.

### Data Insights

The predictions are based on patterns from historical student data including:
- 1,000+ student records
- Multiple demographic factors
- Academic performance metrics
- School environment variables

### Performance Metrics

- **Accuracy**: R² score > 0.6 (industry standard)
- **Processing Time**: < 1 second per prediction
- **Model Size**: ~50MB (compressed)

## Frequently Asked Questions (FAQ)

### Q: How accurate are the predictions?
A: The model achieves over 60% accuracy (R² score) on test data. Real-world accuracy may vary based on individual circumstances.

### Q: Can I use this for actual student assessment?
A: This is an educational tool for demonstration purposes. It should not be used for official academic decisions.

### Q: How does the model work?
A: The system analyzes patterns in historical data to find correlations between input factors and math scores, then applies these patterns to new data.

### Q: Is my data stored or shared?
A: No. All processing happens locally on your computer. Input data is not saved or transmitted.

### Q: Can I modify the model?
A: Yes, the source code is available. You can retrain with new data or adjust parameters.

### Q: What if I get different results for the same input?
A: The model uses stochastic elements. Minor variations are normal but results should be consistent.

### Q: Does it work offline?
A: Yes, once trained, the application works completely offline.

## Support and Resources

### Getting Help
- Check this documentation first
- Review error messages carefully
- Ensure all prerequisites are met

### Additional Resources
- **README.md**: Project overview and setup
- **Source Code**: Located in `src/` directory
- **Data**: Sample data in `notebook/data/`
- **Logs**: Check `logs/` for detailed error information

### Reporting Issues
If you encounter problems:
1. Note the exact error message
2. Check the logs in `logs/` directory
3. Verify your setup matches requirements
4. Include your Python version and OS

## Version Information

- **Current Version**: 1.0.0
- **Python Version**: 3.8+
- **Flask Version**: 2.x
- **ML Libraries**: scikit-learn, CatBoost, XGBoost

## License and Terms

This project is provided for educational purposes. See LICENSE file for full terms.

---

Thank you for using the Student Performance Prediction application! We hope it provides valuable insights into machine learning applications in education.