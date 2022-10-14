#!/usr/bin/python
# encoding: utf-8
import base64
import os
import re
import subprocess
import time

default_adb_path = os.getenv("HOME") + "/Library/Android/sdk/platform-tools/adb"

def get_tag():
    return "devtools"


def get_str_local_time(format_str="%Y-%m-%d-%H-%M-%S"):
    return time.strftime(format_str, time.localtime())


def exec_cmd(command):
    return subprocess.check_output(command, shell=True).decode('utf-8')


def get_path(exec_name):
    """
    获取工具路径
    :return: 路径
    """

    # todo 系统中的工具在workflows中不能直接使用，需要解决下路径找不到的问题
    which_path = os.getenv("which") if os.getenv("which") else ""

    command = which_path + " " + exec_name
    exec_dir = ""
    try:
        exec_dir = exec_cmd(command).replace("\n", "")
    except subprocess.CalledProcessError as e:
        pass

    return exec_dir


def get_adb_path():
    """
    获取可用adb路径
    :return: adb路径
    """
    if os.path.exists(default_adb_path):
        adb_dir = default_adb_path
    else:
        adb_dir = get_path("adb")
    return adb_dir if len(adb_dir) > 0 else "exec/adb"


def get_devices():
    """
    使用adb获取已连接设备信息
    :return:A list of devices. e.g. [(id, model),(id, model)]
    """

    command = get_adb_path() + ' devices -l'
    devices_str = exec_cmd(command)
    device_list = re.findall('(\\S*)\\s*device.*?model:(\\S*)', devices_str)
    return device_list


def encode_str(string):
    return base64.b64encode(string).decode("utf-8")


def decode_str(string):
    return base64.b64decode(string.encode())


def read_clipboard_str():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return p.stdout.read().decode("utf-8")


def read_image_to_clipboard(img_path):
    exec_cmd("exec/impbcopy " + img_path)
