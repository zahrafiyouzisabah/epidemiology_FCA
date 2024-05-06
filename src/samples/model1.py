# MODEL1
c1_s = ["S"]
c1_i = ["I"]
c1_r = ["R"]
c1_v = ["V_1"]

# [from, to, parameters, contact?]
f1_si = [c1_s, c1_i, ["x"]]
f1_ir = [c1_i, c1_r, ["y"]]
f1_rv = [c1_r, c1_v, ["z"]]

model1 = {
    'compartments': [c1_s, c1_i, c1_r, c1_v],
    'flows': [f1_si, f1_ir, f1_rv]
}
