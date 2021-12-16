#!/usr/bin/python
# encoding: utf-8
import sys

import utils
from workflow import Workflow3


def main(wf):
    args = wf.args

    device_list = utils.get_devices()
    if len(device_list) > 1:
        for device in device_list:
            wf.add_item(device[0], device[1], arg=device[0], valid=True)
    elif len(device_list) < 1:
        wf.add_item("没有找到可用设备，请确认设备已连接")
    else:
        scrcpy_dir = utils.get_path("scrcpy")
        print scrcpy_dir
        wf.add_item("没有安装scrcpy")

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
