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
EXCLUDE=./.sauce/ .travis.yml .sauce.ini ./Project/
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

curl -o .sauce/doxygen.dmg http://ftp.stack.nl/pub/users/dimitri/Doxygen-1.8.11.dmg

sudo hdiutil attach .sauce/doxygen.dmg

sudo ditto /Volumes/Doxygen /Applications/Doxygen

sudo rm -rf /Applications/Doxygen.app

sudo mv /Applications/Doxygen/Doxygen.app /Applications/

sudo rm -r /Applications/Doxygen

sudo hdiutil detach /Volumes/doxygen

/Applications/Doxygen.app/Contents/Resources/doxygen ./.sauce/docs/Doxyfile

# go to the out directory and create a *new* Git repo
cd .sauce/docs/output/ || exit 1
git init

# inside this git repo we'll pretend to be a new user
git config user.name "Travis-CI Doxygen Deployment"
git config user.email "doxygen@deployment_to.github.pages"

# The first and only commit to this new Git repo contains all the
# files present with the commit message "Deploying to GitHub Pages"
git add .
git commit -m "Deploying to GitHub Pages"

# Force push from the current repo's master branch to the remote
# repo's gh-pages branch. (All previous history on the gh-pages branch
# will be lost, since we are overwriting it.) We redirect any output to
# /dev/null to hide any sensitive credential data that might otherwise be exposed.
git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" master:gh-pages > /dev/null 2>&1

#just in case travis doesn't know what to do
cd ../../.. || exit 1
