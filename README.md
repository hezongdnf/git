
```
echo "# learn_git" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin git@github.com:hezongdnf/learn_git.git
git push -u origin master
```

```
git remote add [<options>] <name> <url>
<name>是代表仓库
```

```
git push 命用于从将本地的分支版本上传到远程并合并。

命令格式如下：
git push <远程主机名> <本地分支名>:<远程分支名>

如果本地分支名与远程分支名相同，则可以省略冒号：
git push <远程主机名> <本地分支名>
git push origin master
```

### this is a test