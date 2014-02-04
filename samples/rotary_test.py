# Sample code for both the RotaryEncoder class and the Switch class.
# The common pin for the encoder should be wired to ground.
# The sw_pin should be shorted to ground by the switch.

# Output looks like this:
#
#    A B STATE SEQ DELTA SWITCH
#    1 1   3    2    1    0
#    0 1   2    3    1    0
#    0 0   0    0    1    0
#    1 0   1    1    1    0
#    1 1   3    2    1    0
#    0 1   2    3    1    0

import gaugette.rotary_encoder
import gaugette.switch
import math

if gaugette.platform == 'raspberrypi':
    A_PIN  = 7
    B_PIN  = 9
    SW_PIN = 8
else: # beaglbone
    A_PIN  = "P9_13"
    B_PIN  = "P9_14"
    SW_PIN = "P9_15"

encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)

last_state = None
last_switch_state = None
last_delta = 0
last_sequence = encoder.rotation_sequence()
last_heading = 0

# for coarser granularity reading
steps_per_cycle = 4 # arbitrary, usually equal to steps per detent
remainder = steps_per_cycle//2


# NOTE: the library includes individual calls to get
# the rotation_state, rotation_sequence and delta values.  
# However this demo only reads the rotation_state and locally
# derives the rotation_sequence and delta.  This ensures that
# the derived values are based on the same two input bits A and B.
# If we used the library calls, there is a very real chance that
# the inputs would change while we were sampling, giving us 
# inconsistent values in the output table.

while True:

    state = encoder.rotation_state()
    switch_state = switch.get_state()

    if (state != last_state or switch_state != last_switch_state):
        last_switch_state = switch_state
        last_state = state

        # print a heading every 20 lines
        if last_heading % 20 == 0:
          print ("A B STATE SEQ DELTA CYCLES SWITCH")
        last_heading += 1

        # extract individual signal bits for A and B
        a_state = state & 0x01
        b_state = (state & 0x02) >> 1

        # compute sequence number:
        # This is the same as the value returned by encoder.rotation_sequence()
        sequence = (a_state ^ b_state) | b_state << 1

        # compute delta:
        # This is the same as the value returned by encoder.get_delta()
        delta = (sequence - last_sequence) % 4
        if delta == 3:
            delta = -1
        elif delta==2:
            # this is an attempt to make sense out of a missed step:
            # assume that we have moved two steps in the same direction
            # that we were previously moving.
            delta = int(math.copysign(delta, last_delta))
        last_delta = delta
        last_sequence = sequence

        remainder += delta
        cycles = remainder // steps_per_cycle
        remainder %= steps_per_cycle

        print ('%1d %1d %3d %4d %4d %4d %4d' % (a_state, b_state, state, sequence, delta, cycles, switch_state))
