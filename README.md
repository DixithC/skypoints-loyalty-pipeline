# SkyPoints Loyalty Pipeline

A daily data pipeline for the SkyPoints airline loyalty program. It loads a pipe-delimited
member file and a semi-structured JSON redemption feed, validates them, and splits members
into per-country tables (latest record wins when a member changes country).

**Stack:** Python 3.11+, DuckDB, SQL, pytest, ruff.

## Documentation

- [Architecture and design decisions](docs/ARCHITECTURE.md)

## Development

```
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
```

## Status

Work in progress. See the build roadmap in the architecture doc.