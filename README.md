# Pycman

一款用于创建或者管理 python 项目的命令行脚手架工具。

## feature

- 可自定义模板配置项目初始化流程
- 支持像 NPM 项目中，对 package.json 的 script 配置中，自定义指令配置，使用 pyc run <command>
- 支持 pbr 工程配置模板生成
- 可更具`git tag`自动生成`changelog`
- 集成 `commitizen` 工具

## Qucik Start

### 创建项目

```shell
pyc create
Project name: myAwsomeProject
...
```

### 自定义指令配置

```python
package_info = {
    'name': 'Pycman',
    'author': 'singein',
    'email': 'singein@outlook.com'
}

scripts = {
    # 借鉴 npm 可以自定义指令
    # 在package.py根目录下使用 pyc run <command> 即可执行
    'commit': 'git add . && cz commit',
    'build': 'python setup.py bdist_wheel',
    'default': 'echo 请输入明确的命令名称'
}

```
