# Content-aware frame interpolation (CAFI): Deep Learning-based temporal super-resolution for fast bioimaging

Link to the paper: [link](https://doi.org/10.1101/2021.11.02.466664)

## Usage for ZoomingSlowMo_4_Microscopy_V2.ipynb

1. Replace `/home/user2/project/CAFI` to your own path for the whole project including `ZoomingSlowMo_4_Microscopy_V2.ipynb` and `ZS4Mic/load_functions`.
2. This script is already adapted for Pytorch 1.11 and later. Run `python ZS4Mic/codes/models/modules/dcn/setup.py build develop` in the terminal to build the DCN module.
3. Run `python stack_tiff.py "path/to/tiff/dir" "ZS4Mic/demo/dirname/filename.tif"` to stack the tiff files into a single file.
4. Run the notebook `ZoomingSlowMo_4_Microscopy_V2.ipynb` to use the Zooming SlowMo model for microscopy. Only need to run `4. Training` to train the model, and `5. Perform Interpolation and/or Lateral Image upscaling` to perform the interpolation.
5. Run `python split_tiff.py "ZS4Mic/demo/dirname/filename.tif" "path/to/tiff/dir"` to split the tiff file into individual frames.

## What is this?
Content-aware frame interpolation (CAFI) provides a Deep Learning-based temporal super-resolution for fast bioimaging. It increases the frame rate of any microscope modality by interpolating an image in between two consecutive images via “intelligent” interpolation, providing a 2x increase in temporal or/and axial resolution. Here we provide the modified repositories of DAIN and Zooming SlowMo used in the CAFI 4 Microscopy Google Colab notebooks.

<table>
  <tr>
    <td colspan="1">
        <img src="dump/DEMO_GIF_GRAY640.gif" alt="Demo GIF">
        </img>
      </a>
    </td>
  </tr>
</table>

## Want to see a short video demonstration and user tutorials?

| Demonstration Video | Tutorial Video CAFI (DAIN) | Tutorial Video CAFI (ZS) |
|:-:|:-:|:-:|
| [![](https://github.com/mpriessner/CAFI/blob/main/dump/Demo_Video_Screenshot.JPG)](https://www.youtube.com/watch?v=4eCELi-b23k) | [![](https://github.com/mpriessner/CAFI/blob/main/dump/DAIN_Screenshot.JPG)](https://youtu.be/RyMQuRYtpbM) | [![](https://github.com/mpriessner/CAFI/blob/main/dump/ZS_Screenshot_.JPG)](https://youtu.be/xymw0ZRF8Xo) |

## Links to the notebooks and other sources

 DAIN 4 Microscopy:
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bL6wgTWrghHK7LH9xb4KGSk5WuOa5nJS?usp=sharing) | 
 
 [Original Github of DAIN](https://github.com/baowenbo/DAIN) | 
 [Source Paper 1](https://arxiv.org/abs/1904.00830)

 
 ZoomingSlowMo 4 Microscopy
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TZ0K-rq9Nrgu9_XZ0UOK6brxjIM0ISNU?usp=sharing) | 

 [Original Github of ZS](https://github.com/Mukosame/Zooming-Slow-Mo-CVPR-2020) | 
 [Source Paper 1](https://arxiv.org/abs/2002.11616#) | 
 [Source Paper 2](https://arxiv.org/abs/2104.07473#) 

Microscopy training and test data is available here:
[![DOI](dump/zenodo.5596603.svg)](https://zenodo.org/record/7396563)


## How to cite this work
Martin Priessner, David C.A Gaboriau, Arlo Sheridan, Tchern Lenn, Jonathan R. Chubb, Uri Manor, Ramon Vilar,
and Romain F. Laine

**Content-aware frame interpolation (CAFI): Deep Learning-based temporal super-resolution for fast bioimaging. bioRxiv, 2021.** 
DOI: [https://doi.org/10.1101/2021.11.02.466664](https://doi.org/10.1101/2021.11.02.466664)


<table>
  <tr>
    <td colspan="1">
        <img src="dump/TWEET_2_GIF_1_Paper_Screenshots.gif" alt="Demo GIF">
        </img>
      </a>
    </td>
  </tr>
</table>
