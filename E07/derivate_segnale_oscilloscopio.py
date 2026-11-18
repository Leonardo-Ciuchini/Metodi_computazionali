from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Lettura dati
dati = pd.read_csv(Path(__file__).parent / 'oscilloscope.csv', comment='#')
t = dati.loc[:, 'time'].to_numpy()
ch1 = dati.loc[:, 'signal1'].to_numpy()
ch2 = dati.loc[:, 'signal2'].to_numpy()


# Funzione per la differenza centrale con passo n
def differenza_centrale(x, y, n=2):
  k = n // 2
  if k < 1:
    raise ValueError('Il parametro n deve essere almeno 2.')
  dy = y[2 * k :] - y[: -2 * k]
  dx = x[2 * k :] - x[: -2 * k]
  return x[k:-k], dy / dx


# Grafico delle derivate al variare di n
valori_n = [2, 20, 100]  # Puoi provare anche altri valori (es. 50, 200)
colori = ['lightgray', 'royalblue', 'crimson']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

for n, col in zip(valori_n, colori):
  t_der, d_ch1 = differenza_centrale(t, ch1, n=n)
  _, d_ch2 = differenza_centrale(t, ch2, n=n)

  # Impostiamo alpha più basso per n=2 così non copre le curve pulite
  trasparenza = 0.5 if n == 2 else 0.9

  ax1.plot(
      t_der, d_ch1, label=f'n = {n}', color=col, alpha=trasparenza, lw=1.5
  )
  ax2.plot(
      t_der, d_ch2, label=f'n = {n}', color=col, alpha=trasparenza, lw=1.5
  )

# Formattazione Canale 1
ax1.set_title('Derivata Canale 1 (signal1)')
ax1.set_ylabel('dV/dt [V/s]')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper right')

# Formattazione Canale 2
ax2.set_title('Derivata Canale 2 (signal2)')
ax2.set_xlabel('Tempo [s]')
ax2.set_ylabel('dV/dt [V/s]')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()