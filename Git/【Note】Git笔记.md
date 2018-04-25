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

- **版本区（Repository）：**工作区有一个隐藏目录.git，表示Git的版本库；Git版本库中最重要的是**暂存区stage\/index**，Git自动创建的第一个分支**master**及指向**master**的指针**HEAD**。

将文件添加入Git版本库中时，分为两步：

1. **git add**添加文件，实际是把文件修改添加到暂存区；
2. **git commit**提交更改，实际是把暂存区的所有内容提交到当前分支，若提交后且没有对工作区做任何修改，则暂存区将没有内容；

Git跟踪并管理的是修改而非文件，故在修改文件后需要再次将文件add到暂存区，若不执行git add操作，后续git commit操作将不会提交文件的修改。

## 撤销修改
**场景一：**改乱工作区某个文件的内容，希望直接丢弃工作区的修改时：**git checkout -- \<file\>**，将文件在工作区的修改全部撤销，这里有两种情况：

- 文件自修改后还没有被放到暂存区，则撤销修改就回到和版本库一样的版本，即回到最近一次**git add**时的状态；
- 文件已添加到暂存区后又做了修改，则撤销修改将回到添加到暂存区后的状态，即回到最近一次**git commit**的状态；

**场景二：**在改乱工作区文件内容，并将其添加到暂存区后，若想要丢弃修改，则先使用**git reset HEAD file**将其回退到场景一，再使用**git checkout -- \<file\>**进行下一步修改。

**场景三：**已提交不合适的修改到版本库，想要撤销本次提交，则使用**git reset --hard HEAD^**回退到上一个版本，前提是没有推送到远程库。

## 删除文件
若在工作区中删除文件，有两种选择：

- 确实要从版本库中删除该文件，则用**git rm \<file\>**将文件删除，并使用**git commit**提交修改；
- 误删的情况，使用**git checkout -- \<file\>**操作，将误删文件恢复到最新版本，即用版本库里的版本替换工作区的版本；

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