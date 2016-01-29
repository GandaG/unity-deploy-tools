#! /bin/sh

curl -o .sauce/dotgraph.pkg http://www.graphviz.org/pub/graphviz/stable/macos/mountainlion/graphviz-2.36.0.pkg

if [ "$verbose" == "True" ];
then
    sudo installer -dumplog -package .sauce/dotgraph.pkg -target /
else
    sudo installer -package .sauce/dotgraph.pkg -target /
fi

echo "OUTPUT_DIRECTORY=./.sauce/docs/output/
OPTIMIZE_OUTPUT_JAVA=YES
GENERATE_LATEX=NO
EXCLUDE=./.sauce/ .travis.yml .sauce.ini
RECURSIVE=YES
INPUT=./
PROJECT_NAME=$projectname
PROJECT_NUMBER=$
PROJECT_BRIEF=$
PROJECT_LOGO=$
EXTRACT_ALL=$
EXTRACT_STATIC=$
EXTRACT_PRIVATE=$
EXTRACT_PACKAGE=$
SEARCHENGINE=$
GENERATE_TREEVIEW=$
CLASS_DIAGRAMS=$
HAVE_DOT=$" >>./.sauce/docs/Doxyfile



