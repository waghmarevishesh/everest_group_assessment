@echo off
pipenv run uvicorn server:app --reload --log-level debug