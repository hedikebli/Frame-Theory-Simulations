#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
from matplotlib.gridspec import GridSpec

# Initial global parameters
G  = 1.0
M  = 1.0
dt = 0.01
r0 = 3.0
Rt_sim = 8.0

def acc_newton(x, y):
    r = max(np.hypot(x, y), 0.3)
    c = -G * M / r**3
    return c*x, c*y

def acc_trame(x, y):
    r  = max(np.hypot(x, y), 0.3)
    fn = -G * M / r**3
    ft = -G * M / (r**2 * Rt_sim)
    return (fn + ft)*x, (fn + ft)*y

def step(x, y, vx, vy, acc):
    ax, ay = acc(x, y)
    vx += ax * dt;  vy += ay * dt
    x  += vx * dt;  y  += vy * dt
    return x, y, vx, vy

# ── Photons ──
b     = 50.0
x0_ph = -80.0
x1_ph =  80.0
dt_ph = 0.05
N_ph  = 6000

def compute_photon(factor):
    x, y   = x0_ph, b
    vx, vy = 1.0, 0.0
    xs, ys = [], []
    for _ in range(N_ph):
        xs.append(x); ys.append(y)
        if x > x1_ph: break
        r  = max(np.hypot(x, y), 0.5)
        ax = -factor * G * M * x / r**3
        ay = -factor * G * M * y / r**3
        vx += ax * dt_ph
        vy += ay * dt_ph
        x  += vx * dt_ph
        y  += vy * dt_ph
    while len(xs) < N_ph:
        xs.append(xs[-1]); ys.append(ys[-1])
    return np.array(xs), np.array(ys)

# ── Figure ──
fig = plt.figure(figsize=(15, 10), facecolor='#0a0a1a')
fig.suptitle("Frame Theory: Comparison with Newton", color='white', fontsize=18, fontweight='bold', y=0.96)

# GridSpec for adjusting widths
gs = GridSpec(2, 2, width_ratios=[1, 1.4], height_ratios=[1, 1.2])

ax_O = fig.add_subplot(gs[0, 0], facecolor='#0d0d2b')
ax_P = fig.add_subplot(gs[0, 1], facecolor='#0d0d2b')
ax_G = fig.add_subplot(gs[1, :], facecolor='#0d0d2b')
plt.subplots_adjust(bottom=0.28, hspace=0.35, wspace=0.2)

for ax in [ax_O, ax_P, ax_G]:
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    for sp in ax.spines.values(): sp.set_edgecolor('#444')

# Styling box to prevent equation cropping
eq_box = dict(facecolor='#0a0a1a', alpha=0.8, edgecolor='#333', boxstyle='round,pad=0.5')

# Orbits
ax_O.set_xlim(-6, 6); ax_O.set_ylim(-6, 6)
ax_O.set_aspect('equal')
ax_O.set_title("Orbits (Same initial velocity)", color='white', fontsize=13)
ax_O.plot(0, 0, 'o', color='yellow', ms=18, zorder=10)
ln_NO, = ax_O.plot([], [], '#4488ff', lw=1.5, label='Newton')
ln_TO, = ax_O.plot([], [], '#ff8844', lw=1.5, label='Frame')
pt_NO, = ax_O.plot([], [], 'o', color='#4488ff', ms=8, zorder=9)
pt_TO, = ax_O.plot([], [], 'o', color='#ff8844', ms=8, zorder=9)
ax_O.legend(facecolor='#1a1a3a', labelcolor='white', loc='upper right')
ax_O.text(-5.5, -5.5, r"$\vec{g} = -\frac{GM}{r^2}\left(1 + \frac{r}{R_t}\right) \vec{u}_r$", color='#ff8844', fontsize=11, bbox=eq_box)

# Photons (ZOOMED)
ax_P.set_xlim(-80, 80); ax_P.set_ylim(42, 52) 
ax_P.set_title("Photon Deflection (Zoom ×2 Eddington)", color='white', fontsize=13)
ax_P.axvline(0, color='yellow', lw=1, ls='--', alpha=0.3)

