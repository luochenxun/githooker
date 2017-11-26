USER_HOME=`echo ~`
GITHOOKER_HOME=$USER_HOME"/.githooker"
GITHOOKER_NAME="githooker"

main() {
  if [[ -d $GITHOOKER_HOME ]]; then
    cd $GITHOOKER_HOME
    git clean -df
    git reset --hard HEAD
    git pull
  else
     git clone https://github.com/luochenxun/githooker.git $GITHOOKER_HOME
  fi

  echo "\n---------------------------------------"
  echo "Install will move the githooker to your /usr/local/bin/ directory, please input your system password"
  sudo cp $GITHOOKER_HOME/$GITHOOKER_NAME /usr/local/bin/$GITHOOKER_NAME
  sudo chmod a+x /usr/local/bin/$GITHOOKER_NAME

  echo "\n\nCongratulation, githooker has installed successfully!"
}


main
