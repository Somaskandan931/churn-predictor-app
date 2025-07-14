import os
import pandas as pd
import xgboost as xgb
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from joblib import dump
from pathlib import Path


def load_data(processed_data_dir):
    train_path = os.path.join(processed_data_dir, 'train_set.csv')
    test_path = os.path.join(processed_data_dir, 'test_set.csv')

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    X_train = train_df.drop('Churn', axis=1)
    y_train = train_df['Churn']
    X_test = test_df.drop('Churn', axis=1)
    y_test = test_df['Churn']

    return X_train, X_test, y_train, y_test


def train_xgboost(X_train, y_train):
    model = xgb.XGBClassifier(
        use_label_encoder=False,
        eval_metric='logloss',
        random_state=42
    )
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("📊 Classification Report:\n", classification_report(y_test, y_pred))
    print("📉 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print(f"🎯 ROC AUC Score: {roc_auc_score(y_test, y_proba):.4f}")


def save_artifacts(model, X_train, model_dir):
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, 'xgb_churn_model.joblib')
    dump(model, model_path)
    print(f"✅ Model saved to: {model_path}")

    columns_path = os.path.join(model_dir, 'train_columns.joblib')
    dump(X_train.columns.tolist(), columns_path)
    print(f"📁 Training columns saved to: {columns_path}")


if __name__ == "__main__":
    processed_data_dir = 'C:/Users/somas/PycharmProjects/OnSource_Churn_AI/data/processed'
    model_dir = 'C:/Users/somas/PycharmProjects/OnSource_Churn_AI/models'  # corrected folder name

    print("📥 Loading data...")
    X_train, X_test, y_train, y_test = load_data(processed_data_dir)

    print("🚀 Training XGBoost model...")
    model = train_xgboost(X_train, y_train)

    print("🧪 Evaluating model...")
    evaluate_model(model, X_test, y_test)

    print("💾 Saving model and training metadata...")
    save_artifacts(model, X_train, model_dir)
