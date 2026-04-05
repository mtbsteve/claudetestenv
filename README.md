# Claude Workspace

A collection of tools and documents for energy consultant training (Energieberaterschulung).

## Tibber Live (`tibber_live.py`)

Real-time energy measurement viewer that connects to the Tibber GraphQL API via WebSocket and streams live data from Tibber Pulse/Watty devices.

### Features

- Side-by-side display for multiple homes
- Live power consumption and production metrics
- Quarter-hourly electricity pricing (EPEX Spot)
- Min, average, and max price of the day
- Accumulated consumption, cost, and production
- Auto-reconnect on connection loss

### Requirements

- Python 3.10+
- `requests`, `websockets` (see `requirements.txt`)
- A Tibber API token (get one at https://developer.tibber.com/)

### Usage

```bash
export TIBBER_TOKEN="your-token-here"
python tibber_live.py
```

## Documents

- **Etagenheizung ergebnis.docx** — Floor heating system analysis
- **Luft_Wasser_Waermepumpen.docx** — Air-water heat pump documentation
- **Transkript_Heizungstausch_Mehrfamilienhaus.docx** — Heating replacement transcript for multi-family buildings
