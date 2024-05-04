from typing import Optional

from pydantic import BaseModel


class Subnet(BaseModel):
    address: str
    mask: str


class Gateway(BaseModel):
    address: str
    name: str


class GatewaySubnetConnection(BaseModel):
    gateway_network: str
    gateway: Gateway
    subnet: Subnet


class NetworkInterface(BaseModel):
    ifc_name: str
    gateways: list[Gateway]
    default_gateway: Optional[Gateway]
    subnets: list[Subnet]
    gateway_subnet_connections: list[GatewaySubnetConnection]

