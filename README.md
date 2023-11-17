<div align="center">
    <img src="assets/icon.png" width=300><br>
    <h>newpy is a tool to help you create new python projects with ease</h>
</div>

## 📝 Installation

`pip install git+https://github.com/blankRiot96/newpy`<br>

## ⌨️ Usage

start by creating a folder containing all your templates, for example check out [my template folder](https://github.com/blankRiot96/templates)<br>

the `--set-template-dir` flag allows you to set the template folder from which you want to be able to copy<br>

```
newpy --set-template-dir path/to/your/templates
```

the `--spawn` or `-s` flag lets you create a copy of a template within your templates path. for example `pg/` is a folder in the set templates path with the pygame boilerplate <br>

```
newpy -s pg
```

spawn into a specific directory by specifying the `--direc` or `-d` flag<br>

```
newpy -s pg -d my_cool_game
```
