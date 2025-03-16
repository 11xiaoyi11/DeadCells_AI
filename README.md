# DeadCells_AI

## Get Start

### 参考环境配置
环境配置请按顺序参考下列几篇文档：  
基本环境： https://github.com/BAAI-Agents/Cradle/blob/main/README.md （Installation部分）  
groundingdino部分： https://github.com/BAAI-Agents/Cradle/blob/main/docs/envs/groundingdino.md  
videosubfinder部分： https://github.com/BAAI-Agents/Cradle/blob/main/docs/envs/rdr2.md  

### pip install

```bash
git clone https://github.com/11xiaoyi11/DeadCells_AI.git
```

```bash
cd ./DeadCells_AI
```

```bash
pip install requirements.txt
```

[如果遇到问题请参考前一部分](###参考环境配置) 
### 添加密钥
目前本项目代码仅支持openai，需要在.env中修改api_key，以及修改[base_url](https://github.com/11xiaoyi11/DeadCells_AI/blob/main/cradle/provider/llm/openai.py#L108)
运行程序

```bash
python runner.py --envConfig "./conf/env_config_deadcells.json"
```
