
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTleftSUMSUBleftMULDIVASSIGN BOOLEAN BREAK COLON COMMA COMMENT CONTINUE DECR DIV DIV_ASS ELSE EQ FOR FUNCTION GE GT ID IDIV IDIV_ASS IF INCR LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MOD MOD_ASS MUL MUL_ASS NE NEWLINE NULL NUMBER PRINT QUES RBRACE RBRACKET RESERVED RETURN RPAREN SCAN SEMI STRING SUB SUB_ASS SUM SUM_ASS WHILEprogram : program statement\n               | statementprogram : errorstatement : statement command\n                 | command\n            command : function_def\n               | function_call\n               | conditional\n               | ternary_condition\n               | expression\n               | assignment\n               | expression_ass\n               | input\n               | output\n               | for_loop\n               | while_loop\n               | return\n               | break\n               | continue\n               | COMMENT\n               | NEWLINE\n            assignment : ID ASSIGN expression\n                  | ID ASSIGN LBRACKET list RBRACKET\n            input : SCAN LPAREN ID RPAREN\n            output : PRINT LPAREN plist RPAREN\n            plist : pitem\n             | plist COMMA pitem\n            pitem : expressioncondition : expression GT expression\n                 | expression LT expression\n                 | expression GE expression\n                 | expression LE expression\n                 | expression NE expression\n                 | expression EQ expression\n                 | expression LAND expression\n                 | expression LOR expression\n                 | LNOT expression\n                 | BOOLEAN\n                ternary_condition : LPAREN condition RPAREN QUES bloc COLON blocif_bloc : IF LPAREN condition RPAREN blocif_elif_bloc : if_elif_bloc ELSE if_bloc\n                    | if_blocconditional : if_elif_bloc ELSE bloc\n                   | if_elif_bloc\n                bloc : LBRACE stat_bloc RBRACE\n        stat_bloc : stat_bloc command\n                 | command\n            function_def : FUNCTION ID LPAREN param_list RPAREN blocfunction_call : ID LPAREN param_list RPAREN SEMIparam_list : param_list COMMA param\n                  | param\n            param : IDreturn : RETURN expression\n              | RETURN expression SEMI\n    for_loop : FOR LPAREN assignment SEMI condition SEMI expression RPAREN blocwhile_loop : WHILE LPAREN condition RPAREN bloccontinue : CONTINUE\n                | CONTINUE SEMIbreak : BREAK\n             | BREAK SEMIexpression : expression SUM term\n                  | expression SUB term\n       term       : term MUL factor\n                  | term DIV factor\n                  | term IDIV factor\n                  | term MOD factor\n    expression : expression DECR\n                  | expression INCR\n    expression_ass : ID SUM_ASS expression\n                      | ID SUB_ASS expression\n                      | ID MUL_ASS expression\n                      | ID DIV_ASS expression\n                      | ID IDIV_ASS expression\n                      | ID MOD_ASS expression\n    expression : condition\n                  | ternary_condition\n                  | term\n                  | NULL\n            term : factor\n    factor : NUMBER\n              | ID\n              | STRING \n              | ID LBRACKET expression RBRACKET\n        factor : LPAREN expression RPAREN list : list COMMA factor\n             | factor\n             |  '
    
