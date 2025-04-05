# sigma_chi_calculator.py

# Constants (SI units)
k_B = 1.380649e-23       # Boltzmann constant (J/K)
c = 2.99792458e8         # Speed of light (m/s)
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
hbar = 1.054571817e-34   # Reduced Planck constant (J·s)
eV_to_J = 1.602176634e-19  # 1 eV in joules

def sigma_chi(Delta_chi_eV, T_H_K):
    """Compute entropy production rate σ_χ in units of k_B"""
    Delta_chi_J = Delta_chi_eV * eV_to_J
    ratio = (Delta_chi_J / T_H_K)**2
    prefactor = (k_B * c**3) / (G * hbar)
    sigma = prefactor * ratio / k_B  # divide out k_B to return in units of k_B
    return sigma

# Example usage
if __name__ == "__main__":
    Delta_chi = 1e-8  # in eV
    T_H = 1e-8        # in K, example for stellar-mass BH

    result = sigma_chi(Delta_chi, T_H)
    print(f"σ_χ ≈ {result:.3e} k_B / s")
