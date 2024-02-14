# Sewiov
This python script is for analyzing time-series data, focusing on tracking and calculating durations between entry and exit events across various zones.

# Time-Series Data Analysis Tool

## Overview
This project provides a Python tool for analyzing time-series data related to entry and exit times across different zones and feeds. It reads data from a text file, groups entries by identifiers, and calculates the duration between 'in' and 'out' statuses.

## Features
- Data import from text files.
- Grouping data by feed and zone identifiers.
- Time difference calculation for each grouped entry.
- Data integrity checks through assertions.
- Visualization support using seaborn and matplotlib.

## Requirements
- Python 3.x
- Pandas
- Numpy
- Seaborn
- Matplotlib

## Usage
Ensure you have the required libraries installed, then run the script with your data file named `probe.txt` in the same directory.
