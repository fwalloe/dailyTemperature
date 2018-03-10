# dailyTemperature
A polybar module that uses public Norwegian meterological data to display the temperature from a local temperature measuring station in Oslo. 

You'll need an API key to use this module: https://data.met.no/auth/requestCredentials.html

Integrate it in polybar with:


; Daily temperature

[module/dailyTemperature]
type = custom/script

exec = SCRIPTLOCATION/dailyTemperatureWrapper.sh

interval = 60

;script sets icon and color depending on status 

format = <label>
label = %output%
