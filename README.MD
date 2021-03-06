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

User can select binning to group individual reflections the reading file and area (radius parameter) to enhance the filtering.

User can convert either:
1. File by file by specifying the input and the output files. 
Each time the input file name is selected, the program starts an watchdog thread with 5 levels below the folder of the selected file.
New files, if created will appear in the combobox on the top of the interface. 

2. New files appearing in a directory and the subdirectories. Select the parent directory on the top of the interface.

The main operating part of the code is demonstrated in the [examples](CrysalisLibraryExamples/) section.

## Backend
The program heavily relies on the _numpy_ and _watchdog_.

## Installation
The user will require the following libraries

Common libs:
    
    os, path, struct, time, math, re

Special libs required for operation:

    pip install qtpy PySide2 watchdog numpy
    conda install qtpy PySide2 watchdog numpy

Script is working under python 3.6 (PySide2) and can be compacted with _lx_Freeze_ to an executable.
In order to avoid having a terminal window appearing, please use the __.VBS__ file provided as a startup link.

Experienced users can also use [bat2exe]( http://www.f2ko.de/de/b2e.php ) converter.

I have tried to clean the size as best as I could (28Mb in compressed __.7z__ release). Most of the size is taken by _numpy_ and a cleaned version of _PySide2_.

## Releases
The current [release](releases/) is 0.2.0 which is compatible with Crysalis 39.46 and some versions below.

    0.1.0-0.2.0 [2019-04-25] First upload and customization of the user experience, additional filtering of artifacts appearing due to the reading electronics (stripes in a frame)

## Illustrations
The raw and filtered data with 0.2.0
![raw and converted](CrysalisLibraryExamples/images/before_and_after.png)

## Acknowledgements
Many thanks to the [Vaclav Petricek](https://www.fzu.cz/en/prizes/dr-vaclav-petricek-has-received-the-barrett-award) for the initial information on the structure of the Crysalis .tabbin files (peak groups and the corresponding data offsets were discovered independently).

Many thanks to Rigaku Crysalis team (former Oxford Crysalis) offering a state of the art software for single crystal data solution.