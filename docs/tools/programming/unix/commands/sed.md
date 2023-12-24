# sed

Resources
---

- [linux - sed command with -i option
    (in-place editing) works fine on Ubuntu but not
    Mac](https://stackoverflow.com/questions/16745988/sed-command-with-i-option-in-place-editing-works-fine-on-ubuntu-but-not-mac)

Inplace editing
---

Use `-i`.

Print a range of lines
---

```bash
sed -n '1,100 p' file.txt
```

Use environment variables in sed
---

```bash
# sed -e "s/$WIKI_DIR\/docs/string_to_replace_with/"  this doesn't work
sed -e 's@'"$WIKI_DIR/docs/"'@string_to_replace_with@'
sed -e "s|$WIKI_DIR/docs/|string_to_replace_with|"
```

Delete lines in a file
---

```bash
sed -i '' '1,3d' file.txt
# deletes lines 1-3 in place
```

Delete lines that match a pattern
---

```bash
sed -i '' '/somepattern/d' file.txt
```

Remove nth line of stdin
---

```bash
echo '1\n2\n3\n4'
1
2
3
4
echo '1\n2\n3\n4' | sed 2d
1
3
4
```

Add closing tag to html tags
---

```bash
find docs -name '*.md' | xargs sed -i "" '/<img/ s/>$/\/>/'
```
  

Add a character in the beginning of a line
---

Say I want to add `# ` in the begining of the first line.

```bash
find docs -name '*.md' | xargs sed -i "" '1s/^/# /'
```
  
