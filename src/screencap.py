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

    prefix = utils.get_tag() + "_" + device_info["device_name"] + "_" + utils.get_str_local_time()
    local_dir = "~/downloads"
    local_path = "%s/%s.png" % (local_dir, prefix)
    command = utils.get_adb_path() + " -s %s exec-out screencap -p > %s" % (
        device_info["device_id"], local_path)
    result = utils.exec_cmd(command)
    # 将截图拷贝到剪切板
    utils.read_image_to_clipboard(local_path)
    notify_title = "alfred手机截屏"
    notify(notify_title, ("截图已经复制到剪切板，本地保存路径%s" % local_dir))


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
