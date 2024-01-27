# 图片查看器 Web 应用

这是一个基于 Flask 的简单 Web 应用程序，允许用户在目录中查看和管理图像。用户可以在浏览器中查看图像，使用“下一个”和“上一个”按钮进行导航，移动端通过左右滑切换图像，并在进行适当的身份验证后删除图像。

## 安装

1. 克隆仓库到您的本地机器。

2. 在命令行中运行 `pip install -r requirements.txt` 安装所需的 Python 包。

3. 复制 `setting.yaml.sample` 文件并将其重命名为 `setting.yaml`。编辑 `setting.yaml` 文件以设置您想要的配置。部分非必填项留空则使用 `config.py` 提供的默认值。

4. 运行 `python main.py` 启动 Flask 应用程序。

## nginx 配置参考

```
server {
    listen 52020 ssl http2;
    listen [::]:52020 ssl http2;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/example.com/example.com.pem;
    ssl_certificate_key /etc/nginx/ssl/example.com/example.com.key;

    root /var/www/example.com/static;

    # /photos/ 路径在 photos.html 中硬编码，如果修改了这里，需要同步修改 photos.html
    # 存放图片的目录，本例中为 /var/www/example.com/static/photos/
    location /photos/ {
        expires 7d;
        add_header Cache-Control "public,immutable";
    }

    location = /photos/ {
        rewrite ^ /photos break;
    }

    location = /photos {
        rewrite ^ / break;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 使用

在 Web 浏览器中打开并导航到您在配置设置中指定的主机和端口。您将看到在配置设置中指定的目录中的第一张图像。您可以使用“下一个”和“上一个”按钮在图像之间导航，并在进行适当的身份验证后删除图像。

## 贡献

欢迎对这个项目进行贡献。请先 fork 这个仓库，然后创建您的分支，提交更改后创建一个新的 Pull 请求。

## 许可证

此项目根据 MIT 许可证进行许可。

## 联系

如果您有任何问题或建议，请随时通过电子邮件或者 issue 联系我们。

## 致谢

感谢所有对这个项目做出贡献的人。
