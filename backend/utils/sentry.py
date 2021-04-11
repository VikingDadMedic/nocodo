import sentry_sdk

from utils.config import settings


def sentry_init():
    sentry_sdk.init(
        settings.sentry_url,
        traces_sample_rate=1.0
    )
