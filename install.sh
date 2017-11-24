GITHOOKER_HOME="~/.githookkk"
GITHOOKER_NAME="githookkk"

main() {
  git clone https://github.com/luochenxun/githooker.git $GITHOOKER_HOME

  sudo mv GITHOOKER_HOME/githookkk /usr/local/bin/$GITHOOKER_NAME
  sudo chmod a+x /usr/local/bin/$GITHOOKER_NAME
  echo "Congratulation, githooker has installed successfully!"
}


main

