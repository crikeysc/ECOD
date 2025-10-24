// frontend/components/SpaceWeatherTrendline.jsx
import React from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

export default function SpaceWeatherTrendline({ data }) {
  if (!data || data.length === 0) return <div>No trend data available</div>;

  const chartData = {
    labels: data.map(entry => new Date(entry.timestamp_utc).toLocaleTimeString()),
    datasets: [
      {
        label: 'Kp Index',
        data: data.map(entry => entry.kp_index),
        borderColor: '#FF5722',
        backgroundColor: 'rgba(255, 87, 34, 0.2)',
        tension: 0.3,
        fill: true,
        pointRadius: 2
      }
    ]
  };

  const options = {
    scales: {
      y: {
        min: 0,
        max: 9,
        title: {
          display: true,
          text: 'Kp Index'
        }
      },
      x: {
        title: {
          display: true,
          text: 'Time (UTC)'
        }
      }
    },
    plugins: {
      legend: { display: false },
      tooltip: { mode: 'index', intersect: false }
    },
    responsive: true,
    maintainAspectRatio: false
  };

  return (
    <div style={{ height: '200px', width: '100%' }}>
      <Line data={chartData} options={options} />
    </div>
  );
}
