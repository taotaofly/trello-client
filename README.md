#概况

一个用python（node）实现的Trello客户端。

#安装配置

```shell
#安装
cd ~/
wget https://nodeload.github.com/NanJingBoy/trello-client/zip/master
unzip master
#安装python相关依赖
pip install oauth2
pip install python-dateutil==1.5
#安装node相关依赖
cd ~/trello-client-master/node
npm install oauth
#配置
cd trello-client-master
cp config_example.json config.json
vim config.json //修改developerKeys节点中key和oauth_secret的值;并删除文件中所有注释语句
```
#命令列表（此处仅以python版为例，node命令列表相同）

```shell
cd ~/trello-client-master/python
./trello_client -a //用户验证
./trello_client -o //获取organizations列表信息
./trello_client -o org //获取名称为org的organization信息
./trello_client -om org //获取名称为org的organization中member列表信息
./trello_client -ob org //获取名称为org的organization中board列表信息
#其中org为执行./trello_client -o 获取的organization列表信息中包含在"（）"中的值

./trello_client -b board //获取ID为board的board信息
./trello_client -bm board //获取ID为board的board中的member列表信息
./trello_client -bl board //获取ID为board的board中的lists列表信息
#其中board为执行./trello_client -ob org 获取的board列表信息中包含在"（）"中的值

./trello_client -l list //获取ID为list的list信息
./trello_client -lc list //获取ID为list的list中card列表信息
#其中list为执行./trello_client -bl board 获取的lists列表信息中包含在"（）"中的值

./trello_client -c card //获取ID为card的card信息
./trello_client -cm card //获取ID为card的card中member列表信息
#其中card为执行./trello_client -lc list 获取的card列表信息中包含在"（）"中的值
```
