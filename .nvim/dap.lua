-- .nvim/dap.lua
local dap = require("dap")

-- Placeholders
-- ${file}: Current file.
-- ${workspaceFolder}: Project root.
-- ${env:VAR}: Environment variables.

-- Append project-specific configurations for Python
table.insert(dap.configurations.python, {
    name = "Project Run main",
    type = "python",
    request = "launch",
    program = "${workspaceFolder}/src/main.py",
    args = { "--debug" },
})
