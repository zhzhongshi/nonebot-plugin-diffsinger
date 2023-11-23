这个配合这个项目使用（[DiffSinger-ONNX-Infer](https://github.com/zhzhongshi/DiffSinger-ONNX-Infer)
怎么搭？
我只在windows上跑的，欢迎PR（
```
python -m venv ds
ds\Scripts\activate
git clone https://github.com/zhzhongshi/DiffSinger-ONNX-Infer
# 从release里把模型下下来解压丢进model里（
cd DiffSinger-ONNX-Infer
pip install -r requirememts.txt -U
python main.py
```


然后搭建nb，从nb里把插件跑起来（  


测试指令


```
/ds {"data":["小酒窝长睫毛AP是你最美的记号",
"C#4 | F#4| G#4 | A#4 F#4 | F#4 C#4 | C#4 | rest | C#4 | A#4 | G#4 | A#4 | G#4 | F4 | C#4",
"0.407140 | 0.376190 | 0.242180 | 0.509550 0.183420 | 0.315400 0.235020 | 0.361660 | 0.223070 | 0.377270 | 0.340550 | 0.299620 | 0.344510 | 0.283770 | 0.323390 | 0.360340"]
}
```
