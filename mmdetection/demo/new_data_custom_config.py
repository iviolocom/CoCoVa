_base_ = 'configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('steering wheel', 'cell phone', 'hat', 'bottle', 'control panel',)
data = dict(
    train=dict(
        img_prefix='data/train'),
        classes=classes,
        ann_file='data/train/annotation_coco.json',
    val=dict(
        img_prefix='data/val/',
        classes=classes,
        ann_file='balloon/val/annotation_coco.json'),
    test=dict(
        img_prefix='data/test/',
        classes=classes,
        ann_file='data/test/annotation_coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/faster_rcnn_r50_caffe_fpn_mstrain_3x_coco_20210526_095054-1f77628b.pth'
