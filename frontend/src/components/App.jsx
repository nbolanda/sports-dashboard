import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/recommended_props/nba")
      .then(res => setRecommendations(res.data.recommendations));
  }, []);

  return (
    <div>
      <h1>Top Prop Picks</h1>
      {recommendations.map((rec, i) => (
        <div key={i}>
          {rec.player} - {rec.stat}: {rec.pick} than {rec.line} (avg: {rec.average})
        </div>
      ))}
    </div>
  );
}

export default Dashboard;
