import matplotlib.pyplot as plt
import numpy as np

def draw_line(vec1: np.ndarray, vec2: np.ndarray, n: int, ax : plt.Axes): 
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

scale = np.array([2.0, 2.0, 1.0])

lserr = np.linspace(0, 10, 100)
err_array = np.empty(np.size(lserr))

err_array

for idx, i in enumerate(lserr):
    curr_scale = scale.copy()
    curr_scale[1] += i
    scale_inv = 1 / curr_scale

    scale_mat = np.diag(curr_scale)
    scale_mat_trans_inv =  np.diag(scale_inv)

    tang3d_scaled = scale_mat @ tang3d.transpose()
    norm3d_scaled = scale_mat @ norm3d.transpose()
    norm3d_scaled_fix = scale_mat_trans_inv @ norm3d.transpose()

    tang_norm_dot = np.dot(tang3d, norm3d) # 0
    tang_norm_scaled_dot_fix = np.dot(tang3d_scaled, norm3d_scaled_fix) # 0
    tang_norm_scaled_dot = np.dot(tang3d_scaled, norm3d_scaled) # ?

    norm_normfix_dot = np.dot(norm3d_scaled_fix, norm3d_scaled)
    
    err_array[idx] = norm_normfix_dot

fig, (ax1, ax2) = plt.subplots(1, 2)
draw_line(vec1, vec2, interp_sz, ax1)
draw_line(vec_norm_start, vec_norm_start + norm, interp_sz, ax1)

ax2.plot(lserr, err_array)
plt.show()

