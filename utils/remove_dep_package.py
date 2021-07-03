"""
remove package with its dependencies
问题：所有依赖都卸载了，可能某些尚要使用的库 依赖缺失
"""

import os


def check_dependencies(module_name):
    """查看 module 依赖/被依赖
    torch
        requires: ['numpy']
        require_bys: ['torchviz', 'torchvision']
    """
    cmd = f'pip show {module_name}'
    with os.popen(cmd) as p:  # 得到 cmd 打印的内容
        depends = p.readlines()
        if not depends:
            return []
        requires = depends[-2].split(':')[-1].replace(' ', '').replace('\n', '').strip()
        if requires:
            requires = requires.split(',')
        return requires


def remove_module(module_name):
    """
    递归卸载相关模块
    """
    # 先递归删除依赖
    requires = check_dependencies(module_name)
    if requires:
        for module in requires:
            remove_module(module)
    # 再删除最上层包，自下而上
    os.system(f'pip uninstall -y {module_name}')  # -y 强制选择 yes


if __name__ == '__main__':
    remove_module('torchvision')
    pass
