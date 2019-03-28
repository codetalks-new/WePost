首先更新 pip 本身依赖库。
安装 [pip-tools](https://github.com/jazzband/pip-tools) 作为依赖管理工具。

1. 最上层依赖分为生产环境依赖库和开发依赖库。
2. 使用以 `.in` 为后缀的文件声明项目直接依赖。使用 `.txt` 结尾的用来 `freeze` 所有直接间接依赖。
3. 创建一个 `common.in` 文件声明公共依赖， `dev.in` 继承 `common.in` 用于声明开发环境依赖。 `prod.in` 同样继承 `common.in`  声明生产环境依赖。
4. 直接依赖，应该在依赖后面或前面另起一行，简单描述为何增加此依赖。


需要添加依赖时可以先修改对应的 `.in` 文件。然后执行。
` ./requirements/update_locked_requirements.sh`
如开发环境中，再根据需要执行相应的 `pip install -r requirements/dev.txt`