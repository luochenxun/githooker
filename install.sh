USER_HOME=`echo ~`
GITHOOKER_HOME=$USER_HOME"/.githookkk"
GITHOOKER_NAME="githookkk"

main() {
  git clone https://github.com/luochenxun/githooker.git $GITHOOKER_HOME

  echo "Install will move the githooker to your /usr/local/bin/ directory, please input your system password"
  sudo mv $GITHOOKER_HOME/githookkk /usr/local/bin/$GITHOOKER_NAME
  sudo chmod a+x /usr/local/bin/$GITHOOKER_NAME
  echo "Congratulation, githooker has installed successfully!"
}


main
