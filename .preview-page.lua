return {
    commands = {
        function(input)
            -- Command 1: Replace "docs/" with an empty string
            return input:gsub("docs/", "")
        end,
        function(input)
            -- Command 2: Replace "docs/" with an empty string
            return input:gsub("index.md", "")
        end,
        function(input)
            -- Command 2: Replace "docs/" with an empty string
            return input:gsub(".md", "")
        end,
        function(input)
            -- Command 3: Append the input to the URL
            return "open http://127.0.0.1:8001/" .. input
        end,
        -- Add more commands as needed
    }
}
