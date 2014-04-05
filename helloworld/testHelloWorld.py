import os, sys
lib_path = os.path.join('ply-3.4')
sys.path.append(lib_path)

from svelLexHelloWorld import SvelLexer
from node import Node
import svelYaccHelloWorld
from svelTraverse import SvelTraverse

# get and build lexer
svel = SvelLexer()
svel.build()

# get parser
parser = svelYaccHelloWorld.getParser()

# provide some data
data = '''
// some commments
main() {
	print "Hello World!";
}
'''

ast = parser.parse(data, lexer=svel.get_lexer())
print ast

print SvelTraverse(ast).get_code()