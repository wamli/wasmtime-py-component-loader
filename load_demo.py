import wasmtime, wasmtime.loader

import demo_component

store = wasmtime.Store()

component = demo_component.Root(store)

print(component.run(store))
