# YoN

一个帮你做日常小决定的网页工具，支持 Yes / No、自定义选项，以及简体中文、繁体中文和英文。

[在线使用](https://yon.nigga.store)

## 本地启动

需要 Python 3.9+，无第三方依赖。

```sh
python3 -B server.py
```

按提示输入 TypeSafe API Key（隐藏输入），也可通过 `TYPESAFE_API_KEY` 环境变量提供。启动后访问 [本地页面](http://127.0.0.1:8765/)。

## 部署

将仓库导入 Vercel，配置服务端环境变量 `TYPESAFE_API_KEY`，即可按仓库内配置构建部署。密钥仅用于后端。
