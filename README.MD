# Shell tool to make cell-styled code a jupyter .ipynd file
This shell tool is used to transform styled code to ipynb file. The you can use jupyter-nbconvert to transform it to markdown form.
## 1. Install
In python environment.
You should install nuitka first.
```shell
nuitka cellc2jpt.py --onefile --lto=auto --remove-output
```
Then use
```
sudo install -Dm755 ./cellc2jpt "$pkgdir/usr/bin/cellc2jpt"                
```

## 2. Write you code in cell-style
Use '# cell' to devide you code to cells.

For example:
```python
# cell
# comment
print("a")
print("b")

# cell
# other comment
print("c")
```
This python file will be devided to 2 cells in jupyter ipynd file. One cell print \'a\' and \'b\',another cell will print \'c\' 

## 3. Use shell to tansform to ipynb
Use
```shell
cellc2jpt file_path
```
The ipynd file will create in the same dir with the target file.
## 4. Tansform to MD file
In jupyter environment.
```shell
jupyter nbconvert test.ipynb --to markdown
```

or

```shell
jupyter-nbconvert test.ipynb --to markdown
```

## Example
In current path use
```shell
cellc2jpt example/example.py
```
Then use jupyter notebook.
```shell
jupyter-notebook
```
Run the code in jupyter notebook with right kernel. Then save the ipynd file and shut down the jupyter.

Use this commend in the same shell.
```shell
jupyter-nbconvert --to markdown ./example/example.ipynb 
```
To make it to MD file.

Also you should first install jupyter-nbconvert in jupyter environment.
```shell
pip install nbconvert
```
