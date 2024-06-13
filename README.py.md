**创建虚拟环境**

```
python3 -m venv env/
```

**激活虚拟环境**

```
source env/bin/activate
```

**退出虚拟环境**

```
deactivate
```

**安装依赖**

```
pip install fastapi uvicorn
```

```
pip install -r requirements.txt
```

**运行服务器**

```
uvicorn main:app --port 8000 --reload 
```
    