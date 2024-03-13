# Flight Delays Analysis

This Python script is designed to analyze flight data, particularly focusing on the number of flights and flight delays at various airports. The analysis is based on a dataset contained within a CSV file named `flights.csv`.

## Features

- **Count of Flights**: Calculates the total number of flights for each airport.
- **Flight Delays**: Calculates the total delay (in minutes) for flights at each airport.
- **Average Delay**: Determines the average delay per flight at each airport.

## Data Format

The script expects a CSV file with the following columns:

- Column 8 (`row[7]` in the code, 0-indexed): Airport name.
- Column 12 (`row[11]` in the code, 0-indexed): Flight delay in minutes. Positive values indicate a delay.


