import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#Data
dati = pd.read_csv(Path(__file__).parent / 'Dati' / 'ExoplanetsPars_2025.csv', comment='#')

#Selezione dei dati per grafico 1
transit = dati.loc[dati['discoverymethod'] == 'Transit']
rv = dati.loc[dati['discoverymethod'] == 'Radial Velocity']

# print(dati.columns)
# print(dati['pl_orbper'])

#Grafico 1
plt.scatter(transit['pl_orbper'], transit['pl_bmassj'], s=15, color='red', alpha=0.5, label='Transit')
plt.scatter(rv['pl_orbper'], rv['pl_bmassj'], s=10, color='orange', alpha=0.5, label='Radial Velocity')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Orbital Period [days]')
plt.ylabel('Planetary Mass [Jupiter masses]')
plt.legend()
plt.show()

#Grafico 2
y = dati ['pl_orbsmax']**2 / dati ['st_mass']
plt.scatter(dati['pl_orbper'], y, s=1, color='yellow', alpha=0.5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Orbital Period [days]')
plt.ylabel('Orbital Radius [AU]')
plt.show()

#Istogramma
plt.hist(transit['pl_bmassj'], bins=100, color='green', alpha=0.5)
plt.hist(rv['pl_bmassj'], bins=100, color='blue', alpha=0.5)
plt.xscale('log')
plt.xlabel('Planetary Mass [Jupiter masses]')
plt.ylabel('Frequency')
plt.show()
