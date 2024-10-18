import numpy as np
import matplotlib.pyplot as plt

amplitude = 17 
freq = 5 
fs = 500
t = np.linspace(0, 1, fs)  

distortion_angle_deg = 69  
distortion_angle_rad = distortion_angle_deg * np.pi / 180  

data = [1, 0, 1, 1, 0]

def generate_ask(data, amplitude, freq, fs, t):
    ask_signal = np.zeros(len(t))
    for i, bit in enumerate(data):
        if bit == 1:
            ask_signal[i * (fs // len(data)):(i + 1) * (fs // len(data))] = amplitude * np.cos(2 * np.pi * freq * t[:fs // len(data)])
        else:
            ask_signal[i * (fs // len(data)):(i + 1) * (fs // len(data))] = 0
    return ask_signal

ask_signal_original = generate_ask(data, amplitude, freq, fs, t)
ask_signal_distorted = amplitude * np.cos(2 * np.pi * freq * t + distortion_angle_rad) * (np.repeat(data, fs // len(data)))

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, ask_signal_original, label="Original ASK Signal")
plt.title("Original ASK Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, ask_signal_distorted, label="Distorted ASK Signal", color="r")
plt.title(f"Distorted ASK Signal (Distortion = {distortion_angle_deg}°)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
