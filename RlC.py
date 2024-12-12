import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, StateSpace, step, lsim
##Name:Mohammad Ataya
##ID:1211555
#Sec:2
###** System 2 : RLC Circuit **###
def simulate_rlc_circuit():
    # System parameters
    L = 0.5
    C = 0.01
    R_over = 5.0
    R_crit = 2.0
    R_under = 0.5

    # Time vector for simulation
    t = np.linspace(0, 20, 1000)

    ### Laplace-Domain Transfer Function ###
    num = [1, 0]
    den_crit = [L, R_crit , 1/C]  #
    den_under = [L, R_under , 1/C]
    den_ove = [L, R_over, 1 / C]
    sys_tf_crit = TransferFunction(num, den_crit)
    sys_tf_under = TransferFunction(num, den_under)
    sys_tf_ove = TransferFunction(num, den_ove)
    # Step response (Laplace domain)
    t_out_tf_crit, y_out_tf_crit = step(sys_tf_crit, T=t)
    t_out_tf_under, y_out_tf_under = step(sys_tf_under, T=t)
    t_out_tf_ove, y_out_tf_ove = step(sys_tf_ove, T=t)

    ### State-Space Representation ###
    # State-space matrices for RLC circuit
    A_crit = np.array([[0, 1], [-1/(L*C), -R_crit/L]])
    A_under = np.array([[0, 1], [-1 / (L * C), -R_under / L]])
    A_ove = np.array([[0, 1], [-1 / (L * C), -R_over / L]])
    B = np.array([[0], [1/L]])
    C = np.array([1, 0])
    D = np.array([0])

    # Create state-space system
    sys_ss_crit = StateSpace(A_crit, B, C, D)
    sys_ss_under = StateSpace(A_under , B, C, D)
    sys_ss_ove = StateSpace(A_ove, B, C, D)

    # Unit step/Ramp/Sinusoidal inputs force
    U = np.sin(2 * np.pi * 0.5 * t)

    t_out_ss_crit , y_out_ss_crit , x_out_ss_crit  = lsim(sys_ss_crit , U, t)
    t_out_ss_under, y_out_ss_under, x_out_ss_under = lsim(sys_ss_under, U, t)
    t_out_ss_ove, y_out_ss_ove, x_out_ss_ove = lsim(sys_ss_ove, U, t)

# ____________________________________________________________________________________________________________#

    ### Plotting Time-Domain ###
    plt.figure(figsize=(10, 5))
    plt.plot(t_out_ss_crit, y_out_ss_crit, label='Time-Domain Response', color='green')
    plt.plot(t_out_ss_under, y_out_ss_under, label='Time-Domain Response', color='orange')
    plt.plot(t_out_ss_ove, y_out_ss_ove, label='Time-Domain Response', color='blue')
    plt.title('RLC Circuit Response (Time-Domain)')
    plt.xlabel('Time (s)')
    plt.ylabel('Current')
    plt.grid(True)
    plt.legend()
    plt.show()
#____________________________________________________________________________________________________________#
    ### Plotting Laplace-Domain ###
    plt.figure(figsize=(10, 5))
    plt.plot(t_out_tf_crit, y_out_tf_crit, label='Laplace-Domain (Transfer Function)', color='blue')
    plt.plot(t_out_tf_under, y_out_tf_under, label='Laplace-Domain (Transfer Function)', color='orange')
    plt.plot(t_out_tf_ove, y_out_tf_ove, label='Laplace-Domain (Transfer Function)', color='green')
    plt.title('RLC Circuit Response (Laplace-Domain)')
    plt.xlabel('Time (s)')
    plt.ylabel('Current')
    plt.grid(True)
    plt.legend()
    plt.show()
# ____________________________________________________________________________________________________________#

    ### Plotting State-Space  ###
    plt.figure(figsize=(10, 5))
    plt.plot(t_out_ss_crit, y_out_ss_crit, label='State-Space ', color='orange')
    plt.plot(t_out_ss_under, y_out_ss_under, label='State-Space ', color='blue')
    plt.plot(t_out_ss_ove, y_out_ss_ove, label='State-Space ', color='green')
    plt.title('RLC Circuit Response (State-Space)')
    plt.xlabel('Time (s)')
    plt.ylabel('Current')
    plt.grid(True)
    plt.legend()
    plt.show()

 # ____________________________________________________________________________________________________________#

# Main function to call simulation for RLC Circuit
if __name__ == "__main__":
    simulate_rlc_circuit()
