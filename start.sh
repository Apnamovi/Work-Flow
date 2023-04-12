if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Apnamovi/Work-Flow.git /Work-Flow
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Work-Flow
fi
cd /Work-Flow
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
