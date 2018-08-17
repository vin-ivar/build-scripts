import sys
import torch
import argparse
from types import SimpleNamespace
from sacred import Experiment
from sacred.observers import MongoObserver, TinyDbObserver, TelegramObserver

ex = Experiment('mnist')

ex.observers.append(MongoObserver.create())
ex.observers.append(TelegramObserver.from_config('telegram.json'))

parser = argparse.ArgumentParser()
parser.add_argument('--device', action='store', default=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu'))
parser.add_argument('--data', action='store', default='./data/')

ex.add_config({'args': vars(parser.parse_args())})

@ex.main
def main(_run, args):
    args = SimpleNamespace(**args)

ex.run()

