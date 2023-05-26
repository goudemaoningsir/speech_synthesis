<div align="center">
  <a href="https://github.com/sanmaomashi/speech_synthesis">
    <img src="https://raw.githubusercontent.com/sanmaomashi/speech_synthesis/main/img/1.jpg" height="400">
  </a>
  <h1>Speech Synthesis</h1>
  <img src="https://img.shields.io/github/repo-size/sanmaomashi/speech_synthesis.svg?label=Repo%20size&style=flat-square" height="20">
  <img src="https://img.shields.io/badge/License-Apache%202.0-purple" data-origin="https://img.shields.io/badge/License-Apache%202.0-blue" alt="">
</div>






## 简介

语音 语音合成



基于以下开源模型的 [fastapi](https://github.com/tiangolo/fastapi) 实现：

- [x] [damo/speech_sambert-hifigan_tts_zhishuo_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhishuo_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhida_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhida_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhigui_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhigui_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhimao_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhimao_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhiya_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhiya_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhiyuan_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhiyuan_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhisha_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhisha_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhiyue_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhiyue_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhiyan_emo_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhiyan_emo_zh-cn_16k/summary)
- [x] [damo/speech_sambert-hifigan_tts_zhibei_emo_zh-cn_16k](https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zhibei_emo_zh-cn_16k/summary)
- [ ] [PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech)






## 免责声明

本仓库为非盈利仓库，对任何法律问题及风险不承担任何责任。

本仓库没有任何商业目的，如果认为侵犯了您的版权，请来信告知。

本仓库不能完全保证内容的正确性。通过使用本仓库内容带来的风险与本人无关。



## 环境依赖

python3.7



## 本地部署

1. 克隆项目

```bash
git clone https://github.com/sanmaomashi/speech_synthesis.git
```

2. 安装依赖

```bash
pip install -r requirements -i https://mirror.baidu.com/pypi/simple
```

3. 执行项目

```bash
cd /项目目录/bin
bash start_project.sh
```

4. 访问swagger ui

```http
http://{{ip}}:1701/docs
```



## docker部署

构建镜像

```bash
docker build -t speech:synthesis .
```

启动容器

```bash
docker run -d --name speech -p 1701:1701 --restart=always speech:synthesis
```

访问swagger ui

```http
http://{{ip}}:1701/docs
```

![](https://raw.githubusercontent.com/sanmaomashi/speech_synthesis/main/img/2.png)

## License

Licensed under the [Apache-2.0](http://choosealicense.com/licenses/apache/) © speech_synthesis

