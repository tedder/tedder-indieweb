
import CommonMark

def __init__(self):
  pass

# docs: https://rawgit.com/rolandshoemaker/CommonMark-py/master/docs/CommonMark.py.html
def translate(inputstr): # take string or file - how?
  parser = CommonMark.DocParser()
  renderer = CommonMark.HTMLRenderer()
  ast = parser.parse(inputstr)
  html = renderer.render(ast)
  #CommonMark.dumpAST(ast) # pretty print generated AST structure
  return html
