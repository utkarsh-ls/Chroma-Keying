# FILE=./Frame*
# if test -f "$FILE"; then
#     rm Frame*
# fi

if test -d "./2/"; then
    rm -r 2
fi
if test -d "./1/"; then
    rm -r 1
fi
if test -f "3.avi"; then
    rm merged.avi
fi