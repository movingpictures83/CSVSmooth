# CSVSmooth
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 2.0, Python 3.6

PluMA plugin to smooth multiple CSV files and produce one final result.

Convenient when two separate datasets have been filtered and need to be
re-merged.

The first file is assumed to be the original dataset.
The second and third are assumed to be two subsets.

The plugin will keep all measurables in the original CSV file that
were in at least one of the two subset files.

It will output one final CSV file
