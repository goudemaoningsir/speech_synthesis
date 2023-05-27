# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/5/5 20:44
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi

import uvicorn
from pathlib import Path
from fastapi import FastAPI
from synthesis.api_damo import damo_router
from synthesis.api_damo_emo import damo_emo_router
from synthesis.api_paddlespeech import paddlespeech_router

ROOT_PATH = Path(__file__).parent

app = FastAPI(
    title="语音合成",
    default_language="zh",
    debug=True
)

app.include_router(damo_router, prefix="/synthesis", tags=["modelscope"])
app.include_router(damo_emo_router, prefix="/synthesis", tags=["modelscope"])
app.include_router(paddlespeech_router, prefix="/synthesis", tags=["paddlespeech"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1701, log_level="debug", reload=True)
