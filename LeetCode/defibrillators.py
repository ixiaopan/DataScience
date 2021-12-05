"""
Each defibrillator is represented by the following fields:
  Name
  Address
  Contact Phone number
  Longitude (degrees)
  Latitude (degrees)
These fields are separated by a semicolon (;).

return:
  The name of the defibrillator located the closest to the user’s position.
"""

import math


def dist_a_b(lon_a, lat_a, lon_b, lat_b):
  """
  distance between two points
  """
  
  lon_a = math.radians(lon_a)
  lat_a = math.radians(lat_a)
  lon_b = math.radians(lon_b)
  lat_b = math.radians(lat_b)

  x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
  y = lat_b - lat_a
  d = math.sqrt(x**2 + y**2) * 6371
  return d


def comma2decimal(v):
    return float(v.replace(',', '.'))


def defi(lon, lat, defibs):
  """
  Line 1: User's longitude (in degrees)
  Line 2: User's latitude (in degrees)
  Line 3: The number N of defibrillators located in the streets of Montpellier
  """
  lon = comma2decimal(lon)
  lat = comma2decimal(lat)

  min_d = math.inf
  nearest = None
  for defib in defibs:
    def_fields = defib.split(';')

    d = dist_a_b(lon, lat, comma2decimal(def_fields[-2]), comma2decimal(def_fields[-1]))
    if d < min_d:
      min_d = d
      nearest = def_fields[1]
  
  return nearest

