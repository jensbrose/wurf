#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, fixed

def optimaler_winkel(v_0, z_0, g=9.81):
    return np.rad2deg(np.arcsin(v_0/np.sqrt(2 * (v_0**2 + z_0 * g))))

def bahnkurve(alpha=45, v_0=13.5, z_0=0, g=9.81):
    """ alpha - Wurfwinkel [°], 
        v_0   - Anfangsgeschwindigkeit [m/s], 
        z_0   - Anfangshöhe [m], 
        g     - Fallbeschleunigung [m/s²]
    """
    x = np.arange(0, 25, 0.1)               # horizontale Koordinate [m]
    print("Optimaler Wurfwinkel: {:4.2f}".format(optimaler_winkel(v_0, z_0, g)))
    tan_alpha = np.tan(np.deg2rad(alpha))
    z = -g * (1 + tan_alpha**2) / 2 / v_0**2 * x**2 + tan_alpha * x + z_0 # Bahn z(x)
    print("Höchster Punkt: z_max = {:4.2f} m bei x = {:4.2f} m".format(z.max(), x[z.argmax()]))
    ende =  np.where(z < 0)[0][0]           # Index der Wurfweite
    print("Wurfweite: {:5.2f} m".format(x[ende]))
    plt.figure(figsize=[10, 6])
    plt.plot(x[:ende], z[:ende])
    plt.xlabel("Ort x [m]")
    plt.ylabel("Höhe z [m]")
    plt.title("Bahnkurve beim Kugelstoßen (EPI/2.3)")
    plt.show()

interact(bahnkurve, alpha=(0.0, 90.0 ,1.0), v_0=(1, 15, .5), z_0=(0, 3, .1), g=fixed(9.81));
