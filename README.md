# Pharmmapper-Mass-Docker

## Introduction
A script that enables a session of multiple inverse docking of given ligands to the receptors given by queried Pharmmapper job.

## Prerequisites
Downloaded and installed Python 3 and downloaded AutoDock Vina 1.1.2

## Installation
Download the script and extract it to a given folder.
Copy the desired version of AutoDock Vina and paste it in lib folder of the script

## Usage
```
./wrapper.sh <url>
```
Where `<url>` represents the link to a completed Pharmmapper job.

Ligands to be docked are to be put in the same folder where the script is extracted to.
