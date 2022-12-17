import re


file = open('day16_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

flow_rates = dict()
# (valve, flow rate, tunnels)
for line in lines:
    m = re.search(r".*tunnel leads to valve (.+).*", line)
    if m is not None:
        tunnels = m.group(1).split(', ')

        m = re.search(r".*rate=(\d+).*", line)
        if m is not None:
            flow_rates[line[6:8]] = (int(m.group(1)), tunnels)

num_non_zero_flows = 0
for flow in flow_rates:
    if flow[0] != 0:
        num_non_zero_flows += 1
def get_max_flow_rate(time_remaining, flow_rate, pressure_sum_total, valve_opened, current_valve, flow_rates_2, visited):
    if time_remaining == 0:
        return pressure_sum_total



    if time_remaining < 23 and 'HS' not in valve_opened:
        return 0 # not this path

    if len(valve_opened) == num_non_zero_flows:
        return pressure_sum_total + (time_remaining * flow_rate)

    pressure_sum_total += flow_rate

    # either open it or don't open it.
    # if we open it, we can only open it once.

    max_pressure_sum = 0
    if flow_rates_2[current_valve][0] != 0 and current_valve not in valve_opened:
        # open valve
        new_flow_rate = flow_rate + flow_rates_2[current_valve][0]
        valve_opened.add(current_valve)
        pressure = get_max_flow_rate(time_remaining - 1, new_flow_rate, pressure_sum_total, valve_opened, current_valve, flow_rates_2, set())
        max_pressure_sum = max(pressure, max_pressure_sum)
        valve_opened.remove(current_valve)

    # don't open valve
    visited.add(current_valve)
    for valve in flow_rates_2[current_valve][1]:
        if valve not in visited:
            pressure = get_max_flow_rate(time_remaining - 1, flow_rate, pressure_sum_total, valve_opened, valve, flow_rates_2, visited)
            max_pressure_sum = max(pressure, max_pressure_sum)
    visited.remove(current_valve)
    return max_pressure_sum

a = get_max_flow_rate(26, 0, 0, set(), 'AA', flow_rates, set())
print(a)
