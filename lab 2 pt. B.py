import matplotlib.pyplot as plt
import numpy as np

# Density measurements
measurements = [
    "Measurement 1",
    "Measurement 2",
    "Measurement 3",
    "Measurement 4"
]

density = [1.044, 0.8935, 0.8903, 0.8945]

# Average density
average_density = np.mean(density)

# Standard deviation for error bars
std_dev = np.std(density, ddof=1)

# Reference density of water
reference_density = 1.00

# Create bar graph with error bars
plt.bar(
    measurements,
    density,
    yerr=std_dev,
    capsize=6
)

# Average density line
plt.axhline(
    average_density,
    linestyle="--",
    label=f"Average = {average_density:.3f} g/mL"
)

# Reference density line
plt.axhline(
    reference_density,
    linestyle="-",
    label="Reference density = 1.00 g/mL"
)

# Put density numbers above bars
for i, value in enumerate(density):
    plt.text(
        i,
        value + 0.01,
        f"{value:.3f}",
        ha="center"
    )

# Labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 20°C")

plt.ylim(0.75, 1.15)

plt.legend()
plt.tight_layout()

plt.show()

# Print calculations
print("Average Density =", round(average_density, 4), "g/mL")
print("Standard Deviation =", round(std_dev, 4), "g/mL")
