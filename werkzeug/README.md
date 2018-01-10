# werkzeug 的使用

在 werkzeug 有几个功能函数在 web 开发中很有用。
首先是导入它们:
```
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
```
- secure_filename: 返回一个安全的文件名
- generate_password_hash 产生一个 hash 加密的字符串, 通过 check_password_hash 去核对

## 中间件

中间件会在每次请求添加额外的处理,可以用来记录日志,会话管理,请求验证,性能分析等,其中有3个常用的中间件:

- SharedDataMiddleware 实现对静态文件的访问
- ProfileMiddleware 添加性能分析
- DispatchMiddleware 可以调度多个应用的中间件

