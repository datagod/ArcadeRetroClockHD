#!/bin/bash
echo ""
echo ""
echo "--------------------------------------------------------"
ip addr
echo "--------------------------------------------------------"
echo ""
echo ""


IsRunning=$(ps -aux | grep -c '[P]acDot' )

echo "IsRunning: ${IsRunning}"

if [[ $IsRunning -gt "0" ]]; then
    echo ""
    echo "--------------------------------------------------------"
    echo "It seems that the clock is already running! Kill the existing process before running again: sudo kill `pidof -x $(basename $0) -o %PPID`"
    echo "--------------------------------------------------------"
    exit
fi



cd ArcadeRetroClock
#CPU Modifier - used to regulate speed of certain games
# 1 = Raspberry Pi Zero
# 2 = Raspberry Pi A
# 3 = Raspberry Pi 2
# 10 = Raspberry Pi 3B+ ?


# HD UNICORN
#mainsleep flashsleep scrollsleep NightModeStart NightModeDuration(hours) CPUModifier GAMMA
#sudo python3 PacDotHD2.py 0.07 0.01 0.08 23 7 7  1.5


#This is a test to restart if an error occurs
#(sudo python3 PacDotHD2.py 0.07 0.01 0.08 23 7 7  1.5)  ||  (sudo python3 PacDotHD2.py 0.07 0.01 0.08 23 7 7  1.5)

#(sudo python3 PacDotHD2.py 0.07 0.01 0.08 23 7 7  1.5)  ||  (source ../go.sh)
sudo python3 ArcadeRetroClockHD.py 0.07 0.01 0.08 23 7 1 1.75

