import React, { useEffect, useState } from 'react';
import SpaceWeatherTile from './components/SpaceWeatherTile';
import SpaceWeatherTrendline from './components/SpaceWeatherTrendline';

function App() {
  const [spaceWeatherData, setSpaceWeatherData] = useState(null);
  const [trendData, setTrendData] = useState([]);

  useEffect(() => {
    fetch('/api/space-weather')
      .then(res => res.json())
      .then(data => setSpaceWeatherData(data.data));

    fetch('/api/space-weather/trend')
      .then(res => res.json())
      .then(data => setTrendData(data));
  }, []);

  return (
    <div className="dashboard">
      {spaceWeatherData && <SpaceWeatherTile data={spaceWeatherData} />}
      {trendData.length > 0 && <SpaceWeatherTrendline data={trendData} />}
      {/* Other tiles */}
    </div>
  );
}

export default App;
