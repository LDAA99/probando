fechas_manchas.pdf: grafica.py fechas_manchas.dat
	python grafica.py

fechas_manchas.dat: monthrg.dat procesa.py
	python procesa.py 


