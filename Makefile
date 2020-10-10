SHELL := /bin/bash

init-venv:
	python3 -m venv venv

install-dep:
	source venv/bin/activate && pip install -r requirements.txt

check-lint-format-all:
	source venv/bin/activate && black --check -t py38 maker_drive.py maker_drive_remote.py
	source venv/bin/activate && flake8 maker_drive.py maker_drive_remote.py

run:
	source venv/bin/activate && black --check -t py38 maker_drive.py maker_drive_remote.py

