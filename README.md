
telegram 频道图片下载

使用 [dynaconf](https://github.com/dynaconf/dynaconf) 管理配置

使用 [pyrogram](https://github.com/pyrogram/pyrogram) 作为 telegram api 框架

`settings.yaml`中的api_id和api_hash仅做格式参考，实际使用时请新建`.secrets.yaml`并填入自己的api_id和api_hash，以防止泄露


运行方式（Linux为例）：
```python
# 设置虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖项
pip install -r requirements.txt

# 执行程序
python main.py
```
