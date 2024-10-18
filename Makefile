install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint: 
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# ruff check *.py mylib/*.py test_*.py 

run_make:
	python main.py  # Execute the main.py script

test: 
	python -m pytest -vv --nbval -cov=mylib -cov=main test_main.py  # Run tests after main.py

generate_and_push:
	# Create the markdown file 
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python mylib/extract.py

transform: 
	python mylib/transform.py

query:
	python mylib/query.py

# The all target ensures the correct order of operations
all: install format lint run_make test
