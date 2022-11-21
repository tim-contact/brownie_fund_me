#!/usr/bin/env python3

from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIORNMENTS


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to the fundme contract
    # if we are on a persistent network like goerli, use the associated address
    # otherwise, deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed.")



    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(fund_me.address)
    return fund_me


def main():
    deploy_fund_me()
