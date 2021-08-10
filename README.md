
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
git remote remove <name>
```

```
git push 命用于从将本地的分支版本上传到远程并合并。

命令格式如下：
git push <远程主机名> <本地分支名>:<远程分支名>

如果本地分支名与远程分支名相同，则可以省略冒号：
git push <远程主机名> <本地分支名>
git push origin master
```

```
git branch 查看本地分支
git branch -r 查看远程分支
git branch -a 查看所有分支
git branch dev 创建dev分支
git branch -d dev 删除dev分支
git checkout master 切换分支
```