import json
import os
from models.configuration_models import MeshConfig

class Mesh:
    '''
        The Mesh class connects Wits and Pings via a WitPing configuration.
        Wits fire if they notice a change per their Wit threshold whereas
        Pings subsequently perform an action based on the Wit firing.
        The Mesh orchestrates everything.
    '''
    slots = ['config']

    def __init__(self) -> None:
        '''
            Constructor.

            Returns
            -------
            Void
        '''
        self.config = self.load_configuration()


    def load_configuration(self) -> MeshConfig:
        '''
            Load configuration from environment or JSON file.
            Initially (and recommended from production), configuration is
            loaded from environment variable (WITPING_CONFIGURATION). If
            unavailable, WitPing attempts to load configuration from a file
            called configuration.json in the root directory.

            Attributes
            ----------
            self: Mesh
                Self-reference.

            Returns
            -------
            mesh_config: MeshConfig
                Configuration of the mesh.
        '''
        env_configuration = os.getenv('WITPING_CONFIGURATION')

        if env_configuration is not None:
            return json.loads(env_configuration)

        env_path = os.path.join(os.getcwd(), '..', 'configuration.json')

        with open(env_path, 'r') as env_config_file:
            return json.load(env_config_file)