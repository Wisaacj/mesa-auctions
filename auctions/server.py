from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from auctions.agents import Auctioneer, EarlyBidder, SniperBidder
from auctions.model import AuctionHouse

model_params = {
    "snipers": UserSettableParameter(
        "slider", "Sniper Bidders", 3, 1, 10, description="Number of sniper bidders"
    ),
    "earlyBidders": UserSettableParameter(
        "slider", "Early Bidders", 7, 1, 20, description="Number of early (conventional) bidders"
    ),
    "maxValueStandardDeviation": UserSettableParameter(
        "slider", "Strd Dev. Agents", 150, 0, 350, description="Standard deviation of bidders' internal valuations / max bids"
    ),
    "bidProba": UserSettableParameter(
        "slider", "Bid Probability", 0.75, 0, 1, 0.05, description="Bid Probability"
    ),
    "watchProba": UserSettableParameter(
        "slider", "Watch Probability", 0.75, 0, 1, 0.05, description="Number of early (conventional) bidders"
    ),
    "bidTimeframe": UserSettableParameter(
        "slider", "Sniper Activation Window", 7, 1, 20, description="Window of time (from end of auction) where the snipers are active"
    ),
    "auctionLength": UserSettableParameter(
        "slider", "Auction Length", 100, 50, 200, description="Length of Auction"
    ),
}

# Map data to chart in the ChartModule
chart_element = ChartModule([
    {"Label": "Second Highest Bid", "Color": "#46FF33"},
    {"Label": "Highest Bid", "Color": "#3349FF"}
])

# Create instance of Mesa ModularServer
server = ModularServer(
    AuctionHouse,
    [chart_element],
    "Second-Price Auction Model",
    model_params=model_params
)