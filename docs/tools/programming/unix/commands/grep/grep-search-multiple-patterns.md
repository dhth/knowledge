# Grep Search Multiple Patterns

```bash
echo "project/subdir1/file1.py project/subdir1/file2.py project/subdir2/file2.py project/app.py app.py main.py" | tr ' ' '\n' | grep -e "^project\/subdir1\/.*\.py$" -e "^app.py$"

project/subdir1/file1.py
project/subdir1/file2.py
app.py
```
