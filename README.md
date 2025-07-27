# Churn Predictor App

A full-stack machine learning web application for predicting customer churn using **XGBoost** and **SHAP** explainability. Built with **React** (frontend) and **Flask** (backend), the app takes customer details and returns churn probability, prediction, and top contributing features visualized using SHAP values.

---


## Features

* Predict customer churn probability based on input details
* Binary churn prediction (Churn / No Churn)
* Explainability with SHAP values highlighting feature contributions
* Interactive frontend with React for smooth user experience
* Backend API powered by Flask serving ML model and SHAP explanations
* Clean and modular codebase for easy customization and extension

---

## Tech Stack

* **Frontend:** React, Axios, Chart.js 
* **Backend:** Flask, Flask-RESTful
* **Machine Learning:** Python, XGBoost, SHAP
* **Data Processing:** pandas, numpy
* **Visualization:** SHAP, matplotlib (server-side), or frontend visualization library

---

## Installation

### Backend Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/Somaskandan931/churn-predictor-app.git
   cd churn-predictor-app/backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Place your trained model file (e.g., `xgb_model.pkl`) in the backend directory.

5. Start the Flask backend server:

   ```bash
   flask run
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install frontend dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

4. The app will open on `http://localhost:3000` by default.

---

## Usage

* Open the frontend app in your browser.
* Fill in the customer details form.
* Submit to receive churn probability, prediction label, and a SHAP feature importance visualization.
* Use these insights to guide customer retention strategies.

---

## Model

* **Algorithm:** XGBoost classifier
* **Input Features:** (List key features, e.g., tenure, monthly charges, contract type, etc.)
* **Output:** Probability of churn (0-1) and binary prediction
* **Explainability:** SHAP values calculated per prediction to highlight feature impact

---

## Project Structure

```
churn-predictor-app/
│
├── backend/
│   ├── app.py           # Flask API server
│   ├── model.pkl        # Trained XGBoost model
│   ├── shap_utils.py    # SHAP explanation helper functions
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/  # React components (form, charts, etc.)
│   │   ├── App.js
│   │   └── ...
│   ├── package.json
│   └── ...
│
└── README.md
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

