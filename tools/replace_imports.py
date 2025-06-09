#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2025/06/09 22:08:34
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)
# @Desc    : None


import os
import re


def replace_imports_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 定义需要替换的模块映射
    module_mapping = {
        "data_provider": "tslib.data_provider",
        "exp": "tslib.exp",
        "layers": "tslib.layers",
        "models": "tslib.models",
        "utils": "tslib.utils",
    }

    # 对每个模块进行替换
    new_content = content
    for old_module, new_module in module_mapping.items():
        new_content = re.sub(
            rf"from\s+{old_module}(\s|\.)", rf"from {new_module}\1", new_content
        )

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {file_path}")


def main():
    for root, _, files in os.walk("./tslib"):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                replace_imports_in_file(file_path)


if __name__ == "__main__":
    main()
