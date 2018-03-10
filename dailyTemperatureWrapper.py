#!/bin/bash

###
# dailyTemperature wrapper by Fredrik Walløe
# This wrapper helps display font-awesome icons in polybar
###

temperature=$(python ./dailyTemperature.py)

if [[ $temperature < 0 ]];
then # display blue snowflake plus degrees if temperature is below 0
	echo -e ' %{F#a0ccff}%{F-}' $temperature 'C'
else # display an orange sun plus degrees if temperature is above 0
	echo -e ' %{F#ffb52a}%{F-}' $temperature 'C'
fi
