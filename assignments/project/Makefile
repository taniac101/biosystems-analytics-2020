.PHONY = fa clean run pdf test

MOOG = "../08_synthetic_dna/moog.py"

run: fasta
	./n50.py *.fa

test: fasta
	pytest --disable-pytest-warnings -xv test.py

fasta: file1.fa file2.fa file3.fa file4.fa

clean:
	rm -rf *.fa out __pycache__

file1.fa:
	time $(MOOG) -n 456 -o file1.fa -t dna -m 45 -x 200

file2.fa:
	time $(MOOG) -n 1500 -o file2.fa -t dna -m 300 -x 1000

file3.fa:
	time $(MOOG) -n 4563 -o file3.fa -t dna -m 500 -x 10000

file4.fa:
	time $(MOOG) -n 9888 -o file4.fa -t dna -m 75 -x 200

pdf:
	asciidoctor-pdf README.adoc