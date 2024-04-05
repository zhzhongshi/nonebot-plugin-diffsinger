这个需要配合这个项目使用（[DiffSingerMiniEngine](https://github.com/zhzhongshi/DiffSingerMiniEngine)

怎么搭？
我只在windows上跑的，欢迎PR（）

```
python -m venv ds
ds\Scripts\activate
git clone https://github.com/zhzhongshi/DiffSingerMiniEngine
cd DiffSingerMiniEngine
# 从release里把模型下下来解压丢进去（
pip install -r requirememts.txt -U
python server.py
```

然后搭建nb，从nb里把插件跑起来
我默认你会用nb-cli

```
nb plugin install nonebot-plugin-diffsinger
```

插件会自动添加到你pyproject.toml里面

你要是打算用pip安装的话

```
pip install nonebot-plugin-diffsinger
```

别忘了把"nonebot-plugin-diffsinger"加到pyproject.toml里面的"plugins"里面

配置

```
DS_URL="http://127.0.0.1:9266/" #后端的地址
DS_SPEEDUP=200 #后端的推理速度，建议10-255
```

测试指令

```
/diffsinger 120~[
[60,2,"AP"],
[57,2,"ba"],
[59,2,"ni"],
[60,2,"peng"],
[64,2,"zai"],
[62,2,"shou"],
[60,2,"+"],
[62,8,"shang"],
[60,4,"AP"],
[57,2,"he"],
[59,2,"qi"],
[60,12,"le"],
[59,4,"shou"],
[55,16,"zhang"],
[60,4,"AP"]
]|120~[
[60,4,"dao"],
[62,4,"lai"],
[64,4,"mi"],
[65,4,"fa"],
[67,4,"sao"],
[69,4,"la"],
[71,4,"xi"]
]|90~[
[60,4,"dao"],
[62,4,"lai"],
[64,4,"mi"],
[65,4,"fa"],
[67,4,"sao"],
[69,4,"la"],
[71,4,"xi"]
]
```
