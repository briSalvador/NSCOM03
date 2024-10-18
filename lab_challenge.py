import numpy as np
import matplotlib.pyplot as plt

# Parameters
Amp = 5              # Amplitude
f1 = 25              # Frequency for bit 0
f2 = 50              # Frequency for bit 1
Fs = 10000           # Sampling frequency
Tb = 0.05            # Bit duration
time = np.arange(0, Tb, 1/Fs)  # Time vector for one bit

# Binary data to transmit
data = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Generate FSK signal
fsk_signal = []

for bit in data:
    if bit == 0:
        signal = Amp * np.sin(2 * np.pi * f1 * time)  # Signal for bit 0
    else:
        signal = Amp * np.sin(2 * np.pi * f2 * time)  # Signal for bit 1
    
    fsk_signal = np.concatenate((fsk_signal, signal))

# Create a full time vector for the entire signal
full_time = np.arange(0, Tb * len(data), 1/Fs)

# Initialize noisy signal
noisy_signal = np.copy(fsk_signal)

noise_mean = 0
noise_std_dev_1 = 0.5
noise_std_dev_2 = 1.5

# Loop through each bit and add alternating noise every 3 cycles
num_cycles = len(data)
for cycle in range(num_cycles):
    # Choose noise standard deviation based on cycle (every 3 cycles switch noise)
    if (cycle // 3) % 2 == 0:  # Noise type 1
        noise_std_dev = noise_std_dev_1
    else:  # Noise type 2
        noise_std_dev = noise_std_dev_2
    
    # Generate noise for the current bit
    noise = np.random.normal(noise_mean, noise_std_dev, time.shape[0])
    
    # Add noise to the corresponding segments of the FSK signal
    noisy_signal[cycle * time.shape[0]:(cycle + 1) * time.shape[0]] += noise

# Plotting
plt.figure(figsize=(10, 6))

# Plot clean FSK signal
plt.subplot(2, 1, 1)
plt.plot(full_time, fsk_signal, color='b')
plt.title("Clean FSK Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot FSK signal with noise
plt.subplot(2, 1, 2)
plt.plot(full_time, noisy_signal, color='r')
plt.title("FSK Signal with Alternating Noise")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()  # Adjust subplots to fit into figure area.
plt.show()
