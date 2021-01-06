SHELL=/usr/bin/bash
PIGPIO_ADDR=tank.local

init-venv:
	python -m venv venv

save-dep:
	source venv/bin/activate && pip freeze > requirements.txt

install-dep:
	source venv/bin/activate && pip install -r requirements.txt

format:
	source venv/bin/activate && black -t py38 *.py

lint:
	source venv/bin/activate && flake8 *.py

run:
	if [ -x venv/bin/activate ]; then \
		source venv/bin/activate && PIGPIO_ADDR=$(PIGPIO_ADDR) python maker_drive_gamepad_video.py; \
	else \
		PIGPIO_ADDR=$(PIGPIO_ADDR) python maker_drive_gamepad_video.py; \
	fi
