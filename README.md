# Greenhouse Timer

A simple Python program that automatically turns greenhouse lights on and off based on the time of day, and is intended to turn into a full app for controlling greenhouse lights.

## How it currently works

- Every 30 seconds, the program checks the current local time and decides whether the lights should be on or off.
- The decision comes from the clock each time, so it stays correct after crashes, reboots, or missed checks.
