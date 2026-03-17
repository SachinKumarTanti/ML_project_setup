from flask import Flask, render_template, request

from src.pipelines.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_data', methods=['GET', 'POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form['gender'],
            race_ethnicity=request.form['race_ethnicity'],
            parental_level_of_education=request.form['parental_level_of_education'],
            lunch=request.form['lunch'],
            test_preparation_course=request.form['test_preparation_course'],
            reading_score=int(request.form['reading_score']),
            writing_score=int(request.form['writing_score'])
        )
        pred_df = data.get_data_as_dataframe()


        pipeline = PredictPipeline()
        prediction = pipeline.predict(pred_df)
        return render_template('home.html', prediction=prediction[0])
    
if __name__ == '__main__':
    app.run(debug=False)