# Makefile untuk RAG Chatbot

install:
	pip install -r requirements.txt

train:
	python src/train.py

inference:
	python src/inference.py

test:
	pytest tests/

lint:
	flake8 src/

notebook:
	jupyter notebook notebooks/
