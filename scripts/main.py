#!/usr/bin/env python

import os
import sys
from datetime import date
from mavick import Mavick
from phantom import Phantom


srt_tuple = ("SRT", "srt")


input_argument = sys.argv[1]
srt_list = []


if input_argument.endswith(srt_tuple):
    srt_list.append(input_argument)
else:
    file_list = os.listdir(input_argument)

try:
    current_date = str(date.today())
    os.mkdir(f"Processed_SRT")
    os.mkdir(f"Processed_SRT/{current_date}")
except Exception as e:
    print("Error:", e)


for k in srt_list:
    if input_argument.endswith(srt_tuple):
        input_srt = f"{k}"
    else:
        input_srt = f"{input_argument}/{k}"

    output_srt = f"Processed_SRT/{current_date}/{k[0:len(k)-4]}_Processed.SRT"
