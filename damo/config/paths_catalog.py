# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# Copyright (C) Alibaba Group Holding Limited. All rights reserved.
"""Centralized catalog of paths."""
import os


class DatasetCatalog(object):
    DATA_DIR = 'datasets'
    DATASETS = {
        'coco_2017_train': {
            'img_dir': 'coco/train2017',
            'ann_file': 'coco/annotations/instances_train2017.json'
        },
        'coco_2017_val': {
            'img_dir': 'coco/val2017',
            'ann_file': 'coco/annotations/instances_val2017.json'
        },
        'coco_2017_test_dev': {
            'img_dir': 'coco/test2017',
            'ann_file': 'coco/annotations/image_info_test-dev2017.json'
        },

        'AIHUB_updated_train': {
            'img_dir': 'AIHUB_updated/images/train',
            'ann_file': 'AIHUB_updated/annotations/AIHUB_updated_train.json'
        },        
        'wider_face_updated_train': {
            'img_dir': 'wider_face_updated/images/train',
            'ann_file': 'wider_face_updated/annotations/wider_face_updated_train.json'
        },
        'wider_face_updated_val': {
            'img_dir': 'wider_face_updated/images/val',
            'ann_file': 'wider_face_updated/annotations/wider_face_updated_val.json'
        }, 
        'crowd_train': {
            'img_dir': 'crowd/images/train',
            'ann_file': 'crowd/annotations/crowd_train.json'
        },
        'crowd_val': {
            'img_dir': 'crowd/images/val',
            'ann_file': 'crowd/annotations/crowd_val.json'
        },
        'coco_face_from_kpts_wholebody_train': {
            'img_dir': 'coco_face_from_kpts_wholebody/images/train',
            'ann_file': 'coco_face_from_kpts_wholebody/annotations/coco_face_from_kpts_wholebody_train.json'
        },
        'coco_face_from_kpts_wholebody_val': {
            'img_dir': 'coco_face_from_kpts_wholebody/images/val',
            'ann_file': 'coco_face_from_kpts_wholebody/annotations/coco_face_from_kpts_wholebody_val.json'
        },
        }

    @staticmethod
    def get(name):
    
        data_dir = DatasetCatalog.DATA_DIR
        attrs = DatasetCatalog.DATASETS[name]
        args = dict(
            root=os.path.join(data_dir, attrs['img_dir']),
            ann_file=os.path.join(data_dir, attrs['ann_file']),
        )
        return dict(
            factory='COCODataset',
            args=args,
        )
        return None
