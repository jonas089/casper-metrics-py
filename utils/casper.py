import pycspr
from pycspr import NodeClient
from pycspr import NodeConnection
from pycspr.types import CL_URef

def Client(node_host, node_port, node_port_rpc, node_port_sse) -> NodeClient:
    """Returns a pycspr client instance.
    """
    return NodeClient(NodeConnection(
        host=node_host,
        port_rest=node_port,
        port_rpc=node_port_rpc,
        port_sse=node_port_sse
    ))
