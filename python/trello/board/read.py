#-*- coding:utf-8 -*-
from trello.base.read import Read as ReadBase

class Read(ReadBase):
  def __init__(self, configFileName):
    super(Read, self).__init__(configFileName)
    self.baseUrl = self.config.getApi('board', 'item')

  def info(self, id):
    info = self.trello.getData(
      '%s/%s' % (self.baseUrl, id),
      '&fields=name,desc,closed,pinned,url,subscribed'
    )
    if info:
      print(
        '名称：%s（%s）：%s' %
        (info['name'], info['id'], '已加入' if info['pinned'] else '未加入')
      )
      print('关闭：%s' % ('是' if info['closed'] else '否'))
      print('订阅：%s' % ('是' if info['subscribed'] else '否'))
      print('链接：%s' % info['url'])
      print('描述：%s' % info['desc'])

  def lists(self, id):
    lists = self.trello.getData(
      '%s/%s/lists' % (self.baseUrl, id),
      '&fields=name,closed'
    )
    if lists:
      for item in lists:
        print(
          '%s（%s）：%s' %
          (
            item['name'], item['id'],
            '已关闭' if item['closed'] else '未关闭'
          )
        )
