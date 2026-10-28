import pandas as pd
import matplotlib.pyplot as plt

#Data
dati = pd.read_csv('/home/leonardo_ubuntu/MCF/Metodi_computazionali/E04/Dati/kplr010666592-2011240104155_slc.csv')
tempo = dati['TIME']
flusso = dati['PDCSAP_FLUX']
err = dati['PDCSAP_FLUX_ERR']

#Dati locali
loc_dati = dati.loc[( dati['TIME'] > 952) & ( dati['TIME'] < 953)]
loc_tempo = loc_dati['TIME']
loc_flusso = loc_dati['PDCSAP_FLUX']
loc_err = loc_dati['PDCSAP_FLUX_ERR']

#Grafico 1
plt.errorbar(tempo, flusso, yerr=err, fmt='.', color='red')
plt.xlabel('Time [s]')
plt.ylabel('Flusso [$e^-$/s]')
plt.show()
# print(dati.columns)

#Grafico 2
plt.errorbar(loc_tempo, loc_flusso, yerr=loc_err, fmt = 'o', color='purple')
plt.xlabel('Time [s]')
plt.ylabel('Flusso [$e^-$/s]')
plt.show()

#Grafico 3
fig, ax = plt.subplots(figsize=(14,10))
ax.errorbar(tempo, flusso, yerr=err, fmt='.', color='red')

#Spazio per l'insert
y_min = flusso.min()
y_max = flusso.max()
delta_y = y_max - y_min
ax.set_ylim(y_min - 0.05 * delta_y, y_max + 0.45 * delta_y)

ins_ax = ax.inset_axes([0.65, 0.68, 0.3, 0.28])
ins_ax.errorbar(loc_tempo, loc_flusso, yerr=loc_err, color='red')
plt.xlabel('Time [s]')
plt.ylabel('Flusso [$e^-$/s]')

plt.savefig('grafico.pdf', format='pdf', bbox_inches='tight', dpi=300)

plt.show()