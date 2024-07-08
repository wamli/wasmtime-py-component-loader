import wasmtime, wasmtime.loader

import loader_component_add

store = wasmtime.Store()

component = loader_component_add.Root(store)

print(component.add(store, 1, 2))