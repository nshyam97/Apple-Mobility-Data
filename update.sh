#!/bin/sh
export PATH=$PATH:/usr/local/bin/git-credential-osxkeychain
/usr/local/bin/jupyter nbconvert --to notebook --execute --inplace trend_analysis.ipynb
git add .
git commit -m "daily update jupyter"
/usr/local/bin/git push origin master