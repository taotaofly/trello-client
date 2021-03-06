#-*- coding:utf-8 -*-

def run(configFileName, options, arguments):
  from read import Read
  read = Read(configFileName)

  if len(arguments) == 0:
    return read.orgs()

  if options.member:
    return read.members(arguments[0])

  if options.board:
    return read.boards(arguments[0])

  return read.info(arguments[0])

