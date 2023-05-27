# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/5/26 20:35 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
#
from paddlespeech.cli.tts.infer import TTSExecutor
tts = TTSExecutor()
tts(text="今天天气十分不错。", output="output.wav")


from paddlespeech.cli.tts.infer import TTSExecutor

tts = TTSExecutor()
tts.am = 'fastspeech2_csmsc'
tts.am_config = 'path/to/acoustic_model_config.yml'
tts.am_ckpt = 'path/to/acoustic_model_checkpoint.pdparams'
tts.am_stat = 'path/to/acoustic_model_stats.txt'
tts.phones_dict = 'path/to/phones_dict.txt'
tts.voc = 'hifigan_csmsc'
tts.voc_config = 'path/to/vocoder_config.yml'
tts.voc_ckpt = 'path/to/vocoder_checkpoint.pdparams'
tts.voc_stat = 'path/to/vocoder_stats.txt'
tts.lang = 'en'
tts.device = 'gpu'
tts.fs = 22050

tts(text="今天天气十分不错。", output="output.wav")
