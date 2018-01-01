all: algo.ex stat.ex

algo.ex:
	echo 'python src/main.py --run ALGO' > algo.ex
	chmod u+x algo.ex

stat.ex: 
	echo 'python src/main.py --run STAT' > stat.ex
	chmod u+x stat.ex

clean:
	rm algo.ex stat.ex

# TODO: remove
xml:
	python src/main.py --run XML
