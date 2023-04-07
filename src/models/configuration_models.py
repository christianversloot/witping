from pydantic import BaseModel
from typing import List

class WitConfig(BaseModel):
    '''
        A WitConfig represents the configuration of a Wit.

        Implements
        ----------
        BaseModel: pydantic.BaseModel
            Pydantic base model.
    '''
    pass

class GitWitConfig(WitConfig):
    '''
        A GitWitConfig represents the configuration of a GitWit.
        A GitWit listens to releases in Git repositories.
        Currently, there is only support for GitHub repositories.

        Implements
        ----------
        WitConfig
            Wit configuration base class.
    '''
    username: str
    repository: str

class PingConfig(BaseModel):
    '''
        A PingConfig represents the configuration of a Ping.

        Implements
        ----------
        BaseModel: pydantic.BaseModel
            Pydantic base model.
    '''
    pass

class WitPingConfigPair(BaseModel):
    '''
        A WitPingConfigPair represents a pair of a WitConfig and a
        PingConfig. When a Wit configured by the WitConfig of a pair
        fires, the Ping configured by its corresponding PingConfig is
        triggered.

        Implements
        ----------
        BaseModel: pydantic.BaseModel
            Pydantic base model.
    '''
    wit_config: WitConfig
    ping_config: PingConfig


class MeshConfig(BaseModel):
    '''
        A MeshConfig represents the configuration of a Mesh.

        Implements
        ----------
        BaseModel: pydantic.BaseModel
            Pydantic base model.
    '''
    config_pairs: List[WitPingConfigPair]