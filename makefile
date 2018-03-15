fechas_manchas.pdf: grafica.py fechas_manchas.dat
	python grafica.py

fechas_manchas.dat: monthrg.dat procesa.py
	python procesa.py 

monthrg.dat:
	wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/solar/monthrg.dat
