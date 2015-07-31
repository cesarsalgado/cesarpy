import datetime
import subprocess

def get_current_date_and_time_str():
    return datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S")

def get_screen_reso():
    return tuple(map(int, subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True,stdout=subprocess.PIPE).communicate()[0].strip().split('x')))
