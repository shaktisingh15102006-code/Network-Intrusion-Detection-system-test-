#🚨 Network Intrusion Detection System (NIDS)
An end-to-end Machine Learning project that detects whether network traffic is Normal or Malicious (Attack) using the NSL-KDD dataset, and provides real-time predictions through a Streamlit web application.

📌 Project Overview
With the rapid growth of cyber threats, detecting malicious network activity has become essential. This project builds a Network Intrusion Detection System (NIDS) that classifies network connections into:

✅ Normal Traffic
🚨 Attack Traffic
The model is trained on historical network data and deployed using Streamlit for interactive predictions.

🎯 Objectives
Analyze network traffic dataset
Identify patterns of cyber attacks
Build a classification model
Deploy an interactive web application
Provide real-time intrusion detection
📂 Dataset Information
Dataset: NSL-KDD (KDDTrain+)
Type: Tabular dataset for intrusion detection
Total Features: 41 + 2 labels
🔑 Important Features:
protocol_type
service
flag
src_bytes, dst_bytes
count, srv_count
Error rates (serror_rate, rerror_rate, etc.)
⚙️ Tech Stack
👨‍💻 Programming & Libraries
Python 🐍
Pandas, NumPy
Matplotlib, Seaborn
🤖 Machine Learning
Scikit-learn
XGBoost
🌐 Deployment
Streamlit
🔄 Project Workflow
Data Collection

Load NSL-KDD dataset
Data Preprocessing

Handle missing values
Convert categorical → numerical (Label Encoding)
Feature scaling (StandardScaler)
Exploratory Data Analysis (EDA)

Distribution plots
Attack analysis
Feature relationships
Feature Selection

Mutual Information
Select top important features
Model Building

Logistic Regression
XGBoost (final model)
Model Evaluation

Accuracy, Precision, Recall, F1-score
ROC-AUC Score
Hyperparameter Tuning

GridSearchCV on XGBoost
Deployment

Streamlit web app for real-time prediction
🧠 Model Performance
Metric	Value (Approx)
Accuracy	High
Precision	High
Recall	High
F1 Score	High
ROC-AUC	Excellent
✅ XGBoost performed better than Logistic Regression.

🖥️ App Preview
Below is the interface of the NIDS Streamlit App:

App Preview

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/shaktisingh15102006/Network-Intrusion-Detection-System.git
cd Network-Intrusion-Detection-System
2️⃣ Install Requirements
pip install -r requirements.txt
3️⃣ Run Streamlit App
streamlit run network_app.py
📁 Project Structure
NIDS_Project/
│── network_app.py        # Streamlit Application
│── KDDTrain+.txt         # Dataset
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── app_preview.png       # App Screenshot
│     
⚠️ Common Errors & Solutions
❌ ValueError: could not convert string to float
✔ Fix:

pd.read_csv("KDDTrain+.txt", sep=r'\t', engine='python', header=None)
❌ KeyError: 'attack'
✔ Fix:

Assign column names before using:
df.columns = columns
❌ Streamlit not running
✔ Fix:

pip install streamlit
📌 Future Enhancements
Multi-class attack classification
Real-time network traffic integration
Model saving (joblib/pickle)
Deployment on Streamlit Cloud / AWS
Add dashboard analytics
🙌 Author
shakti singh🎓 Data Science Student

📬 Contact
GitHub: https://github.com/shaktisingh15102006
Email: shakti singh
⭐ Support
If you found this project helpful:

👉 Give it a ⭐ on GitHub 👉 Share with others
