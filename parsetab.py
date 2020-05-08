
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALS AND ASSIGN AUS BEGIN BREAK BTAND BTNOT BTOR COLON COMMA COMMENT DANN DIM DIVIDE DOT EIN ENDE EQ FLOAT FLT FUR GE GSUB GT ID LBRKT LE LPAREN LT MINUS MODULO NE NOT OR PLUS PROGRAMM QUOTE RBRKT RPAREN RUKKHER SCHLUSS SONNST STR STRING SUB SWENN TIMES TUN VALUE WAHREND WENN WORD WRD newline\n    program : PROGRAMM V R B SCHLUSS\n    \n    V : V0 V\n    |\n    \n    V0 : DIM ID V1\n    | DIM ID V2\n    \n    V1 : COMMA ID V1\n    | COMMA ID V2\n    \n    V2 : ALS TYPE AMC0\n    \n    R : R0 COLON B RUKKHER R \n    |\n    \n    R0 : SUB ID\n    \n    B : BEGIN S\n    \n    S : S0 S\n    |\n    \n    S0 : IDORAMC ASSIGN E\n    | EIN LPAREN IDORAMC INPUT RPAREN\n    | AUS LPAREN EXP OUTPUT RPAREN\n    | GSUB ID\n    | W SD END\n    | WAHREND CONDITION S ENDE\n    | TUN S WAHREND CONDITION\n    |\n    \n    E : T\n    | E PLUS T\n    | E MINUS T\n    \n    T : F\n    | T TIMES F\n    | T DIVIDE F\n    |\n    \n    F : ID\n    | VALUE\n    | FLT\n    | LPAREN E RPAREN\n    |\n    \n    EXP : \n    \n    IDORAMC : ID\n    | ID AMC1\n    \n    EIDORAMC : ID\n    | ID AMC1\n    \n    CONDITION : LPAREN CMP GT CMP RPAREN\n    | LPAREN CMP GE CMP RPAREN\n    | LPAREN CMP EQ CMP RPAREN\n    | LPAREN CMP NE CMP RPAREN\n    | LPAREN CMP LE CMP RPAREN\n    | LPAREN CMP LT CMP RPAREN\n    | CONDITION AND CONDITION\n    | CONDITION OR CONDITION\n    \n    CMP : VALUE\n    | ID\n    | FLT\n    \n    W : W0 W1\n    \n    W0 : WENN CONDITION\n    \n    W1 : DANN S\n    \n    SD : SD0 W1\n    |\n    \n    SD0 : SONNST\n    \n    END : ENDE\n    \n    INPUT : COMMA IDORAMC INPUT\n    |\n    \n    OUTPUT : COMMA EXP OUTPUT\n    |\n    \n    TYPE : WORD \n    | FLOAT \n    | STRING     \n    \n    AMC0 :  AMC1\n    |\n    \n    AMC1 : LBRKT VALUE RBRKT AMC2\n    | LBRKT ID RBRKT AMC2\n    | LBRKT VALUE RBRKT\n    | LBRKT ID RBRKT\n    |\n    \n    AMC2 : LBRKT VALUE RBRKT AMC3\n    | LBRKT ID RBRKT AMC3\n    | LBRKT VALUE RBRKT\n    | LBRKT ID RBRKT\n    |\n    \n    AMC3 : LBRKT VALUE RBRKT \n    | LBRKT ID RBRKT\n    |\n    '
    
