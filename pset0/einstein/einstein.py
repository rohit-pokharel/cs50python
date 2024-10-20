def main():
    # Speed of light in meters per second
    c = 300000000

    # Prompt the user for mass input
    mass = int(input("Enter mass in kilograms: "))

    # Calculate energy using E = mc^2
    energy = mass * c ** 2

    # Print the equivalent energy
    print(f"The equivalent energy is {energy} Joules.")

main()
