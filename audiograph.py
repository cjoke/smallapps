#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import struct
import time

# Konstantene
CHUNK = 256 * 2             # Samples per frame
FORMAT = pyaudio.paInt16     # Audio format
CHANNELS = 1                 # Single channel for microphone
RATE = 48000                 # Samples per second

# Start PyAudio
p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots(1, figsize=(15, 7))

# Variable for plotting
x = np.arange(0, 2 * CHUNK, 2)       # Samples (waveform)
xf = np.linspace(0, RATE, CHUNK)     # Frequencies (spectrum)

# Create a line object with random data
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# Basic formatting for the axes
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# Show the plot
plt.show(block=False)

print('stream started')

# For measuring frame rate
frame_count = 0
start_time = time.time()

while True:
    # Binary data
    data = stream.read(CHUNK)  
    
    # Convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    
    # Create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128
    
    line.set_ydata(data_np)
    
    # Update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
        
    except RuntimeError as e:
        print(e) # Runtime error handling

        # Calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)
        
        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break
