.PHONY: install test clean reset-index

install:
	pip install -e .

test:
	pytest

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f index.faiss chunks.pkl

reset-index:
	rm -f index.faiss chunks.pkl
	@echo "Index and chunks removed."

