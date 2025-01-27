web: node server.js  # Run Express.js frontend
backend: gunicorn -w 4 -k gevent chat:app  # Run Python backend with Gunicorn
