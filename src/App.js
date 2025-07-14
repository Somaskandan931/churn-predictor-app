import React, { useState } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, LabelList,
} from 'recharts';

const initialForm = {
  gender: 'Female',
  SeniorCitizen: 0,
  Partner: 'Yes',
  Dependents: 'No',
  tenure: 12,
  PhoneService: 'Yes',
  MultipleLines: 'No',
  InternetService: 'Fiber optic',
  OnlineSecurity: 'No',
  OnlineBackup: 'Yes',
  DeviceProtection: 'No',
  TechSupport: 'No',
  StreamingTV: 'Yes',
  StreamingMovies: 'No',
  Contract: 'Month-to-month',
  PaperlessBilling: 'Yes',
  PaymentMethod: 'Electronic check',
  MonthlyCharges: 75.7,
  TotalCharges: 450.5,
};

const categoricalOptions = {
  gender: ['Male', 'Female'],
  Partner: ['Yes', 'No'],
  Dependents: ['Yes', 'No'],
  PhoneService: ['Yes', 'No'],
  MultipleLines: ['Yes', 'No', 'No phone service'],
  InternetService: ['DSL', 'Fiber optic', 'No'],
  OnlineSecurity: ['Yes', 'No', 'No internet service'],
  OnlineBackup: ['Yes', 'No', 'No internet service'],
  DeviceProtection: ['Yes', 'No', 'No internet service'],
  TechSupport: ['Yes', 'No', 'No internet service'],
  StreamingTV: ['Yes', 'No', 'No internet service'],
  StreamingMovies: ['Yes', 'No', 'No internet service'],
  Contract: ['Month-to-month', 'One year', 'Two year'],
  PaperlessBilling: ['Yes', 'No'],
  PaymentMethod: [
    'Electronic check',
    'Mailed check',
    'Bank transfer (automatic)',
    'Credit card (automatic)',
  ],
};

const numericFields = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges'];

function App() {
  const [formData, setFormData] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    const parsedValue = numericFields.includes(name) ? parseFloat(value) : value;
    setFormData({ ...formData, [name]: parsedValue });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Unknown server error');
      }

      setResult({
        prediction: data.prediction,
        probability: data.probability,
        explanation: data.explanation.map((e) => ({
          feature: e.feature,
          impact: parseFloat(e.impact),
        })),
      });
    } catch (err) {
      console.error('❌ Prediction Error:', err.message);
      alert('Prediction failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 700, margin: '2rem auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>📊 Customer Churn Predictor</h1>

      <form onSubmit={handleSubmit} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '2rem' }}>
        {Object.entries(formData).map(([key, value]) => (
          <div key={key} style={{ display: 'flex', flexDirection: 'column' }}>
            <label htmlFor={key} style={{ marginBottom: 4, fontWeight: 'bold' }}>{key}</label>
            {categoricalOptions[key] ? (
              <select name={key} value={value} onChange={handleChange} id={key}>
                {categoricalOptions[key].map((option) => (
                  <option key={option} value={option}>{option}</option>
                ))}
              </select>
            ) : (
              <input
                type="number"
                id={key}
                name={key}
                value={value}
                onChange={handleChange}
                step="any"
                min={key === 'SeniorCitizen' ? 0 : undefined}
              />
            )}
          </div>
        ))}

        <div style={{ gridColumn: '1 / -1', textAlign: 'center' }}>
          <button type="submit" disabled={loading} style={{ padding: '0.75rem 1.5rem', fontSize: '1.1rem' }}>
            {loading ? '⏳ Predicting...' : '🔍 Predict Churn'}
          </button>
        </div>
      </form>

      {result && (
        <div style={{ padding: '1rem', border: '1px solid #ccc', borderRadius: 6, backgroundColor: '#f9f9f9' }}>
          <h2>📈 Prediction Result</h2>
          <p>
            <strong>Prediction:</strong>{' '}
            {result.prediction === 1 ? '❌ Customer Will Churn' : '✅ Customer Will Stay'}
          </p>
          <p><strong>Probability:</strong> {(result.probability * 100).toFixed(2)}%</p>

          {result.explanation.length > 0 && (
            <>
              <h3>🧠 Top Feature Contributions</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart
                  data={result.explanation}
                  layout="vertical"
                  margin={{ top: 20, right: 30, bottom: 10, left: 120 }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis type="number" />
                  <YAxis type="category" dataKey="feature" />
                  <Tooltip />
                  <Bar dataKey="impact" fill="#8884d8">
                    <LabelList dataKey="impact" position="right" formatter={(value) => value.toFixed(3)} />
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
