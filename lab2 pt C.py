import matplotlib.pyplot as plt
import numpy as np

# Penny measurements
measurements = [
    "Penny 1",
    "Penny 2",
    "Penny 3",
    "Penny 4"
]

# Masses of pennies (g)
mass = [2.51, 2.51, 2.51, 2.51]

# Penny dimensions
diameter = 1.8  # cm
height = 0.1    # cm
radius = diameter / 2

# Calculate volume of penny
volume = np.pi * radius**2 * height

# Calculate density for each penny
density = [m / volume for m in mass]

# Average density
average_density = np.mean(density)

# Standard deviation for error bars
std_dev = np.std(density, ddof=1)

# Reference density of water
water_density = 1.00

# Create bar graph
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
    label=f"Average = {average_density:.2f} g/mL"
)

# Water density reference line
plt.axhline(
    water_density,
    linestyle="-",
    label="Water density = 1.00 g/mL"
)

# Put density values above bars
for i, value in enumerate(density):
    plt.text(
        i,
        value + 0.15,
        f"{value:.2f}",
        ha="center"
    )

# Labels
plt.xlabel("Penny")
plt.ylabel("Density (g/mL)")
plt.title("Density of Pennies Compared with Water")

plt.ylim(0, 11)

plt.legend()
plt.tight_layout()

plt.show()

# Print calculations
print("Volume of penny =", round(volume, 4), "mL")
print("Average density =", round(average_density, 2), "g/mL")
print("Standard deviation =", round(std_dev, 4), "g/mL")
