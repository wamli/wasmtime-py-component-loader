# load_adder.py

* mimics [loader_component.py](https://github.com/bytecodealliance/wasmtime-py/blob/main/examples/loader_component.py)
* works

# load_demo.py

* example from [wasmtime-py](https://github.com/bytecodealliance/wasmtime-py)
* does NOT work
* error is

```bash
$ python load_demo.py 
Traceback (most recent call last):
  File "/load_demo.py", line 3, in <module>
    import demo_component
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "lib/python3.11/site-packages/wasmtime/loader.py", line 80, in exec_module
    exec(component_files[relative_path], module.__dict__)
  File "<string>", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "lib/python3.11/site-packages/wasmtime/loader.py", line 80, in exec_module
    exec(component_files[relative_path], module.__dict__)
         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
KeyError: 'imports.py'
```

## Same example, other syntax

```bash
# the following works
python -c 'import wasmtime.loader, loader_component_add; store = wasmtime.Store(); print(loader_component_add.Root(store).add(store, 1, 2))'

# the following does not work
python -c 'import wasmtime.loader, demo_component; store = wasmtime.Store(); print(demo_component.Root(store).run(store))'
```