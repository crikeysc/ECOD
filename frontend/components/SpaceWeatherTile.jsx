// frontend/components/SpaceWeatherTile.jsx
import React from 'react';
import './TileStyles.css'; // Optional: shared styling

const alertColors = {
  quiet: '#4CAF50',
  active: '#FFC107',
  storm: '#FF5722',
  'severe storm': '#D32F2F'
};

export default function SpaceWeatherTile({ data }) {
  const { kp_index, kp_alert, source_timestamp } = data;

  return (
    <div className="tile space-weather-tile" style={{ borderColor: alertColors[kp_alert] }}>
      <h3>Space Weather: Kp Index</h3>
      <div className="kp-value">{kp_index}</div>
      <div className="kp-alert" style={{ color: alertColors[kp_alert] }}>
        {kp_alert.toUpperCase()}
      </div>
      <div className="tile-meta">Updated: {new Date(source_timestamp).toLocaleString()}</div>
    </div>
  );
}
