# -*- coding: utf-8 -*-
'''
@File    : paddle_ocr.py
@Time    : 2024/04/11 16:32:00
@Author  : wty-yy
@Version : 1.0
@Blog    : https://wty-yy.xyz/
@Desc    : Based on Paddle OCR
'''

from paddleocr import PaddleOCR
from paddleocr.tools.infer.predict_system import TextSystem
import numpy as np
import logging
from pathlib import Path
import math
root_path = Path(__file__).parents[2]

onnx_weight_paths = {
  'det': root_path / './runs/ocr/ch_PP-OCRv4_det_infer.onnx',
  'rec': root_path / './runs/ocr/ch_PP-OCRv4_rec_infer.onnx',
  'cls': root_path / './runs/ocr/ch_ppocr_mobile_v2.0_cls_infer.onnx',
}

class OCR:
  def __init__(self, use_angle_cls=False, onnx=False, tensorrt=False, use_gpu=True, lang='ch'):
    self.use_angle_cls = use_angle_cls
    kwargs = dict(use_onnx=onnx, use_tensorrt=tensorrt, use_gpu=use_gpu)
    if onnx:
      kwargs.update({(k + '_model_dir'): str(v) for k, v in onnx_weight_paths.items()})
    self.ocr = PaddleOCR(use_angle_cls=use_angle_cls, show_log=False, lang=lang, **kwargs)
  
  def __call__(self, x: np.ndarray, det=True, rec=True, cls=False, bin=False, pil=True, gray=False):
    """
    Args:
      x (np.ndarray | path | list): img for OCR.
      det (bool): If taggled, use text position detection.
      rec (bool): If taggled, use text recognition.
      cls (bool): If taggled, the text rotation with 180 degrees will be recognized.
      bin (bool): If taggled, binarize img to gray.
      pil (bool): If taggled, image is RGB format.
      gray (bool): If taggled, image x has one color channel.
    Returns:
      [img1_info, img2_info, ...]:
        img{i}_info = [(det)_rec_info1, (det)_rec_info2, ...]:
          (det)_rec_info{i} = [(det_info,) rec_info]:
            det_info = [x0, y0, x1, y1]
            rec_info = ('rec_text', confidence)
    """
    if not pil and not gray:
      if isinstance(x, list):
        for i in range(len(x)):
          if isinstance(x[i], np.ndarray):
            x[i] = x[i][...,::-1]
      elif isinstance(x, np.ndarray):
        x = x[...,::-1]
    cls = cls & self.use_angle_cls
    # if x.ndim == 3: x = x[None,...]
    result = self.ocr.ocr(x, det=det, rec=rec, cls=cls, bin=bin)
    return result
  
  def process_part1(self, img_time, pil=False, show=False):
    results = self(img_time, pil=pil)[0]
    if show:
      import cv2
      print("OCR results:", results)
      cv2.imshow('time', img_time)
      cv2.waitKey(1)
    if results is None: return math.inf
    stage = m = s = None
    for info in results:
      det, rec = info
      rec = rec[0].lower()
      if 'left' in rec:
        stage = 0
      if 'over' in rec:
        stage = 1
      if (':' in rec) or ('：' in rec):
        m, s = rec.split(':' if ':' in rec else '：')
        try:
          m = int(m.strip())
          s = int(s.strip())
        except ValueError:
          m = s = None
    if stage is None or m is None or s is None: return math.inf
    t = m * 60 + s
    if stage == 0:
      return 180 - t
    return 180 + 120 - t

  def process_part3_elixir(self, img_part3, pil=False):
    from katacr.build_dataset.utils.split_part import extract_bbox
    from katacr.build_dataset.constant import part3_elixir_params
    img = extract_bbox(img_part3, *part3_elixir_params)
    results = self(img, pil=pil, det=False)
    for info in results:
      rec = info[0][0].lower()
      num = ''.join([c for c in rec.strip() if c.isnumeric()])
      try:
        m = int(num)
      except ValueError:
        m = None
    return m

def ocr_test(img, det=True, show_time=True, show_result=False, info=""):
  name = ""
  if isinstance(img, str):
    name = Path(img).name
    img = cv2.imread(img)
  result = ocr(img, det=det)
  with sw:
    result = ocr(img, det=det, pil=False)
  if show_time: print("time:", sw.dt)
  if show_result:
    print(name, result)
  if info: print(info)

def speed_test(ocr, ax, mn=1000, mx=737280, sample=100, name="", det=True):
  sw = Stopwatch()
  xs, ys = [], []
  for size in tqdm(range(mn, mx, (mx-mn)//sample)):
    tm = 0
    w = int(np.sqrt(size))
    img = np.ones((w, w, 3), np.uint8) * 255
    ocr(img, det=det)
    for i in range(10):
      with sw:
        ocr(img, det=det)
      tm += (sw.dt - tm) / (i + 1)
    xs.append(size)
    ys.append(tm)
  ax.plot(xs, ys, label=name)

if __name__ == '__main__':
  import matplotlib.pyplot as plt
  from tqdm import tqdm
  import cv2
  from katacr.utils import Stopwatch
  sw = Stopwatch()
  # ocr = OCR()
  ocr = OCR(onnx=True, use_gpu=False)
  # fig, ax = plt.subplots(figsize=(80, 40))
  # speed_test(ocr, ax, name='cpu')
  # ocr_paddle = OCR()
  # speed_test(ocr_paddle, ax, name='gpu')
  # plt.show()
  # ### Text recognition ###
  ocr_test("/home/yy/Pictures/ClashRoyale/ocr/text1.png", show_result=True, det=True)
  # ### Number recognition ###
  # ocr_test("/home/yy/Pictures/ClashRoyale/ocr/num1.png")
  # ### Bar recognition ###
  # ocr_test("/home/yy/Pictures/ClashRoyale/ocr/bar.png")
  # ### Back recognition ###
  # ocr_test("/home/yy/Pictures/ClashRoyale/ocr/test1.png")
  # ### Double Line ###
  # ocr_test("/home/yy/Pictures/ClashRoyale/ocr/double line.png")
  import time
  # time.sleep(10)

"""
onnx:
text1.png
time: 0.026895523071289062
num1.png
time: 0.0014867782592773438
bar.png
time: 0.024847745895385742
test1.png
time: 0.16593289375305176
double line.png
time: 0.02233743667602539

cpu:
text1.png
time: 0.0168914794921875
num1.png
time: 0.0011060237884521484
bar.png
time: 0.014077425003051758
test1.png
time: 0.10216093063354492
double line.png
time: 0.014042139053344727

paddle:
text1.png
time: 0.01307058334350586
num1.png
time: 0.004451751708984375
bar.png
time: 0.011927604675292969
test1.png
time: 0.03846144676208496
double line.png
time: 0.011073112487792969
"""