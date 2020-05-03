from keras_segmentation.models.unet import vgg_unet

model = vgg_unet(n_classes=2, input_height=512, input_width=512)

model.train(
    train_images =  'data/membrane/train/image',
    train_annotations = 'data/membrane/train/aug',
    epochs=5
)

out = model.predict_multiple(
    inp_dir='data/membrane/test/',
    out_dir="data/membrane/pred/"
)