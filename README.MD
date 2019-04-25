# CrysalisTabbiner - filter of tabbin files
## Introduction
Purpose of the program to filter certain peaks from Rigaku Crysalis (former Oxford) .tabbin files.
These files contain information on a peak table from a single crystal data sets.

High pressure diamond anvil data sets collected at Perkin-Elmer XRD or Varex detectors 
can be biased by the strong reflections from diamonds. Since these detectors are built on scintillator technology, 
it takes time for the scintillator to go to the ground state.
 
As a result there could be peaks on data frames which hold residual intensity from strong diamond reflections which dissapear slowly.
The intensity drops off slowly and single crystal data sets contain arcs in the reciprocal space, which can be filtered.

A video introduction will follow shortly.

## Algorithm
Program reads .tabbin files of Crysalis.
The later can be created with a command __wd t__ of Crysalis. 

User can select binning to group reflections upon reading the file and area (radius parameter) to enhance the filtering further.

One can convert either:
1. File by file by specifying the input and the output files. 
Each time the input file name is selected, the program starts an watchdog thread with 5 levels below the folder of the selected file.
New files, if created will appear in the combobox on the top of the interface. 

2. New files appearing in a directory and the subdirectories. Select the parent directory on the top of the interface.

The main part of the code is demonstrated in the [examples](CrysalisLibraryExamples/) section.

## Backend
The program heavily relies on the _numpy_ and _watchdog_.

## Installation
The user will require the following libraries

Common libs:
    
    os, path, struct, time, math, re

Special libs required for operation:

    pip install qtpy PySide2 watchdog
    conda install qtpy PySide2 watchdog

Script is working under python 3.6 (PySide2) and can be compacted with lx_Freeze to an executable.
In order to avoid having a terminal window, please use the __.VBS__ file provided as a startup link.

Experienced users can also use [bat2exe]( http://www.f2ko.de/de/b2e.php ) converter.

## Releases
The current [release](releases/) is 0.1.0 which is compatible with Crysalis 39.46 and some versions below.
