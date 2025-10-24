ECOD/
├── backend/
│   ├── app.py
│   ├── api/
│   │   ├── routes.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── topic_engine.py
│   │   ├── moderation.py
│   │   ├── redis_telemetry.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── redis_client.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── README.md
│
├── frontend/
│   ├── components/
│   │   ├── SpaceWeatherTile.jsx
│   │   ├── SpaceWeatherTrendLine.jsx
│   │   └── __init__.js
│   ├── App.jsx
│   ├── styles/
│   │   └── TileStyles.css
│   └── README.md
│
├── tests/
│   ├── test_redis.py
│   ├── test_topic_engine.py
│   ├── fixtures/
│   │   └── Space_Weather_Tile.json
│   └── README.md
│
├── docs/
│   └── README_ECOD.md
│
└── __pycache__/   # ignored in .gitignore
