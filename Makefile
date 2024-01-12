venv/bin/activate: requirements.txt
	@echo "installing requirements..."
	python3 -m venv venv; 
	source venv/bin/activate; 
	venv/bin/pip3 install -r requirements.txt; 
	@echo " ------- install complete -------";

run: venv/bin/activate
	@export FLASK_APP=app.py; 
	@export FLASK_ENV=development; 
	@flask run --eager-loading --host=0.0.0.0 --port=5001; 

