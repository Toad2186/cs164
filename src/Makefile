# Top-level Makefile for Project 1.
# 
# Targets:
#   gmake [ default ]        Compiles sources in src directory
#   gmake check              Compiles sources and runs tests.  The parameter
#                            APYC indicates which compiler to run.
#   gmake clean              Removes unnecessary files, including those that
#                            are reproducible.
#   gmake depend	     Compute makefile dependencies and store
#                            in .depend.  Use this whenever you add a new
#                            source file or change an #include line.
#   gmake really-clean       Same as 'clean', also removes the file .depend.
#

APYC = $(shell echo `pwd`/../apyc)

CXXFLAGS = -g -Wall

# List of normal C++ sources.  Add any new ones here
SRCS = apyc.cc ast.cc tokens.cc stmts.cc exprs.cc

# C++ top-level (i.e., as opposed to #included) sources that are generated
# by other rules in this Makefile.
GENERATED_SRCS = apyc-parser.cc 

# List of all C++ object files
OBJS = $(SRCS:.cc=.o) $(GENERATED_SRCS:.cc=.o)

# List of all C++ sources generated by tools
OTHER_SRCS = $(GENERATED_SRCS) \
	     apyc-lexer.l apyc-lexer.cc apyc-lexer.hh \
             apyc-parser.y apyc-parser.hh \
             horn-common.h horn-parse-lex.cc

.PHONY: default compile check clean really-clean depend

default: compile

compile: ../apyc

$(OTHER_SRCS): parser-sentinel

# The parser-sentinel file is a device that is used to group all the files
# generated by horn into one dependency.  Each time we generate these files, 
# we update the modify date on parser-sentinel.  The generated files in turn
# depend on parser-sentinel, and it depends on apyc.hn. So, whenever apyc.hn
# is changed, any compilation that depends on a generated file will cause 
# horn to rebuild the generated files (OTHER_SRCS).
parser-sentinel: apyc.hn
	horn $<
	touch parser-sentinel

../apyc: $(OBJS)
	$(CXX) -g -o $@ $(OBJS)

check: 
	$(MAKE) -C .. APYC=$(APYC) check

clean:
	$(RM) *~ *.o *.pyc *.ast *.tab.c *.output 
	$(RM) tests/*~ tests/*/*~
	$(RM) $(GENERATED_SRCS) $(OTHER_SRCS) parser-sentinel

really-clean: clean
	$(RM) .depend

# Dependencies

.depend:
	touch .depend
	$(MAKE) depend

depend: $(OTHER_SRCS)
	$(RM) .depend
	$(CXX) -MM $(OBJS:.o=.cc) > .depend

-include .depend
