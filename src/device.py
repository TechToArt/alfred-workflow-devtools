#!/usr/bin/python
# encoding: utf-8
import json
import sys

import utils
from workflow import Workflow


def main(wf):
    # 多个组件会调用该脚本，调用脚本时传入来源字段
    source = wf.args[0] if len(wf.args) else ""

    device_list = utils.get_devices()

    for device in device_list:
        # 组件中进行传值有逗号会被截断，编码后进行传值
        arg = utils.encode_str(json.dumps({"device_id": device[0], "device_name": device[1]}).encode())
        if source == "device":
            arg = device[0]
        wf.add_item(device[0], device[1], arg=arg, valid=True)

    if len(device_list) == 0:
        wf.add_item("未找到Android设备", "请检查设备链接是否正常", valid=False)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