# Yellow disk background representing central mass
ax_P.plot(0, 42, 'o', color='yellow', ms=70, alpha=0.9, zorder=1)

ln_NP, = ax_P.plot([], [], '#4488ff', lw=2, label='Newton')
ln_TP, = ax_P.plot([], [], '#ff8844', lw=2, label='Frame')
pt_NP, = ax_P.plot([], [], 'o', color='#4488ff', ms=8, zorder=9)
pt_TP, = ax_P.plot([], [], 'o', color='#ff8844', ms=8, zorder=9)
ax_P.text(-76, 42.8, r"$\theta_{Frame} = \frac{4GM}{bc^2}$", color='#ff8844', fontsize=14, bbox=eq_box)

# Galactic Rotation
G_SI  = 6.674e-11
M_SUN = 1.989e30
KPC   = 3.086e19
a0    = 1.13e-10

r_kpc = np.linspace(0.5, 30, 400)
r_m   = r_kpc * KPC

def vN_si(r, mass): return np.sqrt(G_SI * mass / r)
def vT_si(r, mass, Rt_val): return np.sqrt(G_SI * mass / r + G_SI * mass / Rt_val)

ax_G.set_xlabel("r (kpc)"); ax_G.set_ylabel("v (km/s)")
ax_G.set_title("Galactic Rotation Curves", color='white', fontsize=13)
ax_G.set_ylim(0, 450)
ln_NG, = ax_G.plot(r_kpc, np.zeros_like(r_kpc), '#4488ff', lw=2, label='Newton')
ln_TG, = ax_G.plot(r_kpc, np.zeros_like(r_kpc), '#ff8844', lw=2, label='Frame')
ln_Rt  = ax_G.axvline(0, color='white', ls='--', alpha=0.6, label=r'Transition Radius $R_t$')
pt_NG, = ax_G.plot([], [], 'o', color='#4488ff', ms=10, zorder=9)
pt_TG, = ax_G.plot([], [], 'o', color='#ff8844', ms=10, zorder=9)
ax_G.legend(facecolor='#1a1a3a', labelcolor='white', loc='upper right')
ax_G.text(1.0, 40, r"$v^2_{Frame}(r) = \frac{GM}{r} + \frac{GM}{R_t}$", color='#ff8844', fontsize=15, bbox=eq_box)

# ── Sliders ──
ax_sM  = plt.axes([0.15, 0.15, 0.7, 0.025], facecolor='#1a1a3a')
ax_sV  = plt.axes([0.15, 0.10, 0.7, 0.025], facecolor='#1a1a3a')
sl_M   = Slider(ax_sM, 'Galaxy Mass (×10¹¹ M☉)', 0.1, 5.0, valinit=1.0,  color='#4488ff')
sl_V   = Slider(ax_sV, 'Orbit Speed',        1,  40,  valinit=30,   color='#88ff44', valstep=1)
for sl in [sl_M, sl_V]:
    sl.label.set_color('white'); sl.valtext.set_color('white')

ax_btn = plt.axes([0.45, 0.04, 0.1, 0.04])
btn    = Button(ax_btn, 'Reset', color='#223', hovercolor='#445')
btn.label.set_color('white')

state = dict(
    Nx=r0, Ny=0.0, Nvx=0.0, Nvy=0.0,
    Tx=r0, Ty=0.0, Tvx=0.0, Tvy=0.0,
    Nxs=[], Nys=[], Txs=[], Tys=[],
    ph_i=0, gal_r=0.5,
    ph_Nx=[], ph_Ny=[], ph_Tx=[], ph_Ty=[]
)

TRAIL_N = 100; TRAIL_T = 100
Rt_actuel = 15.0

