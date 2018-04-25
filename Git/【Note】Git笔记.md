# 【Note】Git笔记
> 
> 廖雪峰 Git教程
>
> [网站地址](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
> 
> 2018.04.24
> 

## 集中式 v.s. 分布式
### 集中式版本控制系统
版本库集中存放在中央服务器中，工作时先从中央服务器取得最新版本，在完成工作后将结果推送给中央服务器。类似于图书馆，若要更改一本书，需先从图书馆借出，改动后再放回图书馆。

- **缺点**：需要联网才能工作；

### 分布式版本控制系统
没有中央服务器，每个人的电脑上都是一个完整的版本库，若协作工作时进行了修改，只需要将各自的修改推送给对方即可。

## 创建版本库
**版本库（responsibility）**，可简单理解为一个目录，该目录里的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都可进行跟踪，以便任何时刻均可追踪历史，或在将来某个时刻还原。

1. 创建版本库：

	```
	mkdir gitfile
	cd gitfile
	```
2. 设置创建目录为Git可管理的仓库：

	```
	git init
	```
3. 添加文件至版本库：建议使用标准的UTF-8编码，避免冲突和所有平台通用。

	```
	git add <file>
	```
4. 将文件提交到版本库：

	```
	git commit -m "wrote a test file"
	```
	-m后面输入本次提交的说明。
	
## 时光机穿梭
提交文件修改：

```
git add <file>
git status
git commit -m "change file's content"
```
使用git status可以查看当前仓库的状态。

## 版本回退
使用**git log**命令可以查看从最近到最远的提交日志。Git中，用**HEAD**表示当前版本，上一个版本为**HEAD^**，上上个版本为**HEAD^^**。使用**git reset**可以回退到之前的版本：

```
git reset --hard HEAD^
```
若想要撤销回退的操作，可以使用下面的方式：

```
git reflog
git reset --hard <commit id>
```
使用git reflog可以查看每一次命令，可以确定撤销前的commit id，将该id提供给git reset即可恢复。

## 工作区和暂存区

<img src="0.jpeg" width="400" alt="工作区和暂存区" align="center" />

- **工作区（Working Directory）：**即电脑中可以看到的目录；

- **版本区（Repository）：**工作区有一个隐藏目录.git，表示Git的版本库；Git版本库中最重要的是**暂存区(stage, index)**，Git自动创建的第一个分支**master**及指向**master**的指针**HEAD**。

将文件添加入Git版本库中时，分为两步：

1. **git add**添加文件，实际是把文件修改添加到暂存区；
2. **git commit**提交更改，实际是把暂存区的所有内容提交到当前分支，若提交后且没有对工作区做任何修改，则暂存区将没有内容；

Git跟踪并管理的是修改而非文件，故在修改文件后需要再次将文件add到暂存区，若不执行git add操作，后续git commit操作将不会提交文件的修改。

## 撤销修改

**场景一：**改乱工作区某个文件的内容，希望直接丢弃工作区的修改时：**git checkout \-\- {file}**，将文件在工作区的修改全部撤销，这里有两种情况：

- 文件自修改后还没有被放到暂存区，则撤销修改就回到和版本库一样的版本，即回到最近一次**git add**时的状态；
- 文件已添加到暂存区后又做了修改，则撤销修改将回到添加到暂存区后的状态，即回到最近一次**git commit**的状态；

**场景二：**在改乱工作区文件内容，并将其添加到暂存区后，若想要丢弃修改，则先使用**git reset HEAD file**将其回退到场景一，再使用**git checkout \-\- {file}**进行下一步修改。

**场景三：**已提交不合适的修改到版本库，想要撤销本次提交，则使用**git reset --hard HEAD^**回退到上一个版本，前提是没有推送到远程库。

## 删除文件
若在工作区中删除文件，有两种选择：

- 确实要从版本库中删除该文件，则用**git rm {file}**将文件删除，并使用**git commit**提交修改；
- 误删的情况，使用**git checkout \-\- {file}**操作，将误删文件恢复到最新版本，即用版本库里的版本替换工作区的版本；

## 远程仓库
GitHub是提供Git仓库托管服务的网站，设置本地Git仓库和Github仓库之间的传输：

**Step 1. 创建SSH Key:**

在终端中输入下面的命令：

```
ssh-keygen -t rsa -C "youremailaddress@mail.com"
```
**Step 2. 向Git仓库中导入公钥：**

在.ssh文件夹下使用ls命令查看所有文件，将id_rsa.pub文件中的公钥导入。

## 添加远程库
将已有的本地仓库与Github上的仓库相关联，即可将本地仓库的内容推送到Github仓库。在本地仓库下运行命令：

```
git remote add origin git@github.com:<username>/<filename.git>
```

将本地仓库的所有内容推送到远程库中：

```
git push -u origin master
```
在Github上新创建仓库时，使用-u，之后在该仓库下的提交均不需再添加-u的表示。

#### 从远程库克隆
```
git clone git@github.com:<username>/<filename.git>
```
## 分支管理
### 创建与合并分支
HEAD指向当前分支，若只有master分支，则HEASD指向master，master指向提交。一开始，master分支为一条线，Git用master指向最新的提交，再用HEAD指向master，就能确定当前分支及当前分支的提交点。

<img src="0.png" width="250" alt="HEAD master" align="center" />

当创建新分支如dev，Git新建dev指针，指向master相同的提交，再将HEAD指向dev，即表示分支在dev上。此后，对工作区的修改和提交就是针对dev分支，新提交一次后，dev指针往前移动一步，而master指针不变。


<img src="0-2.png" width="300" alt="HEAD master" align="center" />

<img src="0-3.png" width="300" alt="HEAD master" align="center" />

若在dev上完成工作，即可将dev与master合并，即直接将master指向dev的当前提交，即完成合并。

<img src="0-4.png" width="300" alt="HEAD master" align="center" />

删除dev分支即为将dev指针删掉，删掉后，就剩一条master分支。

**具体操作：**

1. 创建dev分支，并切换至dev分支：

	```
	git checkout -b dev
	```
	git checkout命令加上-b参数表示创建并切换，相当于：

	```
	git branch dev
	git checkout dev
	```
2. 使用命令查看当前分支，将列出所有分支，当前分支前标一个*号：

	```
	git branch
	```
3. 在dev分支上修改并正常提交：

	```
	git add <filename>
	git commit -m "branch test"
	```
4. 切换回master分支，此时master上没有dev上的修改，故要将dev分支合并到master上：

	```
	git checkout master
	git merge dev
	```
5. 删除dev分支：

	```
	git branch -d dev
	```

### 解决冲突
若同时对master和分支如dev进行修改，且进行新的提交，则Git无法执行快速合并，只能试图将各自的修改合并起来，这种合并可能会有冲突，必须手动解决冲突之后再提交。

### 分支管理策略
master分支应非常稳定，仅用来发布新版本，平时不在上面干活。干活在dev分支上，dev分支不稳定。每个人都在dev分支上干活，时不时往dev分支合并即可。合并分支时，使用**--no-ff**参数就可以用普通模式合并，合并后的历史有分支，能看出曾经做过合并。

```
git merge --no-ff -m "merge with no-ff" dev
```

### Bug分支
若出现bug需要修复，则每个bug通过一个新的临时分支来修复，修复后，合并分支，并将临时分支删除。若在dev分支上还有工作未提交，则可使用stash功能将工作现场储存，此时工作区将变得干净，等以后恢复现场后继续工作：

```
git stash
```
确定需要修复bug的分支(此处假设为master)，并从其上创建临时分支，修复后提交：

```
git checkout master
git checkout -b issue-101
git add <filename>
git commit -m "fix bug"
git checkout master
git merge --no-ff -m "merged bug fix 101" issue-101
git branch -d issue-101
```
修复bug之后返回原来的dev分支继续工作，并恢复之前的工作现场：

```
git checkout dev
git stash list
git stash pop
```
使用stash list可查看存储的内容，使用stash pop可将存储的内容恢复并删除。

### Feature分支
每添加一个新功能，最好新建一个feature分支，在上面完成开发，之后合并并删除feature分支。若要丢弃一个没有被合并过的分支，则可以强项删除：
```
git branch -D <name>
```

### 多人协作
当从远程仓库克隆时，Git自动把本地的master分支与远程的master分支对应起来，切远程仓库的默认名称为origin。使用**git remote -v**可以查看远程库的特征，表示为可以抓取和推送的origin的地址。

```
$ git remote -v
origin git@github.com:<username>/<filename.git> (fetch)
origin git@github.com:<username>/<filename.git> (push)
```
#### 推送分支
推送分支，即把该分支上的所有本地提交推送到远程库。推送时，要指定本地分支，这样Git将会把该分支推送到远程库对应的远程分支上：

```
git push origin master
```
若要推送其他分支，如dev，则改为：

```
git push origin dev
```
- master分支为主分支，要时刻与远程同步；
- dev分支为开发分支，也需要与远程同步；
- bug分支只用于本地修复bug，不需要推送到远程；
- feature分支推送到远程取决于是否要在上面合作开发；

#### 抓取分支
当从远程库clone时，默认情况下只能看到本地的master分支，若要在dev分支上开发，必须创建远程origin的dev分支到本地：

```
git checkout -b dev origin/dev
```

多人协作工作模式：

1. 使用**git push origin <branch-name>**推送修改；
2. 若推送失败，则因为远程分支比本地更新，需要使用**git pull**试图合并；若**git pull**失败，需要确认是否指定了本地dev分支与远程origin/dev分支的链接：
	
	```
	git branch --set-upstream dev origin/dev
	```
3. 若合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或解决冲突后，**git push origin <branch-name>**推送；

## 标签管理
### 创建标签
1. 使用**git tag <name>**新建一个标签，默认为**HEAD**，也可以指定一个commit id；
2. **git tag -a <tagname> -m "blablabla..."**可以指定标签信息；
3. **git tag**可以查看所有标签；
4. **git push origin <tagname>**可以推送一个本地标签；
5. **git push origin --tag**可以推送全部未推送过的本地标签；
6. **git tag -d <tagname>**可以删除一个本地标签；
7. **git push origin :refs/tags/<tagname>**可以删除一个远程标签；