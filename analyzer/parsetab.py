
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLLECTION COLON COMMA CREATE DATABASE DELETE DOCUMENTS FALSE FROM GET IDENTIFIER INSERT INTO LBRACE NULL NUMBER RBRACE SET STRING TRUE UPDATE WHERE WITHstatement : create_db\n                 | create_collection\n                 | insert_document\n                 | get_documents\n                 | update_document\n                 | delete_document\n                 | delete_collectioncreate_db : CREATE DATABASE IDENTIFIER WITH COLLECTION IDENTIFIERcreate_collection : CREATE COLLECTION IDENTIFIER INTO DATABASE IDENTIFIERinsert_document : INSERT INTO DATABASE IDENTIFIER COLLECTION IDENTIFIER LBRACE document RBRACEget_documents : GET DOCUMENTS FROM DATABASE IDENTIFIER COLLECTION IDENTIFIERupdate_document : UPDATE DATABASE IDENTIFIER COLLECTION IDENTIFIER SET LBRACE document RBRACE WHERE LBRACE document RBRACEdelete_document : DELETE FROM DATABASE IDENTIFIER COLLECTION IDENTIFIER WHERE LBRACE document RBRACEdelete_collection : DELETE COLLECTION IDENTIFIER FROM DATABASE IDENTIFIERdocument : STRING COLON value\n                | document COMMA STRING COLON valuevalue : STRING\n             | NUMBER\n             | TRUE\n             | FALSE\n             | NULL'
    
_lr_action_items = {'CREATE':([0,],[9,]),'INSERT':([0,],[10,]),'GET':([0,],[11,]),'UPDATE':([0,],[12,]),'DELETE':([0,],[13,]),'$end':([1,2,3,4,5,6,7,8,42,43,48,50,57,70,75,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-14,-11,-10,-13,-12,]),'DATABASE':([9,12,16,19,24,29,34,],[14,18,23,26,31,36,41,]),'COLLECTION':([9,13,25,28,30,33,38,],[15,20,32,35,37,40,45,]),'INTO':([10,22,],[16,29,]),'DOCUMENTS':([11,],[17,]),'FROM':([13,17,27,],[19,24,34,]),'IDENTIFIER':([14,15,18,20,23,26,31,32,35,36,37,40,41,45,],[21,22,25,27,30,33,38,39,42,43,44,47,48,50,]),'WITH':([21,],[28,]),'SET':([39,],[46,]),'LBRACE':([44,46,52,69,],[49,51,56,72,]),'WHERE':([47,60,],[52,69,]),'STRING':([49,51,56,58,59,71,72,],[54,54,54,62,63,63,54,]),'RBRACE':([53,55,61,63,64,65,66,67,68,73,74,],[57,60,70,-17,-15,-18,-19,-20,-21,-16,75,]),'COMMA':([53,55,61,63,64,65,66,67,68,73,74,],[58,58,58,-17,-15,-18,-19,-20,-21,-16,58,]),'COLON':([54,62,],[59,71,]),'NUMBER':([59,71,],[65,65,]),'TRUE':([59,71,],[66,66,]),'FALSE':([59,71,],[67,67,]),'NULL':([59,71,],[68,68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'create_db':([0,],[2,]),'create_collection':([0,],[3,]),'insert_document':([0,],[4,]),'get_documents':([0,],[5,]),'update_document':([0,],[6,]),'delete_document':([0,],[7,]),'delete_collection':([0,],[8,]),'document':([49,51,56,72,],[53,55,61,74,]),'value':([59,71,],[64,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> create_db','statement',1,'p_statement','analizer.py',75),
  ('statement -> create_collection','statement',1,'p_statement','analizer.py',76),
  ('statement -> insert_document','statement',1,'p_statement','analizer.py',77),
  ('statement -> get_documents','statement',1,'p_statement','analizer.py',78),
  ('statement -> update_document','statement',1,'p_statement','analizer.py',79),
  ('statement -> delete_document','statement',1,'p_statement','analizer.py',80),
  ('statement -> delete_collection','statement',1,'p_statement','analizer.py',81),
  ('create_db -> CREATE DATABASE IDENTIFIER WITH COLLECTION IDENTIFIER','create_db',6,'p_create_db','analizer.py',85),
  ('create_collection -> CREATE COLLECTION IDENTIFIER INTO DATABASE IDENTIFIER','create_collection',6,'p_create_collection','analizer.py',89),
  ('insert_document -> INSERT INTO DATABASE IDENTIFIER COLLECTION IDENTIFIER LBRACE document RBRACE','insert_document',9,'p_insert_document','analizer.py',93),
  ('get_documents -> GET DOCUMENTS FROM DATABASE IDENTIFIER COLLECTION IDENTIFIER','get_documents',7,'p_get_documents','analizer.py',97),
  ('update_document -> UPDATE DATABASE IDENTIFIER COLLECTION IDENTIFIER SET LBRACE document RBRACE WHERE LBRACE document RBRACE','update_document',13,'p_update_document','analizer.py',101),
  ('delete_document -> DELETE FROM DATABASE IDENTIFIER COLLECTION IDENTIFIER WHERE LBRACE document RBRACE','delete_document',10,'p_delete_document','analizer.py',105),
  ('delete_collection -> DELETE COLLECTION IDENTIFIER FROM DATABASE IDENTIFIER','delete_collection',6,'p_delete_collection','analizer.py',109),
  ('document -> STRING COLON value','document',3,'p_document','analizer.py',113),
  ('document -> document COMMA STRING COLON value','document',5,'p_document','analizer.py',114),
  ('value -> STRING','value',1,'p_value','analizer.py',122),
  ('value -> NUMBER','value',1,'p_value','analizer.py',123),
  ('value -> TRUE','value',1,'p_value','analizer.py',124),
  ('value -> FALSE','value',1,'p_value','analizer.py',125),
  ('value -> NULL','value',1,'p_value','analizer.py',126),
]