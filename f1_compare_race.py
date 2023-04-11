import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()

race = fastf1.get_session(2023, 'Bahrain Grand Prix', 'R')
race.load()

ver = race.laps.pick_driver('VER')
ham = race.laps.pick_driver('HAM')
alo= race.laps.pick_driver('ALO')

fig, ax = plt.subplots()
ax.plot(ver['LapNumber'], ver['LapTime'], color='red', label='VER')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan', label='HAM')
ax.plot(alo['LapNumber'], alo['LapTime'], color='green', label='ALO')
ax.set_title("VER vs ALO vs HAM \n2023 Bahrain GP")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()