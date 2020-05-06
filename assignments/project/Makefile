.PHONY: test pdf clean

pdf:
	asciidoctor-pdf README.adoc

test:
	pytest -xv test.py

clean:
	rm -rf __pycache__

test:
	pytest --disable-pytest-warnings -xv test.py