_lr_action_items = {'error':([0,],[3,]),'COMMENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[19,19,19,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,19,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,19,-63,-64,-65,-66,-54,-83,19,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'NEWLINE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[20,20,20,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,20,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,20,-63,-64,-65,-66,-54,-83,20,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'FUNCTION':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[21,21,21,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,21,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,21,-63,-64,-65,-66,-54,-83,21,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,62,63,64,65,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,130,133,135,136,137,138,139,140,144,146,147,149,150,153,154,155,158,159,162,],[22,22,22,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,56,-81,69,-44,-75,-77,-78,69,-59,-57,-42,69,-38,-79,-80,-82,22,-4,69,69,-67,-68,69,69,69,69,69,69,69,69,96,69,69,69,69,69,69,69,69,-76,-81,69,69,69,69,117,69,122,69,-53,-60,-58,-37,69,-61,69,-62,-29,-30,-31,-32,-33,-34,-35,-36,96,-22,69,-69,-70,-71,-72,-73,-74,-84,-43,-41,22,-63,-64,-65,-66,-54,96,-83,22,-47,-24,-25,69,69,-49,-23,69,-45,-46,-56,-40,-48,69,-39,-55,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,68,69,71,72,73,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,147,149,150,153,154,155,158,159,162,],[23,23,23,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,57,23,-44,-75,-77,-78,75,76,77,78,23,-59,-57,-42,23,-38,-79,83,-80,-82,23,-4,85,85,-67,-68,23,23,23,23,23,23,23,23,95,23,23,23,23,23,23,23,23,-76,-81,85,85,85,85,23,23,-53,-60,-58,-37,23,-61,23,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,85,-69,-70,-71,-72,-73,-74,-84,-43,-41,23,-63,-64,-65,-66,-54,-83,23,-47,-24,-25,23,23,-49,-23,85,-45,-46,-56,-40,-48,23,-39,-55,]),'NULL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,149,150,153,154,155,158,159,162,],[27,27,27,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,27,-44,-75,-77,-78,27,-59,-57,-42,27,-38,-79,-80,-82,27,-4,-67,-68,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-76,-81,27,27,-53,-60,-58,-37,27,-61,27,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,27,-63,-64,-65,-66,-54,-83,27,-47,-24,-25,27,27,-49,-23,-45,-46,-56,-40,-48,27,-39,-55,]),'SCAN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[28,28,28,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,28,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,28,-63,-64,-65,-66,-54,-83,28,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[29,29,29,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,29,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,29,-63,-64,-65,-66,-54,-83,29,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'FOR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[30,30,30,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,30,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,30,-63,-64,-65,-66,-54,-83,30,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[31,31,31,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,31,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,31,-63,-64,-65,-66,-54,-83,31,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'RETURN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[32,32,32,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,32,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,32,-63,-64,-65,-66,-54,-83,32,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'BREAK':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[33,33,33,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,33,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,33,-63,-64,-65,-66,-54,-83,33,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'CONTINUE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[34,34,34,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,34,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,34,-63,-64,-65,-66,-54,-83,34,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'LNOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,149,150,153,154,155,158,159,162,],[36,36,36,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,36,-44,-75,-77,-78,36,-59,-57,-42,36,-38,-79,-80,-82,36,-4,-67,-68,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-76,-81,36,36,-53,-60,-58,-37,36,-61,36,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,36,-63,-64,-65,-66,-54,-83,36,-47,-24,-25,36,36,-49,-23,-45,-46,-56,-40,-48,36,-39,-55,]),'BOOLEAN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,149,150,153,154,155,158,159,162,],[37,37,37,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,37,-44,-75,-77,-78,37,-59,-57,-42,37,-38,-79,-80,-82,37,-4,-67,-68,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-76,-81,37,37,-53,-60,-58,-37,37,-61,37,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,37,-63,-64,-65,-66,-54,-83,37,-47,-24,-25,37,37,-49,-23,-45,-46,-56,-40,-48,37,-39,-55,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,70,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[39,39,39,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,39,-4,-67,-68,-76,-81,39,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,39,-63,-64,-65,-66,-54,-83,39,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,68,69,71,72,73,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,147,149,150,153,154,155,158,159,162,],[40,40,40,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,40,-44,-75,-77,-78,40,-59,-57,-42,40,-38,-79,-80,-82,40,-4,40,40,-67,-68,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-76,-81,40,40,40,40,40,40,-53,-60,-58,-37,40,-61,40,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,40,-69,-70,-71,-72,-73,-74,-84,-43,-41,40,-63,-64,-65,-66,-54,-83,40,-47,-24,-25,40,40,-49,-23,40,-45,-46,-56,-40,-48,40,-39,-55,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,68,69,71,72,73,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,102,103,104,105,106,107,109,110,111,112,113,114,115,116,125,133,135,136,137,138,139,140,144,146,147,149,150,153,154,155,158,159,162,],[41,41,41,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,41,-44,-75,-77,-78,41,-59,-57,-42,41,-38,-79,-80,-82,41,-4,41,41,-67,-68,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-76,-81,41,41,41,41,41,41,-53,-60,-58,-37,41,-61,41,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,41,-69,-70,-71,-72,-73,-74,-84,-43,-41,41,-63,-64,-65,-66,-54,-83,41,-47,-24,-25,41,41,-49,-23,41,-45,-46,-56,-40,-48,41,-39,-55,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,42,43,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,113,114,115,116,125,133,137,138,144,146,149,153,154,155,159,162,],[0,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,-1,-4,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,-63,-64,-65,-66,-54,-83,-24,-25,-49,-23,-45,-56,-40,-48,-39,-55,]),'RBRACE':([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,27,33,34,35,37,38,40,41,46,47,68,69,79,80,81,82,84,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,109,110,111,113,114,115,116,125,133,135,136,137,138,144,146,149,150,153,154,155,159,162,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-81,-44,-75,-77,-78,-59,-57,-42,-38,-79,-80,-82,-67,-68,-76,-81,-53,-60,-58,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-69,-70,-71,-72,-73,-74,-84,-43,-41,-63,-64,-65,-66,-54,-83,149,-47,-24,-25,-49,-23,-45,-46,-56,-40,-48,-39,-55,]),'SUM':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,44,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,44,-76,-81,44,44,-61,-62,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-84,-63,-64,-65,-66,44,-75,44,-75,44,-83,-45,-75,-39,44,]),'SUB':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,45,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,45,-76,-81,45,45,-61,-62,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-84,-63,-64,-65,-66,45,-75,45,-75,45,-83,-45,-75,-39,45,]),'DECR':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,46,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,46,-76,-81,46,46,-61,-62,-29,-30,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-84,-63,-64,-65,-66,46,-75,46,-75,46,-83,-45,-75,-39,46,]),'INCR':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,47,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,47,-76,-81,47,47,-61,-62,-29,-30,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-84,-63,-64,-65,-66,47,-75,47,-75,47,-83,-45,-75,-39,47,]),'GT':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,48,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,48,-76,-81,48,48,-61,-62,None,None,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-84,-63,-64,-65,-66,48,-75,48,-75,48,-83,-45,-75,-39,48,]),'LT':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,49,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,49,-76,-81,49,49,-61,-62,None,None,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-84,-63,-64,-65,-66,49,-75,49,-75,49,-83,-45,-75,-39,49,]),'GE':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,50,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,50,-76,-81,50,50,-61,-62,-29,-30,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-84,-63,-64,-65,-66,50,-75,50,-75,50,-83,-45,-75,-39,50,]),'LE':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,51,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,51,-76,-81,51,51,-61,-62,-29,-30,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-84,-63,-64,-65,-66,51,-75,51,-75,51,-83,-45,-75,-39,51,]),'NE':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,52,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,52,-76,-81,52,52,-61,-62,-29,-30,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-84,-63,-64,-65,-66,52,-75,52,-75,52,-83,-45,-75,-39,52,]),'EQ':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,53,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,53,-76,-81,53,53,-61,-62,-29,-30,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-84,-63,-64,-65,-66,53,-75,53,-75,53,-83,-45,-75,-39,53,]),'LAND':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,54,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,54,-76,-81,54,54,-61,-62,-29,-30,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-84,-63,-64,-65,-66,54,-75,54,-75,54,-83,-45,-75,-39,54,]),'LOR':([8,9,22,25,26,27,37,38,40,41,46,47,66,67,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,109,113,114,115,116,120,123,124,126,127,133,149,152,159,160,],[-76,55,-81,-75,-77,-78,-38,-79,-80,-82,-67,-68,-75,55,-76,-81,55,55,-61,-62,-29,-30,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-84,-63,-64,-65,-66,55,-75,55,-75,55,-83,-45,-75,-39,55,]),'ASSIGN':([22,122,],[58,58,]),'SUM_ASS':([22,],[60,]),'SUB_ASS':([22,],[61,]),'MUL_ASS':([22,],[62,]),'DIV_ASS':([22,],[63,]),'IDIV_ASS':([22,],[64,]),'MOD_ASS':([22,],[65,]),'MUL':([22,26,38,40,41,69,84,86,109,113,114,115,116,133,],[-81,71,-79,-80,-82,-81,71,71,-84,-63,-64,-65,-66,-83,]),'DIV':([22,26,38,40,41,69,84,86,109,113,114,115,116,133,],[-81,72,-79,-80,-82,-81,72,72,-84,-63,-64,-65,-66,-83,]),'IDIV':([22,26,38,40,41,69,84,86,109,113,114,115,116,133,],[-81,73,-79,-80,-82,-81,73,73,-84,-63,-64,-65,-66,-83,]),'MOD':([22,26,38,40,41,69,84,86,109,113,114,115,116,133,],[-81,74,-79,-80,-82,-81,74,74,-84,-63,-64,-65,-66,-83,]),'LBRACKET':([22,58,69,],[59,100,59,]),'ELSE':([24,35,111,149,154,],[70,-42,-41,-45,-40,]),'SEMI':([25,26,27,33,34,37,38,40,41,46,47,68,69,79,82,84,86,87,88,89,90,91,92,93,94,99,109,113,114,115,116,121,129,133,146,149,152,159,],[-75,-77,-78,80,81,-38,-79,-80,-82,-67,-68,-76,-81,125,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-22,-84,-63,-64,-65,-66,140,144,-83,-23,-45,158,-39,]),'RPAREN':([25,26,27,37,38,40,41,46,47,66,67,68,69,82,84,86,87,88,89,90,91,92,93,94,96,97,98,109,113,114,115,116,117,118,119,120,123,126,127,128,133,145,149,151,159,160,],[-75,-77,-78,-38,-79,-80,-82,-67,-68,108,109,-76,-81,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-52,129,-51,-84,-63,-64,-65,-66,137,138,-26,-28,141,142,109,143,-83,-50,-45,-27,-39,161,]),'RBRACKET':([25,26,27,37,38,40,41,46,47,68,69,82,84,86,87,88,89,90,91,92,93,94,100,101,109,113,114,115,116,131,132,133,149,156,159,],[-75,-77,-78,-38,-79,-80,-82,-67,-68,-76,-81,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-87,133,-84,-63,-64,-65,-66,146,-86,-83,-45,-85,-39,]),'COMMA':([25,26,27,37,38,40,41,46,47,68,69,82,84,86,87,88,89,90,91,92,93,94,96,97,98,100,109,113,114,115,116,118,119,120,128,131,132,133,145,149,151,156,159,],[-75,-77,-78,-38,-79,-80,-82,-67,-68,-76,-81,-37,-61,-62,-29,-30,-31,-32,-33,-34,-35,-36,-52,130,-51,-87,-84,-63,-64,-65,-66,139,-26,-28,130,147,-86,-83,-50,-45,-27,-85,-39,]),'LBRACE':([70,134,141,142,143,157,161,],[112,112,112,112,112,112,112,]),'QUES':([108,],[134,]),'COLON':([148,149,],[157,-45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,42,]),'command':([0,1,2,42,112,135,],[4,4,43,43,136,150,]),'function_def':([0,1,2,42,112,135,],[5,5,5,5,5,5,]),'function_call':([0,1,2,42,112,135,],[6,6,6,6,6,6,]),'conditional':([0,1,2,42,112,135,],[7,7,7,7,7,7,]),'ternary_condition':([0,1,2,23,32,36,42,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,76,78,83,85,112,135,139,140,158,],[8,8,8,68,68,68,8,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,8,8,68,68,68,]),'expression':([0,1,2,23,32,36,42,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,76,78,83,85,112,135,139,140,158,],[9,9,9,67,79,82,9,87,88,89,90,91,92,93,94,99,101,102,103,104,105,106,107,120,124,124,127,9,9,120,124,160,]),'assignment':([0,1,2,42,77,112,135,],[10,10,10,10,121,10,10,]),'expression_ass':([0,1,2,42,112,135,],[11,11,11,11,11,11,]),'input':([0,1,2,42,112,135,],[12,12,12,12,12,12,]),'output':([0,1,2,42,112,135,],[13,13,13,13,13,13,]),'for_loop':([0,1,2,42,112,135,],[14,14,14,14,14,14,]),'while_loop':([0,1,2,42,112,135,],[15,15,15,15,15,15,]),'return':([0,1,2,42,112,135,],[16,16,16,16,16,16,]),'break':([0,1,2,42,112,135,],[17,17,17,17,17,17,]),'continue':([0,1,2,42,112,135,],[18,18,18,18,18,18,]),'if_elif_bloc':([0,1,2,42,112,135,],[24,24,24,24,24,24,]),'condition':([0,1,2,23,32,36,42,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,76,78,83,85,112,135,139,140,158,],[25,25,25,66,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,123,126,25,25,25,25,152,25,]),'term':([0,1,2,23,32,36,42,44,45,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,76,78,83,85,112,135,139,140,158,],[26,26,26,26,26,26,26,84,86,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'if_bloc':([0,1,2,42,70,112,135,],[35,35,35,35,111,35,35,]),'factor':([0,1,2,23,32,36,42,44,45,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,71,72,73,74,76,78,83,85,100,112,135,139,140,147,158,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,113,114,115,116,38,38,38,38,132,38,38,38,38,156,38,]),'param_list':([57,95,],[97,128,]),'param':([57,95,130,],[98,98,145,]),'bloc':([70,134,141,142,143,157,161,],[110,148,153,154,155,159,162,]),'plist':([76,],[118,]),'pitem':([76,139,],[119,151,]),'list':([100,],[131,]),'stat_bloc':([112,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','Parsing.py',12),
  ('program -> statement','program',1,'p_program','Parsing.py',13),
  ('program -> error','program',1,'p_program_error','Parsing.py',16),
  ('statement -> statement command','statement',2,'p_statement','Parsing.py',21),
  ('statement -> command','statement',1,'p_statement','Parsing.py',22),
  ('command -> function_def','command',1,'p_command','Parsing.py',26),
  ('command -> function_call','command',1,'p_command','Parsing.py',27),
  ('command -> conditional','command',1,'p_command','Parsing.py',28),
  ('command -> ternary_condition','command',1,'p_command','Parsing.py',29),
  ('command -> expression','command',1,'p_command','Parsing.py',30),
  ('command -> assignment','command',1,'p_command','Parsing.py',31),
  ('command -> expression_ass','command',1,'p_command','Parsing.py',32),
  ('command -> input','command',1,'p_command','Parsing.py',33),
  ('command -> output','command',1,'p_command','Parsing.py',34),
  ('command -> for_loop','command',1,'p_command','Parsing.py',35),
  ('command -> while_loop','command',1,'p_command','Parsing.py',36),
  ('command -> return','command',1,'p_command','Parsing.py',37),
  ('command -> break','command',1,'p_command','Parsing.py',38),
  ('command -> continue','command',1,'p_command','Parsing.py',39),
  ('command -> COMMENT','command',1,'p_command','Parsing.py',40),
  ('command -> NEWLINE','command',1,'p_command','Parsing.py',41),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_assignment','Parsing.py',47),
  ('assignment -> ID ASSIGN LBRACKET list RBRACKET','assignment',5,'p_assignment','Parsing.py',48),
  ('input -> SCAN LPAREN ID RPAREN','input',4,'p_input','Parsing.py',58),
  ('output -> PRINT LPAREN plist RPAREN','output',4,'p_output','Parsing.py',63),
  ('plist -> pitem','plist',1,'p_plist','Parsing.py',70),
  ('plist -> plist COMMA pitem','plist',3,'p_plist','Parsing.py',71),
  ('pitem -> expression','pitem',1,'p_item_expr','Parsing.py',79),
  ('condition -> expression GT expression','condition',3,'p_condition','Parsing.py',83),
  ('condition -> expression LT expression','condition',3,'p_condition','Parsing.py',84),
  ('condition -> expression GE expression','condition',3,'p_condition','Parsing.py',85),
  ('condition -> expression LE expression','condition',3,'p_condition','Parsing.py',86),
  ('condition -> expression NE expression','condition',3,'p_condition','Parsing.py',87),
  ('condition -> expression EQ expression','condition',3,'p_condition','Parsing.py',88),
  ('condition -> expression LAND expression','condition',3,'p_condition','Parsing.py',89),
  ('condition -> expression LOR expression','condition',3,'p_condition','Parsing.py',90),
  ('condition -> LNOT expression','condition',2,'p_condition','Parsing.py',91),
  ('condition -> BOOLEAN','condition',1,'p_condition','Parsing.py',92),
  ('ternary_condition -> LPAREN condition RPAREN QUES bloc COLON bloc','ternary_condition',7,'p_ternary','Parsing.py',101),
  ('if_bloc -> IF LPAREN condition RPAREN bloc','if_bloc',5,'p_if_bloc','Parsing.py',104),
  ('if_elif_bloc -> if_elif_bloc ELSE if_bloc','if_elif_bloc',3,'p_if_elif_bloc','Parsing.py',107),
  ('if_elif_bloc -> if_bloc','if_elif_bloc',1,'p_if_elif_bloc','Parsing.py',108),
  ('conditional -> if_elif_bloc ELSE bloc','conditional',3,'p_conditional','Parsing.py',115),
  ('conditional -> if_elif_bloc','conditional',1,'p_conditional','Parsing.py',116),
  ('bloc -> LBRACE stat_bloc RBRACE','bloc',3,'p_bloc','Parsing.py',123),
  ('stat_bloc -> stat_bloc command','stat_bloc',2,'p_stat_bloc','Parsing.py',127),
  ('stat_bloc -> command','stat_bloc',1,'p_stat_bloc','Parsing.py',128),
  ('function_def -> FUNCTION ID LPAREN param_list RPAREN bloc','function_def',6,'p_function_def','Parsing.py',137),
  ('function_call -> ID LPAREN param_list RPAREN SEMI','function_call',5,'p_function_call','Parsing.py',140),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','Parsing.py',143),
  ('param_list -> param','param_list',1,'p_param_list','Parsing.py',144),
  ('param -> ID','param',1,'p_param','Parsing.py',152),
  ('return -> RETURN expression','return',2,'p_return','Parsing.py',155),
  ('return -> RETURN expression SEMI','return',3,'p_return','Parsing.py',156),
  ('for_loop -> FOR LPAREN assignment SEMI condition SEMI expression RPAREN bloc','for_loop',9,'p_for_loop','Parsing.py',161),
  ('while_loop -> WHILE LPAREN condition RPAREN bloc','while_loop',5,'p_while_loop','Parsing.py',164),
  ('continue -> CONTINUE','continue',1,'p_continue','Parsing.py',167),
  ('continue -> CONTINUE SEMI','continue',2,'p_continue','Parsing.py',168),
  ('break -> BREAK','break',1,'p_break','Parsing.py',171),
  ('break -> BREAK SEMI','break',2,'p_break','Parsing.py',172),
  ('expression -> expression SUM term','expression',3,'p_binary_operators','Parsing.py',176),
  ('expression -> expression SUB term','expression',3,'p_binary_operators','Parsing.py',177),
  ('term -> term MUL factor','term',3,'p_binary_operators','Parsing.py',178),
  ('term -> term DIV factor','term',3,'p_binary_operators','Parsing.py',179),
  ('term -> term IDIV factor','term',3,'p_binary_operators','Parsing.py',180),
  ('term -> term MOD factor','term',3,'p_binary_operators','Parsing.py',181),
  ('expression -> expression DECR','expression',2,'p_unary_operators','Parsing.py',196),
  ('expression -> expression INCR','expression',2,'p_unary_operators','Parsing.py',197),
  ('expression_ass -> ID SUM_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',204),
  ('expression_ass -> ID SUB_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',205),
  ('expression_ass -> ID MUL_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',206),
  ('expression_ass -> ID DIV_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',207),
  ('expression_ass -> ID IDIV_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',208),
  ('expression_ass -> ID MOD_ASS expression','expression_ass',3,'p_binary_operators_ass','Parsing.py',209),
  ('expression -> condition','expression',1,'p_expression','Parsing.py',224),
  ('expression -> ternary_condition','expression',1,'p_expression','Parsing.py',225),
  ('expression -> term','expression',1,'p_expression','Parsing.py',226),
  ('expression -> NULL','expression',1,'p_expression','Parsing.py',227),
  ('term -> factor','term',1,'p_term_factor','Parsing.py',231),
  ('factor -> NUMBER','factor',1,'p_factor_num','Parsing.py',235),
  ('factor -> ID','factor',1,'p_factor_num','Parsing.py',236),
  ('factor -> STRING','factor',1,'p_factor_num','Parsing.py',237),
  ('factor -> ID LBRACKET expression RBRACKET','factor',4,'p_factor_num','Parsing.py',238),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','Parsing.py',250),
  ('list -> list COMMA factor','list',3,'p_list','Parsing.py',253),
  ('list -> factor','list',1,'p_list','Parsing.py',254),
  ('list -> <empty>','list',0,'p_list','Parsing.py',255),
]
