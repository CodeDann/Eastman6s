venv/bin/activate: requirements.txt
	@echo "installing requirements"
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt; \

run: venv/bin/activate
	@source venv/bin/activate; \
	export FLASK_APP=run.py; \
	export FLASK_ENV=development; \
	flask run --eager-loading --host=0.0.0.0 --port=5001; \

