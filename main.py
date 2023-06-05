import asyncio
from threading import Thread
from dependency_injector.wiring import inject, Provide

from app.pkg.connectors import Connectors
from app.workers import Workers, Producer, Consumer
from app.configuration import __containers__


@inject
def producer(
    produce_worker: Producer = Provide(Workers.producer)
):
    produce_worker.main()

@inject
def consumer(
    consume_worker: Consumer = Provide(Workers.consumer)
):
    asyncio.run(consume_worker.main())


if __name__ == '__main__':
    __containers__.wire_packages(pkg_name=__name__)
    Thread(target=producer, args=()).start()
    Thread(target=consumer, args=()).start()
