# Momento
## Implementation Details

Adapted implementation uses TensorFlow to train a fast style transfer network. 

Adapted from below citation
### Citation
```
 
@misc{engstrom2016faststyletransfer,
    author = {Logan Engstrom},
    title = {Fast Style Transfer},
    year = {2016},
    howpublished = {\url{https://github.com/lengstrom/fast-style-transfer/}},
    note = {commit xxxxxxx}
  }
```


### Requirements

You will need the following to run the above:

- TensorFlow 0.11.0

- Python 2.7.9, Pillow 3.4.2, scipy 0.18.1, numpy 1.11.2


- ffmpeg 3.1.3 if you want to stylize video


### Evaluating Style Transfer Networks
Use
 `evaluate.py` to evaluate a style transfer network. Run `python evaluate.py` to view all the possible parameters. Evaluation takes 100 ms per frame (when batch size is 1) on a Maxwell Titan X. Takes several seconds per frame on a CPU.

    python evaluate.py --checkpoint path/to/style/model.ckpt \
      --in-path dir/of/test/imgs/ \
      --out-path dir/for/results/



### Stylizing Video

Use `transform_video.py` to transfer style into a video. Run `python transform_video.py` to view all the possible parameters. Requires `ffmpeg`.

Example usage:

    python transform_video.py --in-path path/to/input/vid.mp4 \
      --checkpoint path/to/style/model.ckpt \
      --out-path out/video.mp4 \
      --device /gpu:0 \
      --batch-size 4

### evaluate.py
evaluate.py evaluates trained networks given a checkpoint directory. If evaluating images from a directory, every image in the directory must have the same dimensions.

Flags

--checkpoint: Directory or ckpt file to load checkpoint from. Required.\
--in-path: Path of image or directory of images to transform. Required.\
--out-path: Out path of transformed image or out directory to put transformed images from in directory (if in_path is a directory). Required.\
--device: Device used to transform image. Default: /cpu:0.\
--batch-size: Batch size used to evaluate images. In particular meant for directory transformations. Default: 4.\
--allow-different-dimensions: Allow different image dimensions. Default: not enabled


### transform_video.py
transform_video.py transforms videos into stylized videos given a style transfer net.

Flags

--checkpoint-dir: Directory or ckpt file to load checkpoint from. Required.\
--in-path: Path to video to transfer style to. Required\
--out-path: Path to out video. Required.\
--tmp-dir: Directory to put temporary processing files in. Will generate a dir if you do not pass it a path. Will delete tmpdir afterwards. Default: randomly generates invisible dir, then deletes it after execution completion.\
--device: Device to evaluate frames with. Default: /gpu:0.\
--batch-size: Batch size for evaluating images. Default: 4.\

[Trained Checkpoints here](https://drive.google.com/open?id=1vUO_TQl0CCueXhriw0_nWW7mOCO_xjYH). 
