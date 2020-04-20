
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALS AND ASSIGN AUS BEGIN BREAK BTAND BTNOT BTOR COLON COMMA COMMENT DANN DIM DIVIDE DOT EIN ENDE EQ FLOAT FLT FUR GE GSUB GT ID LBRKT LE LPAREN LT MINUS MODULO NE NOT OR PLUS PROGRAMM QUOTE RBRKT RPAREN RUKKHER SCHLUSS SONNST STR STRING SUB SWENN TIMES TUN VALUE WAHREND WENN WORD newline\n    program : PROGRAMM V R B SCHLUSS\n    \n    V : V0 V\n    |\n    \n    V0 : DIM ID V1\n    | DIM ID V2\n    \n    V1 : COMMA ID V1\n    | COMMA ID V2\n    \n    V2 : ALS TYPE AMC0\n    \n    R : R0 COLON B RUKKHER R \n    |\n    \n    R0 : SUB ID\n    \n    B : BEGIN S\n    \n    S : S0 S\n    |\n    \n    S0 : IDORAMC ASSIGN E\n    | EIN LPAREN IDORAMC INPUT RPAREN\n    | AUS LPAREN E OUTPUT RPAREN\n    | GSUB ID\n    | WENN CONDITION DANN S SW SD ENDE\n    | WAHREND CONDITION S ENDE\n    | TUN S WAHREND CONDITION\n    |\n    \n    IDORAMC : ID\n    | ID AMC1\n    \n    EIDORAMC : ID\n    | ID AMC1\n    \n    CONDITION : LPAREN CMP COMPARATOR CMP RPAREN\n    | CONDITION AND CONDITION\n    | CONDITION OR CONDITION\n    \n    CMP : VALUE\n    | IDORAMC\n    | FLT\n    \n    COMPARATOR : GT\n    | GE\n    | EQ\n    | NE\n    | LE\n    | LT\n    \n    SW : SWENN CONDITION DANN S SW\n    |\n    \n    SD : SONNST DANN S\n    |\n    \n    E : VALUE\n    | FLT\n    | STR\n    | EIDORAMC\n    | VALUE OPERATOR E\n    | FLT OPERATOR E\n    | STR OPERATOR E\n    | IDORAMC OPERATOR E\n    \n    OPERATOR : PLUS\n    | TIMES\n    | MINUS\n    | DIVIDE\n    | MODULO\n    \n    INPUT : COMMA IDORAMC INPUT\n    |\n    \n    OUTPUT : COMMA E OUTPUT\n    |\n    \n    TYPE : WORD \n    | FLOAT \n    | STRING     \n    \n    AMC0 :  AMC1\n    |\n    \n    AMC1 : LBRKT VALUE RBRKT AMC2\n    | LBRKT ID RBRKT AMC2\n    | LBRKT VALUE RBRKT\n    | LBRKT ID RBRKT\n    |\n    \n    AMC2 : LBRKT VALUE RBRKT AMC3\n    | LBRKT ID RBRKT AMC3\n    | LBRKT VALUE RBRKT\n    | LBRKT ID RBRKT\n    |\n    \n    AMC3 : LBRKT VALUE RBRKT \n    | LBRKT ID RBRKT\n    |\n    '
    
