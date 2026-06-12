import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def draw_line(vec1: np.ndarray, vec2: np.ndarray, n: int):
    global fig, ax
    
    if(vec1[0] > vec2[0]):
        vec1, vec2 = vec2, vec1
        
    ls = np.linspace(vec1[0], vec2[0], n)
    xp = np.array([vec1[0], vec2[0]])
    yp = np.array([vec1[1], vec2[1]])
    d = np.interp(ls, xp, yp)    
    
    ax.plot(ls, d)

interp_sz = 10

vec1 = np.array([1,2])
vec2 = np.array([2,1])

tang = vec1 - vec2
tang3d = np.array([tang[0], tang[1], 0.0])
norm3d = np.cross(np.array([tang[0], tang[1], 0]), np.array([0, 0, 1]))
norm = norm3d[0:2]

vec_norm_start = vec2 + (tang / 2)

draw_line(vec1, vec2, interp_sz)
draw_line(vec_norm_start, vec_norm_start + norm, interp_sz)

scale = np.array([2.0, 3.0, 1.0])
scale_inv = 1 / scale

scale_mat = np.diag(scale)
scale_mat_trans_inv =  np.diag(scale_inv)

tang3d_scaled = scale_mat @ tang3d.transpose()
norm3d_scaled = scale_mat_trans_inv @ norm3d.transpose()

tang_norm_dot = np.dot(tang3d, norm3d) # 0
tang_norm_scaled_dot = np.dot(tang3d_scaled, norm3d_scaled) # 0

print(tang_norm_scaled_dot)

plt.show()

