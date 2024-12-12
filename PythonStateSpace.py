import numpy as np
A_t_minus_1 = np.array([[1.0, 0, 0],
                        [0, 1.0, 0],
                        [0, 0, 1.0]])
state_estimate_t_minus_1 = np.array([0.0, 0.0, 0.0])
control_vector_t_minus_1 = np.array([4.5, 0.05])
process_noise_v_t_minus_1 = np.array([0.01, 0.01, 0.003])
yaw_angle = 0.0  # radians
delta_t = 1.0  # seconds
def getB(yaw, dt):
    B = np.array([[np.cos(yaw) * dt, 0],
                  [np.sin(yaw) * dt, 0],
                  [0, dt]])
    return B
def main():
    state_estimate_t = A_t_minus_1 @ state_estimate_t_minus_1 + getB(yaw_angle, delta_t) @ control_vector_t_minus_1 + process_noise_v_t_minus_1
    print(f'State at time t-1: {state_estimate_t_minus_1}')
    print(f'Control input at time t-1: {control_vector_t_minus_1}')
    print(f'State at time t: {state_estimate_t}')  # State after delta_t seconds
main()
