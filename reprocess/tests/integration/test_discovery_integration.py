import json
import pytest
# import unittest
from flask import Flask

from reprocess.discovery import construct_blueprint
from reprocess.tests.mock.process_memory import ProcessMemoryApi
from reprocess.tests.mock.event_manager import EventManager
from platform_sdk.domain.reader import DomainReaderApi


class DiscoveryTest():
    domain_reader_params = {
        'api_url':'http://0.0.0.0:8089/'
    }
    _app = Flask(__name__, instance_relative_config=True)
    _app_client = _app.test_client()
    _app.register_blueprint(
        construct_blueprint(
            ProcessMemoryApi(),
            DomainReaderApi(domain_reader_params),
            EventManager()))
    

    def test_discovery_integration(self):
        # arrange
        request_contract = { 'solution': 'SAGER', 'app': 'SAGER_Cenario',
                             'instance_id': 1}

        # action
        response = self._app_client.post('/discovery/check',
                                         data=json.dumps(request_contract),
                                         follow_redirects=True,
                                         mimetype='application/json')
        # assert
        assert True

    def process_memory_should_use(self, app, map, entity, process_memory):
        # arrange
        entity = {
            'id':'fddcd109-40f2-434b-97c2-13053dfb7967'
        }
        app = 'SAGER_Cenario'
        map = 'criteriopotencia'
        # action
        # TODO: decidir se vai fazer o teste direto aqui ou de ponta a ponta.
        response = self._app_client.get('/discovery/check',
                                         follow_redirects=True,
                                         mimetype='application/json')

        # assert
        assert 200 == response.default_status

test = DiscoveryTest()
test.test_discovery_integration()

