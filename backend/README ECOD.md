# 🧠 Ephemeral Chat-Overlay Dashboard (ECOD)

## Overview

ECOD is the audience-facing layer of the GEFL system, transforming telemetry alerts into ephemeral, community-driven discussions. It enables real-time interpretation of crypto, seismic, and CME events through modular threads, ML-powered moderation, and CASA-style traceability.

## 🔗 Strategic Purpose

- **Ephemerality**: Time-bound threads keep the dashboard fresh and relevant.
- **Traceability**: Every comment and moderation action is logged for auditability.
- **Modularity**: Each alert type spawns its own thread with TTL.
- **Moderation**: ML filters ensure constructive dialogue.
- **Engagement**: Users contribute insights, reactions, and overlays.

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
