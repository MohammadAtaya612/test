import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, StateSpace, step, lsim
from scipy.integrate import odeint
##Name:Mohammad Ataya
##ID:1211555
#Sec:2

##** System 1: Spring-Mass System** ###
def SimulateSpring():
    # System parameters
    m = 1
    k = 2
    t = np.linspace(0, 10, 500)

    b_underdamped = 1
    b_critically_damped = 2
    b_overdamped = 5

    ### Laplace-Domain Transfer Function ###
    num = [1]
    den_over = [m, b_overdamped, k]
    den_under = [m, b_underdamped, k]
    den_critical = [m, b_critically_damped, k]
    sys_tf_critical = TransferFunction(num, den_critical)
    sys_tf_over = TransferFunction(num, den_over)
    sys_tf_under = TransferFunction(num, den_under)

    # Step response (Laplace domain)
    t_OutTransFunc_critical, y_OutTransFunc_critical = step(sys_tf_critical, T=t)
    t_OutTransFunc_over, y_OutTransFunc_over = step(sys_tf_over, T=t)
    t_OutTransFunc_under, y_OutTransFunc_under = step(sys_tf_under, T=t)

    ### State-Space Representation ###
    A_critical = np.array([[0, 1], [-k / m, -b_critically_damped / m]])
    A_over = np.array([[0, 1], [-k / m, -b_overdamped / m]])
    A_under = np.array([[0, 1], [-k / m, -b_underdamped / m]])

    B = np.array([[0], [1 / m]])
    C = np.array([1, 0])
    D = np.array([0])

    SysStaSpace_critical = StateSpace(A_critical, B, C, D)
    SysStaSpace_over = StateSpace(A_over, B, C, D)
    SysStaSpace_under = StateSpace(A_under, B, C, D)

    # Unit step/Ramp/Sinusoidal inputs force
    U = np.ones_like(t)
    # Simulate state-space response (calculated using state-space approach)
    t_OutStaSpace_critical, y_OutStaSpace_critical, x_OutStaSpace_critical = lsim(SysStaSpace_critical, U, t)
    t_OutStaSpace_over, y_OutStaSpace_over, x_OutStaSpace_over = lsim(SysStaSpace_over, U, t)
    t_OutStaSpace_under, y_OutStaSpace_under, x_OutStaSpace_under = lsim(SysStaSpace_under, U, t)

    def SpringMassOde(InitCond, t, m, b, k):
        x, v = InitCond
        dxdt = v
        dx2dt = (1 / m) * (1 - b * v - k * x)
        return [dxdt, dx2dt]

    InitCond = [0, 0]

    # time_domain_solution = odeint(SpringMassOde, InitCond, t, args=(m, b, k))
    # Solve for different damping cases using odeint
    sol_underdamped = odeint(SpringMassOde, InitCond, t, args=(m, b_underdamped, k))
    sol_critically_damped = odeint(SpringMassOde, InitCond, t, args=(m, b_critically_damped, k))
    sol_overdamped = odeint(SpringMassOde, InitCond, t, args=(m, b_overdamped, k))

    # _________________________________________________________________________________________________________________#
    ### Plotting Time-Domain ###
    plt.figure(figsize=(10, 5))
    plt.plot(t, sol_underdamped[:, 0], label="Underdamped", linestyle="--")
    plt.plot(t, sol_critically_damped[:, 0], label="Critically Damped", linestyle="-.")
    plt.plot(t, sol_overdamped[:, 0], label="Overdamped", linestyle=":")
    plt.title('Spring-Mass System Response (Time-Domain Solution)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement')
    plt.grid(True)
    plt.legend()
    plt.show()
    # _________________________________________________________________________________________________________________#
    ### Plotting Laplace-Domain ###
    plt.figure(figsize=(10, 5))
    plt.plot(t_OutTransFunc_under, y_OutTransFunc_under, label='Underdamped', linestyle="--")
    plt.plot(t_OutTransFunc_critical, y_OutTransFunc_critical, label='Critically Damped', linestyle="-.")
    plt.plot(t_OutTransFunc_over, y_OutTransFunc_over, label='Overdamped', linestyle=":")
    plt.title('Spring-Mass System Response (Laplace-Domain)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement')
    plt.grid(True)
    plt.legend()
    plt.show()
    # _________________________________________________________________________________________________________________#
    ### Plotting State-Space  ###
    plt.figure(figsize=(10, 5))
    plt.plot(t_OutStaSpace_under, y_OutStaSpace_under, label='Under Damp', linestyle="--")
    plt.plot(t_OutStaSpace_critical, y_OutStaSpace_critical, label='Critically Damped', linestyle="-.")
    plt.plot(t_OutStaSpace_over, y_OutStaSpace_over, label='Overdamped', linestyle=":")
    plt.title('Spring-Mass System Response (State-Space Representation)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement')
    plt.grid(True)
    plt.legend()
    plt.show()
 ### Main function ###
if __name__ == "__main__":
    SimulateSpring()
#______________________________________________________________________________________________________________________#