
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'funcdefCOLON HYPHEN LPAREN NAME RPAREN TABfuncdef : NAME LPAREN parameters RPAREN COLON funcbodyparameters : NAME \n\t| NAME HYPHEN parameters \n\t| emptyfuncbody : TAB statement  \n\t|  TAB statement funcbodystatement : NAME   \n\t| NAME statementempty :'
    
_lr_action_items = {'NAME':([0,3,7,12,14,],[2,4,4,14,14,]),'$end':([1,11,13,14,15,16,],[0,-1,-5,-7,-6,-8,]),'LPAREN':([2,],[3,]),'RPAREN':([3,4,5,6,7,9,],[-9,-2,8,-4,-9,-3,]),'HYPHEN':([4,],[7,]),'COLON':([8,],[10,]),'TAB':([10,13,14,16,],[12,12,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funcdef':([0,],[1,]),'parameters':([3,7,],[5,9,]),'empty':([3,7,],[6,6,]),'funcbody':([10,13,],[11,15,]),'statement':([12,14,],[13,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> funcdef","S'",1,None,None,None),
  ('funcdef -> NAME LPAREN parameters RPAREN COLON funcbody','funcdef',6,'p_funcdef','interpretgrammar.py',3),
  ('parameters -> NAME','parameters',1,'p_parameters','interpretgrammar.py',6),
  ('parameters -> NAME HYPHEN parameters','parameters',3,'p_parameters','interpretgrammar.py',7),
  ('parameters -> empty','parameters',1,'p_parameters','interpretgrammar.py',8),
  ('funcbody -> TAB statement','funcbody',2,'p_funcbody','interpretgrammar.py',11),
  ('funcbody -> TAB statement funcbody','funcbody',3,'p_funcbody','interpretgrammar.py',12),
  ('statement -> NAME','statement',1,'p_statement','interpretgrammar.py',15),
  ('statement -> NAME statement','statement',2,'p_statement','interpretgrammar.py',16),
  ('empty -> <empty>','empty',0,'p_empty','interpretgrammar.py',51),
]