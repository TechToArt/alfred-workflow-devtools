#!/usr/bin/python
# encoding: utf-8
import json
import sys

import utils
from workflow.notify import notify
from workflow import Workflow3


def main(wf):
    args = wf.args

    # 因为直接传递json字符串会被截断，输入参数为经过编码后的json字符串
    device_info = json.loads(utils.decode_str(args[0]))

    prefix = utils.get_tag() + "_" + device_info["device_name"] + "_" + utils.get_str_local_time()
    command = utils.get_adb_path() + " -s %s exec-out screencap -p > ~/downloads/%s.png" % (
        device_info["device_id"], prefix)
    result = utils.exec_cmd(command)
    notify(result)


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
