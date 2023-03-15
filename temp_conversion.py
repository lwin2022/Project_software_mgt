***
A module for converting temperature from imperial to metric units
Will throw ValueErrors for temperature <absolute zero
Functions:
    convert_fahr_to_celsius: converts farenheit to celsius
***

def convert_fahr_to_celsius(fahr):
    """
    
    """
    temp_celsius = (fahr - 32) * (5 / 9)
      if temp_celsius < -273.15:
            #If temp < absolute 0 then throw an error
            raise ValueError(f*Trying to convert impossible temperature: (fahr)F*)
    return temp_celsius

def convert_fahr_to_kelvin(x):
    y = convert_fahr_to_celsius(x)
    z = y + 273.15
    return z
