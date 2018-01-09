# restful
关于 restful 使用 flask 的 flask_restful 插件可以快速实现一个项目的 restful 架构。

## flask_restful 的使用
从 flask_restful 导入 `Api` 和 `Resource` 两个主要的对象 
`api=Api(app)` 实例化一个 api 对象
然后建立一个 resource 类然后继承 Resource 接下来再到类中分别实现 `get`,`put`,`delete`等方法

在 flask_restful 中还有使用 `reqparse` 添加 request 的参数
使用 `marshal_with` 装饰器将 python 对象转为字典集合

## 测试
在 shell 中可以使用 `curl` 和 `http` 两个命令进行实际的测试
```sh
http -f get http://example.com/api/v2
curl -X get http://example.com/api/v2
```
