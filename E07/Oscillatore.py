import numpy as np
from  scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse

# Periodo
def calcola_periodo(x0, V_funz, m, N=1000):
    x = np.linspace(0, x0, N + 1, endpoint=False) #endpoint risolve il problema in x0
    integranda = 1.0 / np.sqrt(V_funz(x0) - V_funz(x))
    i = integrate.simpson(integranda, x=x)
    return np.sqrt(8 * m) * i

# Argparse
def main():
    parser = argparse.ArgumentParser(description='Calcola e visualizza il periodo T(x0) per diversi potenziali')
    parser.add_argument('-p', '--potenziale', type=str, choices=["x^2", "x^6", "|x|^(3/2)", "tutti"], default="tutti", help='Scegli il potenziale da utilizzare: x^2, x^6, |x|^(3/2) o tutti (default: tutti).')
    parser.add_argument('-m', '--massa', type=float, default= 1.0, help='Massa della particella in Kg (default: 1.0)')
    parser.add_argument('-k', '--costante', type=float, default= 1.0, help='Costante k del potenziale (default: 1.0)')
    return  parser.parse_args()

# Parametri
x0_valori = np.linspace(0.1, 5.0, 100)  # evito x0 = 0
args = main()
m = args.massa
k = args.costante

# Potenziali
potenziali = {
      "x^2": (lambda x: k * x**2, r"Armonico $V_a(x) = kx^2$"),
      "x^6": (lambda x: k * x**6, r"Anarmonico $V(x) = kx^6$"),
      "|x|^(3/2)": (lambda x: k * np.abs(x) ** 1.5, r"Modulo $V(x) = k|x|^{3/2}$"),
  }

plt.figure(figsize=(8, 5))

# Scelte
scelte = potenziali.keys() if args.potenziale == "tutti" else [args.potenziale]

for chiave in scelte:
    V_func, etichetta = potenziali[chiave]
    T_valori = np.array([calcola_periodo(x0, V_func, m) for x0 in x0_valori])
    plt.plot(x0_valori, T_valori, label=etichetta, lw=2)


#Grafico
plt.title("Periodo di oscillazione $T$ in funzione del punto di partenza $x_0$")
plt.xlabel("Punto di partenza $x_0$ [m]")
plt.ylabel("Periodo $T$ [s]")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()