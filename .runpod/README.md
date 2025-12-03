# [waifu2x](https://github.com/nagadomi/nunif/tree/master/waifu2x) - Runpod Serverless endpoint

[![Runpod](https://api.runpod.io/badge/LarveyOfficial/waifu2x-runpod)](https://console.runpod.io/hub/LarveyOfficial/waifu2x-runpod)

---

## What is it?
waifu2x is an Image Super-Resolution for Anime-Style Art created by [nagadomi](https://github.com/nagadomi).

This fork is simply an implementation of waifu2x for use on Runpod.

## How to use

### Example
```json
{
  "input": {
    "model_type": "art",
    "image": "https://raw.githubusercontent.com/nihui/waifu2x-ncnn-vulkan/master/images/0.jpg",
    "method": "scale4x",
    "noise_level": 3,
    "tile_size": 256,
    "batch_size": 4
  }
}
```

| Parameter   | Default | Options                                                            |
|-------------|---------|--------------------------------------------------------------------|
| image       | n/a     | url to image                                                       |
| model_type  | `art`   | `art`,`art_scan`, `photo`                                          |
| method      | `scale` | `noise`: 1x denoising, `scale`, `scale2x`, `scale4x`               |
| noise_level | `-1`    | `-1`: none, `0-3`: denoising level                                 |
| tile_size   | `256`   | Tile size                                                          |
| batch_size  | `4`     | Batch size                                                         |
| keep_alpha  | `True`  | When `False` is specified, the alpha channel will be dropped.      |
| amp         | `True`  | When `False` is specified, performs in FP32 mode. FP16 by default. |



![waifu2x demo](https://raw.githubusercontent.com/nagadomi/waifu2x/master/images/slide.png)