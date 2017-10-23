GOSTCoin Web Wallet
===================

Django-powered web wallet for [GOSTCoin](http://gostco.in)


# Celery development workers

    celery -A gst_web_wallet.celery worker --loglevel=debug

    celery -A gst_web_wallet.celery beat --loglevel=debug
