if [ -z $FLASK_CONFIG ]; then
    export FLASK_CONFIG="development"
fi

/usr/bin/env python3 simple_app.py
