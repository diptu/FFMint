#!/bin/sh

echo "Running database migrations (example)..."
# e.g. alembic upgrade head
alembic upgrade head

echo "Prestart script done."
