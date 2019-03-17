clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '>>- Notelizer -<< ' --python=python3 env
	env/bin/pip install -r requirements.txt
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=journalizer \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/
build:
	if [ -d "build" ]; then rm -rfv build; fi
	if [ -d "dist" ]; then rm -rfv dist; fi
	pyinstaller --onefile notelizer.py
install:
	if [ -f "~/.local/bin/no" ]; then rm -rf ~/.local/bin/no; fi
	cp -v dist/notelizer ~/.local/bin/no