_lr_action_items = {'PROGRAMM':([0,],[2,]),'$end':([1,19,],[0,-1,]),'SUB':([2,3,4,9,15,16,32,33,34,35,47,48,49,50,51,87,88,110,111,123,124,129,130,136,137,],[-3,8,-3,-2,-4,-5,-64,-60,-61,-62,8,-6,-7,-8,-63,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'BEGIN':([2,3,4,6,9,13,15,16,32,33,34,35,47,48,49,50,51,72,87,88,110,111,123,124,129,130,136,137,],[-3,-10,-3,12,-2,12,-4,-5,-64,-60,-61,-62,-10,-6,-7,-8,-63,-9,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'DIM':([2,4,15,16,32,33,34,35,48,49,50,51,87,88,110,111,123,124,129,130,136,137,],[5,5,-4,-5,-64,-60,-61,-62,-6,-7,-8,-63,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'ID':([5,8,12,17,21,25,29,37,38,39,40,42,44,45,53,54,55,56,57,58,63,73,74,75,76,77,78,79,80,81,82,84,86,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,109,110,111,122,123,124,125,126,127,128,129,130,136,137,],[10,14,26,31,26,40,26,58,26,58,-18,62,26,26,-15,-43,-44,-45,-46,-25,26,58,-51,-52,-53,-54,-55,58,58,58,-26,26,58,-67,-68,-28,-29,26,-33,-34,-35,-36,-37,-38,-20,-21,-50,-47,-48,-49,-16,-17,118,-65,-66,-27,-72,-73,-19,26,26,134,-70,-71,-75,-76,]),'COLON':([7,14,],[13,-11,]),'COMMA':([10,26,31,41,54,55,56,57,58,59,60,82,87,88,101,102,103,104,106,108,110,111,123,124,129,130,136,137,],[17,-23,17,-24,-43,-44,-45,-46,-25,84,86,-26,-67,-68,-50,-47,-48,-49,84,86,-65,-66,-72,-73,-70,-71,-75,-76,]),'ALS':([10,31,],[18,18,]),'SCHLUSS':([11,12,20,21,36,40,53,54,55,56,57,58,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,129,130,136,137,],[19,-14,-12,-14,-13,-18,-15,-43,-44,-45,-46,-25,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,-70,-71,-75,-76,]),'RUKKHER':([12,20,21,30,36,40,53,54,55,56,57,58,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,129,130,136,137,],[-14,-12,-14,47,-13,-18,-15,-43,-44,-45,-46,-25,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,-70,-71,-75,-76,]),'EIN':([12,21,29,40,45,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[23,23,23,-18,23,-15,-43,-44,-45,-46,-25,23,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,23,23,-70,-71,-75,-76,]),'AUS':([12,21,29,40,45,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[24,24,24,-18,24,-15,-43,-44,-45,-46,-25,24,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,24,24,-70,-71,-75,-76,]),'GSUB':([12,21,29,40,45,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[25,25,25,-18,25,-15,-43,-44,-45,-46,-25,25,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,25,25,-70,-71,-75,-76,]),'WENN':([12,21,29,40,45,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[27,27,27,-18,27,-15,-43,-44,-45,-46,-25,27,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,27,27,-70,-71,-75,-76,]),'WAHREND':([12,21,29,36,40,45,46,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[28,28,28,-13,-18,28,71,-15,-43,-44,-45,-46,-25,28,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,28,28,-70,-71,-75,-76,]),'TUN':([12,21,29,40,45,53,54,55,56,57,58,63,82,87,88,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,126,127,129,130,136,137,],[29,29,29,-18,29,-15,-43,-44,-45,-46,-25,29,-26,-67,-68,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,29,29,-70,-71,-75,-76,]),'WORD':([18,],[33,]),'FLOAT':([18,],[34,]),'STRING':([18,],[35,]),'ENDE':([21,36,40,45,53,54,55,56,57,58,63,70,82,87,88,89,90,91,99,100,101,102,103,104,105,107,110,111,112,119,122,123,124,125,126,127,129,130,131,132,135,136,137,],[-14,-13,-18,-14,-15,-43,-44,-45,-46,-25,-14,99,-26,-67,-68,-40,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-42,125,-27,-72,-73,-19,-14,-14,-70,-71,-41,-40,-39,-75,-76,]),'SWENN':([21,36,40,53,54,55,56,57,58,63,82,87,88,89,90,91,99,100,101,102,103,104,105,107,110,111,122,123,124,125,127,129,130,132,136,137,],[-14,-13,-18,-15,-43,-44,-45,-46,-25,-14,-26,-67,-68,113,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,-27,-72,-73,-19,-14,-70,-71,113,-75,-76,]),'SONNST':([21,36,40,53,54,55,56,57,58,63,82,87,88,89,90,91,99,100,101,102,103,104,105,107,110,111,112,122,123,124,125,127,129,130,132,135,136,137,],[-14,-13,-18,-15,-43,-44,-45,-46,-25,-14,-26,-67,-68,-40,-28,-29,-20,-21,-50,-47,-48,-49,-16,-17,-65,-66,120,-27,-72,-73,-19,-14,-70,-71,-40,-39,-75,-76,]),'ASSIGN':([22,26,41,87,88,110,111,123,124,129,130,136,137,],[37,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'LPAREN':([23,24,27,28,64,65,71,113,],[38,39,44,44,44,44,44,44,]),'RPAREN':([26,41,54,55,56,57,58,59,60,67,68,69,82,83,85,87,88,101,102,103,104,106,108,110,111,114,115,116,123,124,129,130,136,137,],[-23,-24,-43,-44,-45,-46,-25,-57,-59,-30,-31,-32,-26,105,107,-67,-68,-50,-47,-48,-49,-57,-59,-65,-66,122,-56,-58,-72,-73,-70,-71,-75,-76,]),'GT':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,93,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'GE':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,94,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'EQ':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,95,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'NE':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,96,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'LE':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,97,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'LT':([26,41,66,67,68,69,87,88,110,111,123,124,129,130,136,137,],[-23,-24,98,-30,-31,-32,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'LBRKT':([26,32,33,34,35,58,87,88,123,124,],[42,42,-60,-61,-62,42,109,109,128,128,]),'VALUE':([37,39,42,44,73,74,75,76,77,78,79,80,81,86,92,93,94,95,96,97,98,109,128,],[54,54,61,67,54,-51,-52,-53,-54,-55,54,54,54,54,67,-33,-34,-35,-36,-37,-38,117,133,]),'FLT':([37,39,44,73,74,75,76,77,78,79,80,81,86,92,93,94,95,96,97,98,],[55,55,69,55,-51,-52,-53,-54,-55,55,55,55,55,69,-33,-34,-35,-36,-37,-38,]),'STR':([37,39,73,74,75,76,77,78,79,80,81,86,],[56,56,56,-51,-52,-53,-54,-55,56,56,56,56,]),'DANN':([43,90,91,120,121,122,],[63,-28,-29,126,127,-27,]),'AND':([43,45,90,91,100,121,122,],[64,64,64,64,64,64,-27,]),'OR':([43,45,90,91,100,121,122,],[65,65,65,65,65,65,-27,]),'PLUS':([52,54,55,56,58,82,87,88,110,111,123,124,129,130,136,137,],[74,74,74,74,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'TIMES':([52,54,55,56,58,82,87,88,110,111,123,124,129,130,136,137,],[75,75,75,75,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'MINUS':([52,54,55,56,58,82,87,88,110,111,123,124,129,130,136,137,],[76,76,76,76,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'DIVIDE':([52,54,55,56,58,82,87,88,110,111,123,124,129,130,136,137,],[77,77,77,77,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'MODULO':([52,54,55,56,58,82,87,88,110,111,123,124,129,130,136,137,],[78,78,78,78,-23,-24,-67,-68,-65,-66,-72,-73,-70,-71,-75,-76,]),'RBRKT':([61,62,117,118,133,134,],[87,88,123,124,136,137,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'V':([2,4,],[3,9,]),'V0':([2,4,],[4,4,]),'R':([3,47,],[6,72,]),'R0':([3,47,],[7,7,]),'B':([6,13,],[11,30,]),'V1':([10,31,],[15,48,]),'V2':([10,31,],[16,49,]),'S':([12,21,29,45,63,126,127,],[20,36,46,70,89,131,132,]),'S0':([12,21,29,45,63,126,127,],[21,21,21,21,21,21,21,]),'IDORAMC':([12,21,29,37,38,39,44,45,63,73,79,80,81,84,86,92,126,127,],[22,22,22,52,59,52,68,22,22,52,52,52,52,106,52,68,22,22,]),'TYPE':([18,],[32,]),'AMC1':([26,32,58,],[41,51,82,]),'CONDITION':([27,28,64,65,71,113,],[43,45,90,91,100,121,]),'AMC0':([32,],[50,]),'E':([37,39,73,79,80,81,86,],[53,60,101,102,103,104,108,]),'EIDORAMC':([37,39,73,79,80,81,86,],[57,57,57,57,57,57,57,]),'CMP':([44,92,],[66,114,]),'OPERATOR':([52,54,55,56,],[73,79,80,81,]),'INPUT':([59,106,],[83,115,]),'OUTPUT':([60,108,],[85,116,]),'COMPARATOR':([66,],[92,]),'AMC2':([87,88,],[110,111,]),'SW':([89,132,],[112,135,]),'SD':([112,],[119,]),'AMC3':([123,124,],[129,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMM V R B SCHLUSS','program',5,'p_program','elementar.py',180),
  ('V -> V0 V','V',2,'p_V','elementar.py',186),
  ('V -> <empty>','V',0,'p_V','elementar.py',187),
  ('V0 -> DIM ID V1','V0',3,'p_V0','elementar.py',192),
  ('V0 -> DIM ID V2','V0',3,'p_V0','elementar.py',193),
  ('V1 -> COMMA ID V1','V1',3,'p_V1','elementar.py',199),
  ('V1 -> COMMA ID V2','V1',3,'p_V1','elementar.py',200),
  ('V2 -> ALS TYPE AMC0','V2',3,'p_V2','elementar.py',206),
  ('R -> R0 COLON B RUKKHER R','R',5,'p_R','elementar.py',211),
  ('R -> <empty>','R',0,'p_R','elementar.py',212),
  ('R0 -> SUB ID','R0',2,'p_R0','elementar.py',217),
  ('B -> BEGIN S','B',2,'p_B','elementar.py',223),
  ('S -> S0 S','S',2,'p_S','elementar.py',235),
  ('S -> <empty>','S',0,'p_S','elementar.py',236),
  ('S0 -> IDORAMC ASSIGN E','S0',3,'p_S0','elementar.py',241),
  ('S0 -> EIN LPAREN IDORAMC INPUT RPAREN','S0',5,'p_S0','elementar.py',242),
  ('S0 -> AUS LPAREN E OUTPUT RPAREN','S0',5,'p_S0','elementar.py',243),
  ('S0 -> GSUB ID','S0',2,'p_S0','elementar.py',244),
  ('S0 -> WENN CONDITION DANN S SW SD ENDE','S0',7,'p_S0','elementar.py',245),
  ('S0 -> WAHREND CONDITION S ENDE','S0',4,'p_S0','elementar.py',246),
  ('S0 -> TUN S WAHREND CONDITION','S0',4,'p_S0','elementar.py',247),
  ('S0 -> <empty>','S0',0,'p_S0','elementar.py',248),
  ('IDORAMC -> ID','IDORAMC',1,'p_IDORAMC','elementar.py',257),
  ('IDORAMC -> ID AMC1','IDORAMC',2,'p_IDORAMC','elementar.py',258),
  ('EIDORAMC -> ID','EIDORAMC',1,'p_EIDORAMC','elementar.py',265),
  ('EIDORAMC -> ID AMC1','EIDORAMC',2,'p_EIDORAMC','elementar.py',266),
  ('CONDITION -> LPAREN CMP COMPARATOR CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',271),
  ('CONDITION -> CONDITION AND CONDITION','CONDITION',3,'p_CONDITION','elementar.py',272),
  ('CONDITION -> CONDITION OR CONDITION','CONDITION',3,'p_CONDITION','elementar.py',273),
  ('CMP -> VALUE','CMP',1,'p_CMP','elementar.py',278),
  ('CMP -> IDORAMC','CMP',1,'p_CMP','elementar.py',279),
  ('CMP -> FLT','CMP',1,'p_CMP','elementar.py',280),
  ('COMPARATOR -> GT','COMPARATOR',1,'p_COMPARATOR','elementar.py',284),
  ('COMPARATOR -> GE','COMPARATOR',1,'p_COMPARATOR','elementar.py',285),
  ('COMPARATOR -> EQ','COMPARATOR',1,'p_COMPARATOR','elementar.py',286),
  ('COMPARATOR -> NE','COMPARATOR',1,'p_COMPARATOR','elementar.py',287),
  ('COMPARATOR -> LE','COMPARATOR',1,'p_COMPARATOR','elementar.py',288),
  ('COMPARATOR -> LT','COMPARATOR',1,'p_COMPARATOR','elementar.py',289),
  ('SW -> SWENN CONDITION DANN S SW','SW',5,'p_SW','elementar.py',294),
  ('SW -> <empty>','SW',0,'p_SW','elementar.py',295),
  ('SD -> SONNST DANN S','SD',3,'p_SD','elementar.py',300),
  ('SD -> <empty>','SD',0,'p_SD','elementar.py',301),
  ('E -> VALUE','E',1,'p_E','elementar.py',306),
  ('E -> FLT','E',1,'p_E','elementar.py',307),
  ('E -> STR','E',1,'p_E','elementar.py',308),
  ('E -> EIDORAMC','E',1,'p_E','elementar.py',309),
  ('E -> VALUE OPERATOR E','E',3,'p_E','elementar.py',310),
  ('E -> FLT OPERATOR E','E',3,'p_E','elementar.py',311),
  ('E -> STR OPERATOR E','E',3,'p_E','elementar.py',312),
  ('E -> IDORAMC OPERATOR E','E',3,'p_E','elementar.py',313),
  ('OPERATOR -> PLUS','OPERATOR',1,'p_OPERATOR','elementar.py',318),
  ('OPERATOR -> TIMES','OPERATOR',1,'p_OPERATOR','elementar.py',319),
  ('OPERATOR -> MINUS','OPERATOR',1,'p_OPERATOR','elementar.py',320),
  ('OPERATOR -> DIVIDE','OPERATOR',1,'p_OPERATOR','elementar.py',321),
  ('OPERATOR -> MODULO','OPERATOR',1,'p_OPERATOR','elementar.py',322),
  ('INPUT -> COMMA IDORAMC INPUT','INPUT',3,'p_INPUT','elementar.py',327),
  ('INPUT -> <empty>','INPUT',0,'p_INPUT','elementar.py',328),
  ('OUTPUT -> COMMA E OUTPUT','OUTPUT',3,'p_OUTPUT','elementar.py',333),
  ('OUTPUT -> <empty>','OUTPUT',0,'p_OUTPUT','elementar.py',334),
  ('TYPE -> WORD','TYPE',1,'p_TYPE','elementar.py',339),
  ('TYPE -> FLOAT','TYPE',1,'p_TYPE','elementar.py',340),
  ('TYPE -> STRING','TYPE',1,'p_TYPE','elementar.py',341),
  ('AMC0 -> AMC1','AMC0',1,'p_AMC0','elementar.py',350),
  ('AMC0 -> <empty>','AMC0',0,'p_AMC0','elementar.py',351),
  ('AMC1 -> LBRKT VALUE RBRKT AMC2','AMC1',4,'p_AMC1','elementar.py',357),
  ('AMC1 -> LBRKT ID RBRKT AMC2','AMC1',4,'p_AMC1','elementar.py',358),
  ('AMC1 -> LBRKT VALUE RBRKT','AMC1',3,'p_AMC1','elementar.py',359),
  ('AMC1 -> LBRKT ID RBRKT','AMC1',3,'p_AMC1','elementar.py',360),
  ('AMC1 -> <empty>','AMC1',0,'p_AMC1','elementar.py',361),
  ('AMC2 -> LBRKT VALUE RBRKT AMC3','AMC2',4,'p_AMC2','elementar.py',369),
  ('AMC2 -> LBRKT ID RBRKT AMC3','AMC2',4,'p_AMC2','elementar.py',370),
  ('AMC2 -> LBRKT VALUE RBRKT','AMC2',3,'p_AMC2','elementar.py',371),
  ('AMC2 -> LBRKT ID RBRKT','AMC2',3,'p_AMC2','elementar.py',372),
  ('AMC2 -> <empty>','AMC2',0,'p_AMC2','elementar.py',373),
  ('AMC3 -> LBRKT VALUE RBRKT','AMC3',3,'p_AMC3','elementar.py',381),
  ('AMC3 -> LBRKT ID RBRKT','AMC3',3,'p_AMC3','elementar.py',382),
  ('AMC3 -> <empty>','AMC3',0,'p_AMC3','elementar.py',383),
]
