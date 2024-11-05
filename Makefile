test:
	pytest -v -p no:warnings

cov:
	xdg-open htmlcov/index.html
