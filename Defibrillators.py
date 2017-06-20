import math

lon, lat = input(), input()
lon, lat = float(lon.replace(",", ".")), float(lat.replace(",", "."))
n, ans, values, defib = int(input()), {}, [], []


def calc(dlatx, dlonx, val):
    global values, lon, lat, ans
    x = (dlonx-lon)*(math.cos((lat+dlatx)/2))
    y = (dlatx-lat)
    d = math.sqrt(math.pow(x, 2)+math.pow(y, 2))*6371
    values += [d]
    ans[d] = val

for i in range(n):
    defib += [input()]

for defibb in defib:
    dlat, dlon = defibb.split(";")[-1].replace(",", "."), defibb.split(";")[-2].replace(",", ".")
    calc(float(dlat), float(dlon), defibb.split(";")[1])

print(ans[min(values)])
