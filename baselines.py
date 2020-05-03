from keras_segmentation.models.unet import vgg_unet

model = vgg_unet(n_classes=256, input_height=512, input_width=512)

model.train(
    train_images = 'data/membrane_rgb/train/image',
    train_annotations = 'data/membrane_rgb/train/label',
    checkpoints_path = 'checkpoints/',
    epochs = 3,
    steps_per_epoch = 300
)

out = model.predict_multiple(
    inp_dir='data/membrane_rgb/test/',
    out_dir="data/membrane_rgb/pred/"
)