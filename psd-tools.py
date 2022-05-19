# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2022-04-30 15:44:23.645151
# @file_path "D:\CPS\MyProject\test"
# @Filename "s.py"
# @Description: 功能描述
#

from typing import *
from psd_tools import PSDImage
from os import path

from psd_tools.psd import PSD

class TLayerInfo(TypedDict):
    name:str
    size:list[int]
    layer_type:str
    layer_id:int
    has_mask:bool

def get_font_layer_info(layer):
    if layer.kind != 'type': return
    print(dir(layer))
    print("layer.text: ", layer.text)
    print('layer.kind: ', layer.kind)

def get_smart_object_info(layer):
    if layer.smart_object.is_psd():
        with layer.smart_object.open() as f:
            print('\n')
            print(f'打开智能对象【 {layer.smart_object.filename} 】: ')
            smart_object = PSDImage.open(f)
            for each in smart_object:
                get_layer_info(each)
            print('\n')

    # print(dir(layer.smart_object))

def get_group_info(group):
    for layers in group:
        get_layer_info(layers)


def get_layer_info(layer, only_visible:bool=False) -> 'TLayerInfo':
    if only_visible and layer.visible == False: return
    print(f'Open Layer: {layer.name}')
    res = {
        'visible':layer.is_visible(),
        'name':layer.name,
        "size":layer.size,
        'layer_type':layer.kind,
        'has_mask':layer.has_mask(),
        "layer_id":layer.layer_id
    }

    # print(res)
    match str(layer.kind):
        case 'group':
            get_group_info(layer)
        case 'smartobject':
            get_smart_object_info(layer)
        case 'type':
            print(f'【！发现文字图层！】:')
            get_font_layer_info(layer)

    return res

if ( __name__ == "__main__"):
    target = path.abspath(r'./test_file/3.psd')
    psd = PSDImage.open(target)
    p = PSD.open(target)

    print(f'根图层数量({len(psd)})')
    print(f'{p.linked_layer}')
    for layer in psd:
        get_layer_info(layer)

    print('\n')
    # print(dir(psd[0]))



    # psd.composite().save('example.png')
