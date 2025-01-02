import numpy as np
import matplotlib.pyplot as plt

# Metode Midpoint Rule
def midpoint_rule(x, y):
    n = len(x)  # Jumlah titik (jumlah subinterval + 1)
    integral = 0
    midpoints = []  # Untuk menyimpan titik-titik tengah
    values = []     # Untuk menyimpan nilai interpolasi di titik tengah

    for i in range(n - 1):
        # Menghitung titik tengah (midpoint) antara x[i] dan x[i+1]
        midpoint = (x[i] + x[i+1]) / 2
        mid_value = np.interp(midpoint, x, y)
        midpoints.append(midpoint)
        values.append(mid_value)
        integral += (x[i+1] - x[i]) * mid_value

    return integral, midpoints, values

# Contoh penggunaan
x = np.array([1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8])  # Titik-titik pembagi
y = np.array([1.449, 2.06, 2.645, 3.216, 3.779, 4.338, 4.898])  # Nilai fungsi pada titik-titik tersebut

# Menghitung integral dan titik-titik tengah
result, midpoints, values = midpoint_rule(x, y)

# Menampilkan hasil
print(f"Integral menggunakan metode Midpoint Rule adalah: {result}")

# Visualisasi grafik
fig, ax = plt.subplots()
# Plot data asli
ax.plot(x, y, 'bo-', label="Data (x, f(x))")
# Plot batang untuk area midpoint
for i in range(len(midpoints)):
    ax.bar(midpoints[i], values[i], width=(x[i+1] - x[i]), color='skyblue', alpha=0.5, edgecolor='black', align='center')
# Tambahkan label dan judul
ax.set_title("Visualisasi Metode Midpoint Rule")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()

# Tampilkan grafik
plt.show()