def update_physics(val=None):
    global M, TRAIL_N, TRAIL_T, Rt_actuel
    M = sl_M.val
    
    M_si = M * 1e11 * M_SUN
    Rt_SI = np.sqrt(G_SI * M_si / a0)
    Rt_actuel = Rt_SI / KPC
    
    vN   = vN_si(r_m, M_si)/1e3
    vT   = vT_si(r_m, M_si, Rt_SI)/1e3
    ln_NG.set_ydata(vN)
    ln_TG.set_ydata(vT)
    ln_Rt.set_xdata([Rt_actuel, Rt_actuel])
    
    state['ph_Nx'], state['ph_Ny'] = compute_photon(factor=1)
    state['ph_Tx'], state['ph_Ty'] = compute_photon(factor=2)
    alpha_N = np.degrees(2*G*M/b)
    alpha_T = np.degrees(4*G*M/b)
    ln_NP.set_label(f'Newton  θ={alpha_N:.3f}°')
    ln_TP.set_label(f'Frame   θ={alpha_T:.3f}°')
    ax_P.legend(facecolor='#1a1a3a', labelcolor='white', fontsize=10, loc='upper right')
    
    v_init = np.sqrt(G * M / r0)
    T_orb_N = 2 * np.pi * r0 / v_init
    TRAIL_N = int(T_orb_N / dt * 0.95)
    TRAIL_T = TRAIL_N * 3
    
    state.update(
        Nx=r0, Ny=0.0, Nvx=0.0, Nvy=v_init,
        Tx=r0, Ty=0.0, Tvx=0.0, Tvy=v_init,
        Nxs=[], Nys=[], Txs=[], Tys=[],
        ph_i=0
    )
    fig.canvas.draw_idle()

sl_M.on_changed(update_physics)
btn.on_clicked(update_physics)

update_physics()

PH_SPEED  = 18
GAL_SPEED = 0.04

def animate(frame):
    s = state
    n_sub = int(sl_V.val)
    
    for _ in range(n_sub):
        s['Nx'],s['Ny'],s['Nvx'],s['Nvy'] = step(s['Nx'],s['Ny'],s['Nvx'],s['Nvy'],acc_newton)
        s['Tx'],s['Ty'],s['Tvx'],s['Tvy'] = step(s['Tx'],s['Ty'],s['Tvx'],s['Tvy'],acc_trame)
    
    s['Nxs'].append(s['Nx']); s['Nys'].append(s['Ny'])
    s['Txs'].append(s['Tx']); s['Tys'].append(s['Ty'])
    if len(s['Nxs']) > TRAIL_N: s['Nxs'].pop(0); s['Nys'].pop(0)
    if len(s['Txs']) > TRAIL_T: s['Txs'].pop(0); s['Tys'].pop(0)
    
    ln_NO.set_data(s['Nxs'], s['Nys'])
    ln_TO.set_data(s['Txs'], s['Tys'])
    pt_NO.set_data([s['Nx']], [s['Ny']])
    pt_TO.set_data([s['Tx']], [s['Ty']])

    i = min(s['ph_i'], N_ph-1)
    ln_NP.set_data(s['ph_Nx'][:i+1], s['ph_Ny'][:i+1])
    ln_TP.set_data(s['ph_Tx'][:i+1], s['ph_Ty'][:i+1])
    pt_NP.set_data([s['ph_Nx'][i]], [s['ph_Ny'][i]])
    pt_TP.set_data([s['ph_Tx'][i]], [s['ph_Ty'][i]])
    s['ph_i'] = (s['ph_i'] + PH_SPEED) % N_ph

    gr    = s['gal_r']
    gr_m  = gr * KPC
    M_si  = M * 1e11 * M_SUN
    Rt_SI = np.sqrt(G_SI * M_si / a0)
    pt_NG.set_data([gr], [vN_si(gr_m, M_si)/1e3])
    pt_TG.set_data([gr], [vT_si(gr_m, M_si, Rt_SI)/1e3])
    s['gal_r'] = gr + GAL_SPEED
    if s['gal_r'] > 30: s['gal_r'] = 0.5

    return ln_NO, ln_TO, pt_NO, pt_TO, ln_NP, ln_TP, pt_NP, pt_TP, pt_NG, pt_TG, ln_Rt

anim = FuncAnimation(fig, animate, interval=20, blit=False)
plt.show()
