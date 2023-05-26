# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/5/4 22:31
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi

import os
from fastapi import APIRouter, Query, BackgroundTasks
from fastapi.responses import FileResponse
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from tempfile import NamedTemporaryFile

SUMMARY = "语音合成-多情感"
POST_DESCRIPTION = "语音合成API\n"
damo_emo_router = APIRouter()

MODEL_IDS = [
    'damo/speech_sambert-hifigan_tts_zhiyan_emo_zh-cn_16k',
    'damo/speech_sambert-hifigan_tts_zhibei_emo_zh-cn_16k'
]

EMOTIONS = ['neutral', 'happy', 'angry', 'sad', 'fear', 'hate', 'surprise', 'arousal']


def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)


@damo_emo_router.post("/damo_emo/", summary=SUMMARY, description=POST_DESCRIPTION, response_description="语音合成结果")
async def predict(text: str,
                  background_tasks: BackgroundTasks,
                  emotion: str = Query('neutral', description="可选的情感", enum=EMOTIONS),
                  intensity: float = Query(1.0, description="情感强度"),
                  model_id: str = Query(MODEL_IDS[0], description="可选的语音合成模型", enum=MODEL_IDS)):
    sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id)
    ssml_text = f'<speak><emotion category="{emotion}" intensity="{intensity}">{text}</emotion></speak>'
    output = sambert_hifigan_tts(input=ssml_text)
    wav = output[OutputKeys.OUTPUT_WAV]

    temp_file = NamedTemporaryFile(delete=False, suffix=".wav")
    filename = temp_file.name
    with open(filename, 'wb') as f:
        f.write(wav)
    background_tasks.add_task(delete_file, filename)
    response = FileResponse(filename, media_type="audio/wav", filename="output.wav",
                            headers={"Content-Disposition": "attachment; filename=output.wav"})
    return response