# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/5/26 20:35 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi

from scipy.io.wavfile import write

from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

text = '待合成文本'
model_id = 'speech_tts/speech_sambert-hifigan_tts_ainan_zh-cn_16k'
sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id, model_revision='v1.0.0')
output = sambert_hifigan_tts(input=text)
pcm = output[OutputKeys.OUTPUT_PCM]
write('output.wav', 16000, pcm)