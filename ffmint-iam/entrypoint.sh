#!/bin/sh

echo "Running prestart script..."
./prestart.sh

echo "Starting uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
