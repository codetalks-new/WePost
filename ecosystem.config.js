module.exports = {
  apps: [
    {
      name: "wepost",
      script: "./gunicorn_main.py",
      interpreter: "/home/ubuntu/.pyenv/versions/wepost/bin/python",
      args: "wepost.wsgi"
    }
  ]
};
