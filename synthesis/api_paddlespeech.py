# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/5/4 22:31
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi

from fastapi import APIRouter, Query, BackgroundTasks
from fastapi.responses import FileResponse
from paddlespeech.cli.tts.infer import TTSExecutor
from tempfile import NamedTemporaryFile
import os

SUMMARY = "语音合成"
POST_DESCRIPTION = "语音合成API\n"

paddlespeech_router = APIRouter()

def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)


AM_MODEL_IDS = [
    'speedyspeech_csmsc',
    'fastspeech2_csmsc',
    'fastspeech2_aishell3',
    'fastspeech2_mix',
    'tacotron2_csmsc',
    'fastspeech2_male',
]

VOC_MODEL_IDS = [
    'pwgan_csmsc',
    'pwgan_aishell3',
    'mb_melgan_csmsc',
    'style_melgan_csmsc',
    'hifigan_csmsc',
    'hifigan_aishell3',
    'wavernn_csmsc',
    'pwgan_male',
    'hifigan_male',
]


@paddlespeech_router.post("/paddlespeech/", summary=SUMMARY, description=POST_DESCRIPTION,
                          response_description="语音合成结果")
async def predict(
        background_tasks: BackgroundTasks,
        text: str = Query(..., description='输入要生成的文本。'),
        am_model: str = Query(AM_MODEL_IDS[0], description="选择TTS任务的声学模型类型。", enum=AM_MODEL_IDS),
        voc_model: str = Query(VOC_MODEL_IDS[0], description="选择TTS任务的声码器类型。", enum=VOC_MODEL_IDS),
        fs: int = Query(24000, description='使用指定模型文件时的采样率。')
):
    tts = TTSExecutor()
    temp_file = NamedTemporaryFile(delete=False, suffix=".wav")
    filename = temp_file.name
    tts(text=text, am=am_model, voc=voc_model, fs=fs, output=filename)
    background_tasks.add_task(delete_file, filename)

    response = FileResponse(filename, media_type="audio/wav", filename="output.wav",
                            headers={"Content-Disposition": "attachment; filename=output.wav"})
    return response

