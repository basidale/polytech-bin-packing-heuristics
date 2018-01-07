all: clean algo.ex stat.ex

algo.ex:
	echo 'python source/main.py --run ALGO' > algo.ex
	chmod u+x algo.ex

stat.ex:
	echo 'python source/main.py --run STAT' > stat.ex
	chmod u+x stat.ex

test:
	python source/test.py

clean:
	rm -f algo.ex stat.ex

# TODO: remove
xml:
	python source/main.py --run XML
