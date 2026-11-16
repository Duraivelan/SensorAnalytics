#One-dimensional Kalman filter
def kalman(zs, q=1e-4, r=1e-2, x=0.0, p=1.0):
out = []
for z in zs:
p += q k = p / (p + r) x += k * (z - x) p *= (1 - k)
out.append(x)
return out
