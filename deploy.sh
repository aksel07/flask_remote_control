#!/bin/bash
ssh pi@aksel-pi.local -C killall python
scp app.py pi@aksel-pi.local:.
rsync -avz html pi@aksel-pi.local:.
ssh pi@aksel-pi.local -C python app.py
