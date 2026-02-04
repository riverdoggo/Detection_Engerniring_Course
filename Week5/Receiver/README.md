# Receiver System

## Architecture
alerts -> main.py -> dedupe -> storage -> sqlite

## Storage
SQLite chosen for simplicity and persistence.

## Deduplication
MD5 hash of rule + host with 5 minute window.

## Limitations
Single node only.
No authentication.
High volume may require queue system.

## Scaling Concerns
Database write contention and memory cache size.
