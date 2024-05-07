#!/bin/bash
# Script to run all Django PyTest tests

echo "Current working directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Django settings module: $DJANGO_SETTINGS_MODULE"

echo "Setting Django settings module..."
export DJANGO_SETTINGS_MODULE=news_portal.settings
echo "Django settings module set to: $DJANGO_SETTINGS_MODULE"

echo "Running PyTest for model tests..."
pytest news_app/tests/test_models.py --html=report_models.html

echo "Running PyTest for view tests..."
pytest news_app/tests/test_views.py --html=report_views.html

echo "Tests completed."
