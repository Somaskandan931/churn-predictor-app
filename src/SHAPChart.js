import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, LabelList } from 'recharts';

const SHAPChart = ({ data }) => {
  const formattedData = data.map(item => ({
    ...item,
    impact: parseFloat(item.impact),
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart
        data={formattedData}
        layout="vertical"
        margin={{ top: 10, right: 20, bottom: 10, left: 100 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis type="number" label={{ value: "Impact", position: "insideBottomRight", offset: 0 }} />
        <YAxis type="category" dataKey="feature" />
        <Tooltip />
        <Bar dataKey="impact" fill="#8884d8">
          <LabelList dataKey="impact" position="right" />
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
};

export default SHAPChart;
