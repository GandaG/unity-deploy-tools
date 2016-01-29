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
PROJECT_NUMBER=$TRAVIS_TAG
PROJECT_BRIEF=$description
PROJECT_LOGO=$logo
EXTRACT_ALL=$include_non_documented
EXTRACT_STATIC=$include_non_documented
EXTRACT_PRIVATE=$include_privates
EXTRACT_PACKAGE=$include_privates
SEARCHENGINE=$include_search
GENERATE_TREEVIEW=$include_nav_panel
CLASS_DIAGRAMS=$gen_diagrams
HAVE_DOT=$class_diagrams" >>./.sauce/docs/Doxyfile



