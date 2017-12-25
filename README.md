# githooker `[latest version: v1.0.2]`

A extensible tool to hook your git projects


- [githooker](#githooker)
	- [Install](#install)
	- [Getting Started](#getting-started)
		- [Init Hook Environment](#init-hook-environment)
		- [Add hook plugins or scripts](#add-hook-plugins-or-scripts)
		- [Hook](#hook)
		- [Make My Own Hook-plugin](#make-my-own-hook-plugin)
	- [Usage](#usage)
	- [Plugin-list](#plugin-list)
- [githooker 中文说明](#githooker-中文说明)
---

- **simpleness:** You need only a few commands(`githooker init`、`githooker add`)to manage your hook scrips of your git project through `githooker`.
- **use unify config:** Generate every git-project a `githooker.json` config file，you can share it for all the project members。
- **extensible plugins support:** Use `githooker add` to add git hook-scripts or hooker-plugins. Use `githooker make` to make your hook plugin as you like（Please contact me to add your plugin at the plugin list below to let people easy to find them：[luochenxun@gmail.com](luochenxun@gmail.com)）


## Install

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/luochenxun/githooker/master/install.sh)"
```

## Getting Started

### Init Hook Environment

Run `githooker init` in the root directory of your git project，it'll auto generate a `githooker.json` config file。config like this(conclude your project's name、path、hook list)
```
{
  "name": "gitProjName",
  "hookerversion": "1.0.1",
  "path": "/Users/xx/gitProj",
  "hooks": [
  ]
}
```

After init done,you can use `githooker list` to list the config in `githooker.json`

### Add hook plugins or scripts

As I want to add a plugin `githooker-npm-version-inc` to increate my npm package's version every I commit，use `githooker add` like：

```
githooker add https://github.com/luochenxun/githooker-npm-version-inc.git
```

Now my `githooker.json` take place, the plugin was added to the hooks list.Through `githooker list` command to see the change.

### Hook

After I add the `githooker-npm-version-inc` plugin. Now when I perform a new commit like `git commit -m "xxx"`, the package's version will increate automatically. I can use it to increate the buildId of my project ,that will help me to track the bug.


### Make My Own Hook-plugin

If I want to make a hook script to lint my code every before I `git push`.

Use `githooker make -o py-code-lint` to generate the templete scrips in the directory `githooker-py-code-lint`(the templete scrips is in the directory).

The name of the script tell you when they invoke(pre-commit will invoke before your commit take effect，pre-commit-msg invoke your commit-msg take effect， pre-push invoke before your push take effect).

After I write my lint script, then use `githooker add xx/pre-push.py` to add my script to the config. And then when I use `git push`, my lint hook will take effect.


You can also follow the `githooker-pluginName` format to upload your plugin's code to github, and then send an email to me[luochenxun@gmail.com](luochenxun@gmail.com), I'll add your plugin at the plugin list below to let people easy to find them.

## Usage

Githooker is a extensible tool to hook your git projects. version:1.0.2 .

Usage: `githooker <cmd> [OPTIONS] [param]`
-  **init**                   : init the hook-environment of the project, write the config in githooker.json
-  **clean**                  : clean the hook-environment of the project, do the reverse job as 'init'
-  **list**                   : list the config of the project
-  **add  [hookers]**         : add a hooker of the project
-  **remove [hookers]**       : remove a hooker of the project
-  **clear**                  : clear all the hookers the project
-  **make [OPTIONS] [param]** : help you to make a githooker plugin in the current dir

for more infomation of the cmd, you can use option as 'githooker add -h' for farther help.

## Plugin-list


https://github.com/luochenxun/githooker-npm-version-inc.git      | increate your npm package's version every time you git commit.
-----------------------------------------------------------------|--------------------------------------------------------------------------------------


# githooker 中文说明

一个可扩展的git hook工具

---

- **简单:** 只需要简单几个的命令(`githooker init`、`githooker add`)就可以管理你的git项目的hook脚本。
- **统一管理:** 为每个git项目生成独立的`githooker.json`配置文件，使项目成员可以共同使用同一套git hook脚本配置。
- **可扩展:** 可使用`githooker add` 命令为您的项目添加自己或别人已写好的本地hook脚本，你还可以使用线上脚本（只要在add后紧跟hook脚本的git地址）。更有`githooker make`命令可以更方便地生成模板，编写自己的hook脚本，欢迎大家贡献更多的线上hook脚本（联系我会帮你们放到本页的列表上：[luochenxun@gmail.com](luochenxun@gmail.com)）


- [githooker 中文说明](#githooker-中文说明)
	- [安装](#安装)
	- [快速入门](#快速入门)
		- [初始化项目](#初始化项目)
		- [添加hook插件](#添加hook插件)
		- [使用](#使用)
		- [制作我自己的hook脚本或上传插件](#制作我自己的hook脚本或上传插件)
	- [使用说明](#使用说明)
		- [主要命令](#主要命令)
		- [帮助](#帮助)
	- [插件列表](#插件列表)

<!-- /TOC -->

## 安装

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/luochenxun/githooker/master/install.sh)"
```

## 快速入门

### 初始化项目

在你的git项目根目录运行`githooker init`初始化hook环境，会自动生成配置文件`githooker.json`。配置如下，记录了项目的路径、githooker版本、所使用的hook插件或脚本
```
{
  "name": "gitProjName",
  "hookerversion": "1.0.1",
  "path": "/Users/xx/gitProj",
  "hooks": [
  ]
}
```
初始化完成后，你可以使用`githooker list`来查看githooker配置。

### 添加hook插件

比如我现在想在每次提交代码时递增npm包的版本号，我找到了`githooker-npm-version-inc`插件，使用`add`命令添加之：

```
githooker add https://github.com/luochenxun/githooker-npm-version-inc.git
```

提示我添加成功，此命令也可以同时添加多个插件或本地脚本。这将会导致`githooker.json`配置文件发生变化，hooks列表将增加我新添加的插件，使用`githooker list`可以查看到我新添加的插件。

### 使用

添加完`githooker-npm-version-inc`插件后，现在每当我执行`git commit -m "xxx"`命令后，hook会自动递增我的npm包版本号，我可以使用这个插件每当有代码提交时递增构建号，达到Bug追踪的功能。


### 制作我自己的hook脚本或上传插件

我现在想给项目增加一个hook脚本让团队在每次push代码前使用lint先检验下代码，如果发生语法错误则中止代码推送。

使用 `githooker make -o py-code-lint` 在本地生成了一个文件夹，名为`githooker-py-code-lint`，这里面有我们需要的hook代码模块（python脚本）。脚本的名称说明了他们调用的时机（pre-commit 发生在提交生效前，pre-commit-msg 发生在提交信息生效前， pre-push 发生在git push命令生效前）。因此，我修改pre-push.py代码，完成我需要的功能，删掉另两个用不上的脚本文件。

然后我使用 `githooker add xx/pre-push.py` 添加我制作的hook脚本。

我也可以按照`githooker-pluginName`的格式上传插件到github，然后发邮件给[luochenxun@gmail.com](luochenxun@gmail.com), 我会把你的插件添加到本页列表中，方便更多人使用。

## 使用说明

### 主要命令

1. `githooker init` : 在你的git项目根目录使用`init`命令将初始化你的项目为githooker项目，这将会替换你本地git项目中的hook脚本以及生成一个githooker本地配置文件`githooker.json`;
2. `githooker add scripts` : 找到你需要的hook脚本（可以使用`githooker make`自己生成本地脚本，也可以使用线上的插件），
3. `githooker list` : 打印当前项目githooker配置，可以查看当前项目使用了哪些插件或脚本。
4. `githooker make` : 生成hook脚本模板，用于快速制作专属于自己项目

### 帮助
githooker <cmd> [OPTIONS] [param]
-  init                   : 在你的git项目根目录使用`init`命令将初始化你的项目为githooker项目，这将会替换你本地git项目中的hook脚本以及生成一个githooker本地配置文件`githooker.json`;
-  clean                  : 清除`githoooker init`生成的hook脚本及配置
-  list                   : 打印当前项目githooker配置，可以查看当前项目使用了哪些插件或脚本。
-  add  [hookers]         : 添加一个或多个hook插件或本地脚本
-  remove [hookers]       : 删除一个或多个hook插件或本地脚本
-  clear                  : 清空hook插件或本地脚本
-  make [OPTIONS] [param] : 制作hook插件或本地脚本

## 插件列表


https://github.com/luochenxun/githooker-npm-version-inc.git      | 会在你每次commit代码时自动增加npm包的最小版本号，对package中version字段时小版本号加1.
-----------------------------------------------------------------|--------------------------------------------------------------------------------------
https://github.com/luochenxun/githooker-module-commit-msg-cn.git | commit代码时触发，只有符合提交规范的commit` [模块名/Bug号] 提交内容描述`才会通过.
