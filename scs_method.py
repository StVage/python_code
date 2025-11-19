import matplotlib.pyplot as plt

def scs_method_cumulative(P_cum, CN, a=0.2):
    
    S = 25400.0 / CN - 254.0
    Ia = a * S

    if P_cum <= Ia:
        return 0.0

    Q = (P_cum - Ia)**2 / (P_cum - Ia + S)
    return Q



rain_hyetograph = [5, 12, 25, 10, 3, 0, 1]

CN = 75
a = 0.2


cumulative_rain = []
total_rain = 0
for P in rain_hyetograph:
    total_rain += P
    cumulative_rain.append(total_rain)

runoff = []
for P_cum in cumulative_rain:
    q = scs_method_cumulative(P_cum, CN, a)
    runoff.append(q)


hourly_runoff = []
previous = 0
for current in runoff:
    hourly = current - previous
    hourly_runoff.append(hourly)
    previous = current


print(f"{'Hour':>4} | {'P (mm)':>8} | {'Total P (mm)':>12} | {'Total Q (mm)':>12} | {'Q (mm)':>10}")
print("-" * 70)

for i in range(len(rain_hyetograph)):
    hour = i + 1
    P = rain_hyetograph[i]
    P_cum = cumulative_rain[i]
    Q_cum = runoff[i]
    Q_hour = hourly_runoff[i]
    print(f"{hour:>4} | {P:>8.2f} | {P_cum:>12.2f} | {Q_cum:>12.3f} | {Q_hour:>10.3f}")


# Plot rainfall and runoff
hours = list(range(1, len(rain_hyetograph) + 1))

plt.figure(figsize=(10, 6))
plt.plot(hours, rain_hyetograph, label="P (mm)")
plt.plot(hours, hourly_runoff, label="Q (mm)")
plt.xlabel("Time (h)")
plt.ylabel("Depth (mm)")
plt.title("Rainfall (P) and Runoff (Q) (mm)")
plt.legend()
plt.grid(True)

plt.show()
