"""Settings for the Bhote Koshi–Trishuli gauge monitor.

Every threshold here is a working assumption, not a calibrated value.
They are kept in one place so they can be argued with and changed.
"""

SOURCE_URL = "https://www.dhm.gov.np/hydrology/floodMonitoring"
SOURCE_NAME = "Department of Hydrology and Meteorology (DHM), Government of Nepal"

# Corridor stations, ordered upstream to downstream. IDs are DHM station IDs
# as used in https://www.dhm.gov.np/hydrology/hms-Single/<id>.
# "role" is descriptive only: mainstem gauges sit on the river that carried the
# flood; tributary gauges sit on side streams joining it.
CORRIDOR = [
    {"id": 4913, "label": "Bhotekoshi at Rasuwagadi", "role": "mainstem, near the China border"},
    {"id": 191, "label": "Bhote Koshi at Shyaprubesi", "role": "mainstem"},
    {"id": 4657, "label": "Trishuli Khola at Dhunche", "role": "tributary"},
    {"id": 52, "label": "Trishuli at Betrawati", "role": "mainstem"},
    {"id": 4783, "label": "Trishuli River at Betrawati", "role": "mainstem (second listing)"},
    {"id": 4658, "label": "Phalakhu Khola at Betrawati", "role": "tributary"},
    {"id": 5705, "label": "Trishuli at Galchi", "role": "mainstem"},
    {"id": 4781, "label": "Trishuli River at Kali Khola", "role": "mainstem"},
    {"id": 4661, "label": "Trishuli River at Bhorle", "role": "mainstem"},
]

# Silence thresholds, in minutes since the station's latest reading.
# DHM's feed shows readings stamped every 5-10 minutes at working stations;
# that cadence is observed, not documented, so these are assumptions.
LATE_AFTER_MIN = 60
SILENT_AFTER_MIN = 6 * 60

# Rapid-rise check: flag a rise of at least RISE_M metres within RISE_WINDOW_MIN.
# Uncalibrated placeholder. A real threshold needs each station's rating
# history and flood record.
RISE_M = 0.5
RISE_WINDOW_MIN = 60

# How much corridor history the status page charts.
CHART_HOURS = 48

# The project runs unattended until this moment (UTC), then stops requesting
# data from DHM and relabels the status page as an archive. Extend it here.
END_AT = "2027-01-21T00:00:00+00:00"

# Retries for a failed request to DHM before the check is recorded as a source error.
FETCH_ATTEMPTS = 3
FETCH_BACKOFF_S = 20
