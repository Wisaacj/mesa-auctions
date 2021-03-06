# ABM: Second-Price Auctions

Auctions have existed for millennia, dating back to the Ancient Greeks. They facilitate a vast swathe of transactions each year, with over 17.6 billion dollars of art and antiques sold via auction in 2020, not to mention the mammoth volume of auction-based transactions in the general financial system. Total assets under management for the hedge-fund industry eclipses $4.5 trillion (with a ‘t’) dollars and many of these institutions use auctions for the sale of their assets. The sheer volume of transactions by auctions and the power they wield warrants an investigation into optimising such systems.

We aim to investigate various bidding strategies in a second-price auction system. The goal of such a system is for both buyers and sellers to pay/receive a ‘fair’ price for the goods on sale - mitigating against the infamous “winner’s curse”. We introduce two types of bidders: early and so-called ‘sniper’ bidders, which we model using a Python Agent-Based Modelling framework “Mesa”. The characteristic distinction between the two is that whilst early bidders are permitted to bid throughout the auction, with acute scale factors used to update their bids, sniper bidders wait until the end to swoop in and place a large bid in the hope they ‘steal’ the item at the last moment.

## Repository Architecture

> root - Contains run.py and batch-run.py for running the webserver visualisation / generating datasets respectively

> analysis - Data analysis notebooks used in the hypothesis analysis section of the report

> auctions - Agent-based model of second price auctions (see model design)

> data - All datasets used for data analysis

> images - Images used in the report

## Model Design

``` python
from auctions.model import AuctionHouse
from auctions.bidder import Bidder
from auctions.agents import Auctioneer, EarlyBidder, SniperBidder
from auctions.alternate_agents import AAuctioneer, ASniperBidder
```

`AuctionHouse` is the overarching model, initialising the `Auctioneer`, `EarlyBidder`, `SniperBidder` agents. It contains a `DataCollector` object which (as the name implies) collects metrics about the model and the agents throughout the simulation, as well as a `RandomActivationByType` object which calls agents' logic function in a stratified random order at each timestep.

Each agent inherits from the Bidder class, which is a generic bidding agent that initialises internal properties. These properties are intialised as follows in `AuctionHouse` when agents are generated:

1. maxBid drawn from a normal distribution with mean = 1000, standard deviation = (user inputted)
2. valuation drawn from a normal distribution with mean = 500, standard deviation = (user inputted)

The different agents utilise different private valuation update functions:

1. EarlyBidder bids are updated by a scalar factor drawn from uniform distribution [1.0, 1.2]
     + min(self.valuation * scalar, self.valuation)
2. Naive SniperBidder bids are updated by a scalar factor drawn from uniform distribution [1.0, 2.0]
     + min(self.valuation * scalar, self.maxBid)
3. Intelligent SniperBidder bids are updated by the average bid increase (observed over the whole auciton)
     + min(self.auctioneer.getSecondHighestBid() + self.auctioneer.getBidIncreaseAverage() + 5, self.maxBid)

The python file "alternate_agents.py" contains the original naive SniperBidder agent and the corresponding Auctioneer agent which interacts with it.

## Running our model

Install mesa with `pip install mesa`. Run the webserver visualtion with `python run.py` or create a batch dataset with `python batch-run.py`.
