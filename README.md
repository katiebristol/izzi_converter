# Generic IZZI Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Purpose

This script was created to convert individual sample files previously
made by Data Splitter into generic PmagPy format for IZZI paleointensity experiments.
Files produced by this script can be used with PmagPy and paleointensity.org. 
Field intensity is output in A/m assuming a sample volume of 10cc. 

![Demo data.](/assets/input-output.png)

## How to use

1) Put individual sample files (such as those split by [Data Splitter](https://github.com/katiebristol/data_splitter)) that you want 
converted into the /input/ folder.
2) Run the script
3) Check the /output/ folder for your converted files. 

## Inputs

This script requires .dat files that you want converted placed into the
/input/ folder. 

## Outputs

This script will create converted files with the same name. 
The converted files will write to the /output/ folder. 

## Notes

This script was made in conjunction with the Data Splitter script.
It is intended to be used afterwards to convert data to PmagPy generic/paleointensity.org friendly formats.

## License

This script is published under the [MIT license](LICENSE.txt).