_lr_action_items = {'PROGRAMM':([0,],[2,]),'$end':([1,19,],[0,-1,]),'SUB':([2,3,4,9,15,16,34,35,36,37,54,55,56,57,58,92,93,114,115,132,133,135,136,139,140,],[-3,8,-3,-2,-4,-5,-66,-62,-63,-64,8,-6,-7,-8,-65,-69,-70,-67,-68,-74,-75,-72,-73,-77,-78,]),'BEGIN':([2,3,4,6,9,13,15,16,34,35,36,37,54,55,56,57,58,82,92,93,114,115,132,133,135,136,139,140,],[-3,-10,-3,12,-2,12,-4,-5,-66,-62,-63,-64,-10,-6,-7,-8,-65,-9,-69,-70,-67,-68,-74,-75,-72,-73,-77,-78,]),'DIM':([2,4,15,16,34,35,36,37,55,56,57,58,92,93,114,115,132,133,135,136,139,140,],[5,5,-4,-5,-66,-62,-63,-64,-6,-7,-8,-65,-69,-70,-67,-68,-74,-75,-72,-73,-77,-78,]),'ID':([5,8,12,17,21,25,29,39,40,42,44,48,49,52,59,60,61,62,63,64,65,70,71,83,84,85,86,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,113,126,127,128,129,130,131,134,],[10,14,26,33,26,42,26,62,26,-18,69,26,78,26,-15,-23,-26,-30,-31,-32,62,-19,-57,62,62,62,62,26,-20,-46,-47,78,78,78,78,78,78,-21,-24,-25,-27,-28,-33,-16,-17,125,-40,-41,-42,-43,-44,-45,138,]),'COLON':([7,14,],[13,-11,]),'COMMA':([10,26,33,41,43,66,67,91,92,93,110,112,114,115,132,133,135,136,139,140,],[17,-36,17,-35,-37,89,91,-35,-69,-70,89,91,-67,-68,-74,-75,-72,-73,-77,-78,]),'ALS':([10,33,],[18,18,]),'SCHLUSS':([11,12,20,21,38,39,42,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[19,-14,-12,-14,-13,-29,-18,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'RUKKHER':([12,20,21,32,38,39,42,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[-14,-12,-14,54,-13,-29,-18,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'EIN':([12,21,29,39,42,48,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[23,23,23,-29,-18,23,23,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'AUS':([12,21,29,39,42,48,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[24,24,24,-29,-18,24,24,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'GSUB':([12,21,29,39,42,48,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[25,25,25,-29,-18,25,25,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'WAHREND':([12,21,29,38,39,42,48,50,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[28,28,28,-13,-29,-18,28,80,28,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'TUN':([12,21,29,39,42,48,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[29,29,29,-29,-18,29,29,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'WENN':([12,21,29,39,42,48,52,59,60,61,62,63,64,70,71,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[31,31,31,-29,-18,31,31,-15,-23,-26,-30,-31,-32,-19,-57,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'WORD':([18,],[35,]),'FLOAT':([18,],[36,]),'STRING':([18,],[37,]),'ENDE':([21,27,38,39,42,45,48,51,52,59,60,61,62,63,64,70,71,72,73,81,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[-14,-55,-13,-29,-18,71,-14,-51,-14,-15,-23,-26,-30,-31,-32,-19,-57,-54,94,-53,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'SONNST':([21,27,38,39,42,51,52,59,60,61,62,63,64,70,71,81,83,84,85,86,94,95,96,103,104,105,106,107,108,109,111,126,127,128,129,130,131,],[-14,47,-13,-29,-18,-51,-14,-15,-23,-26,-30,-31,-32,-19,-57,-53,-29,-29,-34,-34,-20,-46,-47,-21,-24,-25,-27,-28,-33,-16,-17,-40,-41,-42,-43,-44,-45,]),'ASSIGN':([22,26,43,92,93,114,115,132,133,135,136,139,140,],[39,-36,-37,-69,-70,-67,-68,-74,-75,-72,-73,-77,-78,]),'LPAREN':([23,24,28,31,39,65,74,75,80,83,84,85,86,],[40,41,49,49,65,65,49,49,49,65,65,65,65,]),'RPAREN':([26,41,43,60,61,62,63,64,65,66,67,77,78,79,83,84,85,86,87,88,90,91,92,93,104,105,106,107,108,110,112,114,115,116,117,118,119,120,121,122,123,132,133,135,136,139,140,],[-36,-35,-37,-23,-26,-30,-31,-32,-29,-59,-61,-48,-49,-50,-29,-29,-34,-34,108,109,111,-35,-69,-70,-24,-25,-27,-28,-33,-59,-61,-67,-68,126,127,128,129,130,131,-58,-60,-74,-75,-72,-73,-77,-78,]),'LBRKT':([26,34,35,36,37,92,93,132,133,],[44,44,-62,-63,-64,113,113,134,134,]),'DANN':([30,46,47,53,95,96,126,127,128,129,130,131,],[52,52,-56,-52,-46,-47,-40,-41,-42,-43,-44,-45,]),'TIMES':([39,60,61,62,63,64,65,83,84,85,86,104,105,106,107,108,],[-29,85,-26,-30,-31,-32,-29,-29,-29,-34,-34,85,85,-27,-28,-33,]),'DIVIDE':([39,60,61,62,63,64,65,83,84,85,86,104,105,106,107,108,],[-29,86,-26,-30,-31,-32,-29,-29,-29,-34,-34,86,86,-27,-28,-33,]),'PLUS':([39,59,60,61,62,63,64,65,83,84,85,86,87,104,105,106,107,108,],[-29,83,-23,-26,-30,-31,-32,-29,-29,-29,-34,-34,83,-24,-25,-27,-28,-33,]),'MINUS':([39,59,60,61,62,63,64,65,83,84,85,86,87,104,105,106,107,108,],[-29,84,-23,-26,-30,-31,-32,-29,-29,-29,-34,-34,84,-24,-25,-27,-28,-33,]),'VALUE':([39,44,49,65,83,84,85,86,97,98,99,100,101,102,113,134,],[63,68,77,63,63,63,63,63,77,77,77,77,77,77,124,137,]),'FLT':([39,49,65,83,84,85,86,97,98,99,100,101,102,],[64,79,64,64,64,64,64,79,79,79,79,79,79,]),'AND':([48,53,95,96,103,126,127,128,129,130,131,],[74,74,74,74,74,-40,-41,-42,-43,-44,-45,]),'OR':([48,53,95,96,103,126,127,128,129,130,131,],[75,75,75,75,75,-40,-41,-42,-43,-44,-45,]),'RBRKT':([68,69,124,125,137,138,],[92,93,132,133,139,140,]),'GT':([76,77,78,79,],[97,-48,-49,-50,]),'GE':([76,77,78,79,],[98,-48,-49,-50,]),'EQ':([76,77,78,79,],[99,-48,-49,-50,]),'NE':([76,77,78,79,],[100,-48,-49,-50,]),'LE':([76,77,78,79,],[101,-48,-49,-50,]),'LT':([76,77,78,79,],[102,-48,-49,-50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'V':([2,4,],[3,9,]),'V0':([2,4,],[4,4,]),'R':([3,54,],[6,82,]),'R0':([3,54,],[7,7,]),'B':([6,13,],[11,32,]),'V1':([10,33,],[15,55,]),'V2':([10,33,],[16,56,]),'S':([12,21,29,48,52,],[20,38,50,73,81,]),'S0':([12,21,29,48,52,],[21,21,21,21,21,]),'IDORAMC':([12,21,29,40,48,52,89,],[22,22,22,66,22,22,110,]),'W':([12,21,29,48,52,],[27,27,27,27,27,]),'W0':([12,21,29,48,52,],[30,30,30,30,30,]),'TYPE':([18,],[34,]),'AMC1':([26,34,],[43,58,]),'SD':([27,],[45,]),'SD0':([27,],[46,]),'CONDITION':([28,31,74,75,80,],[48,53,95,96,103,]),'W1':([30,46,],[51,72,]),'AMC0':([34,],[57,]),'E':([39,65,],[59,87,]),'T':([39,65,83,84,],[60,60,104,105,]),'F':([39,65,83,84,85,86,],[61,61,61,61,106,107,]),'EXP':([41,91,],[67,112,]),'END':([45,],[70,]),'CMP':([49,97,98,99,100,101,102,],[76,116,117,118,119,120,121,]),'INPUT':([66,110,],[88,122,]),'OUTPUT':([67,112,],[90,123,]),'AMC2':([92,93,],[114,115,]),'AMC3':([132,133,],[135,136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMM V R B SCHLUSS','program',5,'p_program','elementar.py',192),
  ('V -> V0 V','V',2,'p_V','elementar.py',198),
  ('V -> <empty>','V',0,'p_V','elementar.py',199),
  ('V0 -> DIM ID V1','V0',3,'p_V0','elementar.py',204),
  ('V0 -> DIM ID V2','V0',3,'p_V0','elementar.py',205),
  ('V1 -> COMMA ID V1','V1',3,'p_V1','elementar.py',211),
  ('V1 -> COMMA ID V2','V1',3,'p_V1','elementar.py',212),
  ('V2 -> ALS TYPE AMC0','V2',3,'p_V2','elementar.py',218),
  ('R -> R0 COLON B RUKKHER R','R',5,'p_R','elementar.py',223),
  ('R -> <empty>','R',0,'p_R','elementar.py',224),
  ('R0 -> SUB ID','R0',2,'p_R0','elementar.py',229),
  ('B -> BEGIN S','B',2,'p_B','elementar.py',235),
  ('S -> S0 S','S',2,'p_S','elementar.py',240),
  ('S -> <empty>','S',0,'p_S','elementar.py',241),
  ('S0 -> IDORAMC ASSIGN E','S0',3,'p_S0','elementar.py',246),
  ('S0 -> EIN LPAREN IDORAMC INPUT RPAREN','S0',5,'p_S0','elementar.py',247),
  ('S0 -> AUS LPAREN EXP OUTPUT RPAREN','S0',5,'p_S0','elementar.py',248),
  ('S0 -> GSUB ID','S0',2,'p_S0','elementar.py',249),
  ('S0 -> W SD END','S0',3,'p_S0','elementar.py',250),
  ('S0 -> WAHREND CONDITION S ENDE','S0',4,'p_S0','elementar.py',251),
  ('S0 -> TUN S WAHREND CONDITION','S0',4,'p_S0','elementar.py',252),
  ('S0 -> <empty>','S0',0,'p_S0','elementar.py',253),
  ('E -> T','E',1,'p_E','elementar.py',279),
  ('E -> E PLUS T','E',3,'p_E','elementar.py',280),
  ('E -> E MINUS T','E',3,'p_E','elementar.py',281),
  ('T -> F','T',1,'p_T','elementar.py',303),
  ('T -> T TIMES F','T',3,'p_T','elementar.py',304),
  ('T -> T DIVIDE F','T',3,'p_T','elementar.py',305),
  ('T -> <empty>','T',0,'p_T','elementar.py',306),
  ('F -> ID','F',1,'p_F','elementar.py',317),
  ('F -> VALUE','F',1,'p_F','elementar.py',318),
  ('F -> FLT','F',1,'p_F','elementar.py',319),
  ('F -> LPAREN E RPAREN','F',3,'p_F','elementar.py',320),
  ('F -> <empty>','F',0,'p_F','elementar.py',321),
  ('EXP -> <empty>','EXP',0,'p_EXP','elementar.py',330),
  ('IDORAMC -> ID','IDORAMC',1,'p_IDORAMC','elementar.py',344),
  ('IDORAMC -> ID AMC1','IDORAMC',2,'p_IDORAMC','elementar.py',345),
  ('EIDORAMC -> ID','EIDORAMC',1,'p_EIDORAMC','elementar.py',352),
  ('EIDORAMC -> ID AMC1','EIDORAMC',2,'p_EIDORAMC','elementar.py',353),
  ('CONDITION -> LPAREN CMP GT CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',358),
  ('CONDITION -> LPAREN CMP GE CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',359),
  ('CONDITION -> LPAREN CMP EQ CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',360),
  ('CONDITION -> LPAREN CMP NE CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',361),
  ('CONDITION -> LPAREN CMP LE CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',362),
  ('CONDITION -> LPAREN CMP LT CMP RPAREN','CONDITION',5,'p_CONDITION','elementar.py',363),
  ('CONDITION -> CONDITION AND CONDITION','CONDITION',3,'p_CONDITION','elementar.py',364),
  ('CONDITION -> CONDITION OR CONDITION','CONDITION',3,'p_CONDITION','elementar.py',365),
  ('CMP -> VALUE','CMP',1,'p_CMP','elementar.py',389),
  ('CMP -> ID','CMP',1,'p_CMP','elementar.py',390),
  ('CMP -> FLT','CMP',1,'p_CMP','elementar.py',391),
  ('W -> W0 W1','W',2,'p_W','elementar.py',400),
  ('W0 -> WENN CONDITION','W0',2,'p_W0','elementar.py',405),
  ('W1 -> DANN S','W1',2,'p_W1','elementar.py',416),
  ('SD -> SD0 W1','SD',2,'p_SD','elementar.py',429),
  ('SD -> <empty>','SD',0,'p_SD','elementar.py',430),
  ('SD0 -> SONNST','SD0',1,'p_SD0','elementar.py',436),
  ('END -> ENDE','END',1,'p_END','elementar.py',446),
  ('INPUT -> COMMA IDORAMC INPUT','INPUT',3,'p_INPUT','elementar.py',452),
  ('INPUT -> <empty>','INPUT',0,'p_INPUT','elementar.py',453),
  ('OUTPUT -> COMMA EXP OUTPUT','OUTPUT',3,'p_OUTPUT','elementar.py',458),
  ('OUTPUT -> <empty>','OUTPUT',0,'p_OUTPUT','elementar.py',459),
  ('TYPE -> WORD','TYPE',1,'p_TYPE','elementar.py',464),
  ('TYPE -> FLOAT','TYPE',1,'p_TYPE','elementar.py',465),
  ('TYPE -> STRING','TYPE',1,'p_TYPE','elementar.py',466),
  ('AMC0 -> AMC1','AMC0',1,'p_AMC0','elementar.py',475),
  ('AMC0 -> <empty>','AMC0',0,'p_AMC0','elementar.py',476),
  ('AMC1 -> LBRKT VALUE RBRKT AMC2','AMC1',4,'p_AMC1','elementar.py',482),
  ('AMC1 -> LBRKT ID RBRKT AMC2','AMC1',4,'p_AMC1','elementar.py',483),
  ('AMC1 -> LBRKT VALUE RBRKT','AMC1',3,'p_AMC1','elementar.py',484),
  ('AMC1 -> LBRKT ID RBRKT','AMC1',3,'p_AMC1','elementar.py',485),
  ('AMC1 -> <empty>','AMC1',0,'p_AMC1','elementar.py',486),
  ('AMC2 -> LBRKT VALUE RBRKT AMC3','AMC2',4,'p_AMC2','elementar.py',494),
  ('AMC2 -> LBRKT ID RBRKT AMC3','AMC2',4,'p_AMC2','elementar.py',495),
  ('AMC2 -> LBRKT VALUE RBRKT','AMC2',3,'p_AMC2','elementar.py',496),
  ('AMC2 -> LBRKT ID RBRKT','AMC2',3,'p_AMC2','elementar.py',497),
  ('AMC2 -> <empty>','AMC2',0,'p_AMC2','elementar.py',498),
  ('AMC3 -> LBRKT VALUE RBRKT','AMC3',3,'p_AMC3','elementar.py',506),
  ('AMC3 -> LBRKT ID RBRKT','AMC3',3,'p_AMC3','elementar.py',507),
  ('AMC3 -> <empty>','AMC3',0,'p_AMC3','elementar.py',508),
]
