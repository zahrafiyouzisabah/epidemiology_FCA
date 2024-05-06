# MODEL2
c2_s = ["S"]
c2_i = ["I"]
c2_r = ["R"]
c2_v = ["V_2"]

# [from, to, parameters, contact?]
f2_si = [c2_s, c2_i, ["a"]]
f2_ir = [c2_i, c2_r, ["b"]]
f2_rv = [c2_r, c2_v, ["c"]]

model2 = {
    'compartments': [c2_s, c2_i, c2_r, c2_v],
    'flows': [f2_si, f2_ir, f2_rv]
}

# MODEL2
# c2_sf = ["S_F"]
# c2_if = ["I_F"]
# c2_rf = ["R_F"]
# c2_sm = ["S_M"]
# c2_im = ["I_M"]
# c2_rm = ["R_M"]

# # [from, to, parameters, contact?]
# f2_sif = [c2_sf, c2_if, ["a"]]
# f2_irf = [c2_if, c2_rf, ["b"]]

# f2_sim = [c2_sm, c2_im, ["c"]]
# f2_irm = [c2_im, c2_rm, ["d"]]

# model2 = {
#     'compartments': [c2_sf, c2_if, c2_rf, c2_sm, c2_im, c2_rm],
#     'flows': [f2_sif, f2_irf, f2_sim, f2_irm]
# }

# MODEL2
# c2_s = ["S"]
# c2_i = ["I"]
# c2_r = ["R"]

# # [from, to, parameters, contact?]
# f2_si = [c2_s, c2_i, ["a"]]
# f2_ir = [c2_i, c2_r, ["b"]]

# model2 = {
#     'compartments': [c2_s, c2_i, c2_r],
#     'flows': [f2_si, f2_ir]
# }
