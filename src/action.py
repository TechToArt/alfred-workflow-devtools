#!/usr/bin/python
# encoding: utf-8
import json
import sys

import utils
from workflow import Workflow
from workflow.notify import notify


def main(wf):
    args = wf.args

    # 因为直接传递json字符串会被截断，输入参数为经过编码后的json字符串
    device_info = json.loads(utils.decode_str(args[0]))
    clipboard_str = utils.read_clipboard_str().replace("&", "\\&")

    notify_title = "alfred打开app"
    # 读取到apk路径则进行安装
    if "://" in clipboard_str:
        command = utils.get_adb_path() + " -s %s shell am start \"%s\"" % (device_info["device_id"], clipboard_str)
        result = utils.exec_cmd(command)
        notify(notify_title, result)
    else:
        notify(notify_title, "剪切板中没有找到跳链")


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
