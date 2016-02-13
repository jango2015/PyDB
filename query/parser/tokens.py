from pyparsing import Literal, CaselessLiteral, Upcase, Word, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword


# define SQL tokens
selectStmt = Forward()
selectToken = Keyword("select", caseless=True)
fromToken   = Keyword("from", caseless=True)

ident          = Word( alphas, alphanums + "_$" ).setName("identifier")
columnName     = Upcase( delimitedList( ident, ".", combine=True ) )
columnNameList = Group( delimitedList( columnName ) )
tableName      = Upcase( delimitedList( ident, ".", combine=True ) )
tableNameList  = Group( delimitedList( tableName ) )

whereExpression = Forward()
joinExpression = Forward()
and_ = Keyword("and", caseless=True)
or_ = Keyword("or", caseless=True)
in_ = Keyword("in", caseless=True)
on_ = Keyword("on", caseless=True)