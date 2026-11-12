# 🎓 Student Performance Predictor

An AI/ML-based web application that predicts students' final examination scores based on their study hours, attendance, previous academic performance, and sleep hours.

The project uses **Machine Learning (Linear Regression)** to learn patterns from student data and estimate academic performance.

## 🚀 Features

- Predicts students' expected final examination marks.
- Takes study hours as input.
- Considers attendance percentage.
- Uses previous examination scores.
- Considers daily sleep hours.
- Displays predicted marks instantly.
- Categorizes performance as Excellent, Good, Average, or Needs Improvement.
- Simple and interactive web interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data visualization |
| Streamlit | Web application |
| Joblib | Saving and loading the trained model |

## 🧠 Machine Learning Algorithm

**Linear Regression**

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

In this project:

**Input Features:**
- Study Hours
- Attendance
- Previous Score
- Sleep Hours

**Target Variable:**
- Final Score

The dataset is divided into:
- 80% Training Data
- 20% Testing Data

The model learns from the training data and is evaluated using Mean Absolute Error (MAE) and R² Score.

## 📂 Project Structure

```text
prediction/
│
├── venv/
│
├── dataset.csv
├── inspect_data.py
├── train_model.py
├── model.pkl
├── app.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install pandas numpy scikit-learn matplotlib streamlit joblib
```

## ▶️ How to Run

### Step 1: Inspect the dataset

```bash
python inspect_data.py
```

### Step 2: Train the machine learning model

```bash
python train_model.py
```

This creates the trained model file:

```text
model.pkl
```

### Step 3: Launch the web application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📊 Example Input

| Parameter | Value |
|---|---:|
| Study Hours | 5 |
| Attendance | 80% |
| Previous Score | 70 |
| Sleep Hours | 7 |

The application generates an estimated final examination score based on the trained model.

## 🔮 Future Enhancements

- Add more student records for better model training.
- Compare different machine learning algorithms.
- Improve prediction accuracy using real-world datasets.
- Add interactive performance analysis graphs.
- Store student prediction history.
- Deploy the application online.

## ⚠️ Disclaimer

This project uses a small synthetic dataset created for educational purposes. Predictions are experimental estimates and should not be used for actual academic decisions.

## 👩‍💻 Author

**Nandhana TS**

B.Tech Computer Science and Engineering

## 📄 License

This project is developed for educational and learning purposes.
