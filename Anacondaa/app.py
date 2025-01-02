import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi Trapezoidal Rule
def trapezoidal_rule(x, y):
    n = len(x)  # Jumlah titik
    integral = (x[-1] - x[0]) * (y[0] + 2 * np.sum(y[1:n-1]) + y[n-1]) / (2 * (n - 1))
    return integral

# Streamlit Interface
st.title("Trapezoidal Rule Calculator with Visualization")
st.write("Hitung integral menggunakan metode Trapezoidal Rule dan lihat visualisasi grafiknya.")

# Input untuk titik pembagi dan nilai fungsi
x_input = st.text_input("Masukkan titik-titik pembagi (pisahkan dengan koma):", "1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8")
y_input = st.text_input("Masukkan nilai fungsi pada titik-titik tersebut (pisahkan dengan koma):", "1.449, 2.06, 2.645, 3.216, 3.779, 4.338, 4.898")

# Proses input
try:
    x = np.array([float(i.strip()) for i in x_input.split(",")])
    y = np.array([float(i.strip()) for i in y_input.split(",")])

    if len(x) != len(y):
        st.error("Jumlah titik pembagi (x) harus sama dengan jumlah nilai fungsi (y).")
    else:
        # Menghitung integral
        result = trapezoidal_rule(x, y)
        st.success(f"Hasil integral menggunakan metode Trapezoidal Rule adalah: {result}")

        # Membuat visualisasi grafik
        fig, ax = plt.subplots()
        ax.plot(x, y, 'bo-', label="Data")
        for i in range(len(x) - 1):
            ax.fill_between([x[i], x[i+1]], [y[i], y[i+1]], color='skyblue', alpha=0.5)
        ax.set_title("Visualisasi Metode Trapezoidal")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        st.pyplot(fig)

except ValueError:
    st.error("Pastikan semua input valid dan berupa angka yang dipisahkan oleh koma.")

st.write("Masukkan nilai yang sesuai, lalu hasil dan grafik akan dihitung secara otomatis.")


